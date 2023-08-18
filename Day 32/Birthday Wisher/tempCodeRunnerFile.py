with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=data['email'],msg=f"Subject:Happy Birthday!\n\n{letter}")
        print('SENT')