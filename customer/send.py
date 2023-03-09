
from email.message import EmailMessage
import ssl
import smtplib


def sendEmail(mail_receiver,massege):
    email_sender = 'suiuikhalifa@gmail.com'
    password = 'rlulfpmdsrguawtx'

    subject = "From Django"

    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = mail_receiver
    email['Subject'] = subject
    email.set_content(massege)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender, mail_receiver, email.as_string())