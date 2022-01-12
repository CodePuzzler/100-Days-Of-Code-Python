# Day32 of my 100DaysOfCode Challenge
# send a quote on monday using email
import random
import smtplib
import datetime as dt


# function to send email
def send_email(_quote):
    my_email = "abc@example.com"
    password = "qwerty@1234"
    # opening connection using 'with', as done for opening a file
    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="email@example.com",
            msg=f"Subject:Monday Motivation\n\n{_quote}"
        )


# accessing the file and choose a random quote and call send email on monday
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    # print(quote)
    send_email(quote)
