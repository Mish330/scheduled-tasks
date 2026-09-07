import os
import datetime as dt
import pandas as pd
import random as rnd
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day

birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")
print(birthdays_dict)

for birthday in birthdays_dict:
    if birthday["month"] == month and birthday[ "day"] == day:
        print("Happy birthday")
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"./letter_templates/letter_{rnd.randint(1,3)}.txt", "r") as file:
            letter_text = file.read()
            # print(letter_text)
            new_text = letter_text.replace("[NAME]", birthday["name"])
            print(new_text)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
            msg=f"Subject: Happy birthday!\n\n{new_text}"
            )
