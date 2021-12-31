import smtplib
import datetime as dt
import random
   
weekday = dt.datetime.now()
monday = weekday.weekday()

if monday == 0:
    with open('quotes.txt') as quote:
        all_quotes =  quote.readlines()
        random_quote = random.choice(all_quotes)

    my_email =  'insert email'
    password = 'insert password'

    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='insert email to send to', msg=f'Subject:Inpiring Quote\n\n{random_quote}')