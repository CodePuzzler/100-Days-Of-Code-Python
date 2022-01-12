# Day32 of my 100DaysOfCode Challenge
# Sending Emails using python

import smtplib

my_email = "abc@example.com"
password = "qwerty@1234"

# simpler way, here we have to close the connection
# connection = smtplib.SMTP("smtp.example.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="email@example.com", msg="Happy Birthday")
# connection.close()

# opening connection using 'with', as done for opening a file
with smtplib.SMTP("smtp.example.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="email@example.com",
        msg="Happy Birthday"
    )
