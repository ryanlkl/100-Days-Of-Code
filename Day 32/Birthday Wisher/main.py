##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "pythonsmtp94@gmail.com"
MY_PASSWORD = "pkzqmcqayhihxbns"

# Load birthday data from csv file
birthday_file = pandas.read_csv("Day 32\\Birthday Wisher\\birthdays.csv")
birthday_data = birthday_file.to_dict(orient="records")

# Get today's date
today = dt.datetime.now()
month = today.month
day = today.day

birthday_today = [data for data in birthday_data if data['month'] == month and data['day'] == day]

for data in birthday_today:

    template_number = random.randint(1,3)
    template_path = f"Day 32\\Birthday Wisher\\letter_templates\\letter_{template_number}.txt"
    with open(template_path) as letter:
      contents = letter.read()
      new_contents = contents.replace("[NAME]",data['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        subject = f"Subject: Happy Birthday, {data['name']}!\n\n"
        email_content = subject + new_contents

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=data['email'],
                            msg=email_content)
        print('SENT')
