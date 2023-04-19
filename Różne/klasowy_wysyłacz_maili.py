import ssl
from email.message import EmailMessage
import smtplib
# adres roboczy to tcra2023python@gmail.com, hasło: fvidtbvomtlhbfab


class Email:
    def __init__(self):
        self.sender_email = "tcra2023python@gmail.com"
        self.email_password = "fvidtbvomtlhbfab"
        self.receiver_email = "jack85@tlen.pl"

        self.subject = "Nowe konto testowe"
        self.body = "Udało Ci się wysłać maila!"
        self.em = EmailMessage()
        self.em['From'] = self.sender_email
        self.em['To'] = self.receiver_email
        self.em['Subject'] = self.subject
        self.em.set_content(self.body)

        self.contex = ssl.create_default_context()

    def send_email(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.contex) as smtp:
            smtp.login(self.sender_email, self.email_password)
            smtp.sendmail(self.sender_email, self.receiver_email, self.em.as_string())


new_email = Email()
new_email.send_email()
