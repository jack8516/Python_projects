import ssl
from email.message import EmailMessage
import smtplib
# adres roboczy to tcra2023python@gmail.com, hasło: ?12345QwErTy!aX%

sender_email = "tcra2023python@gmail.com"
email_password = "fvidtbvomtlhbfab"
receiver_email = "jack85@tlen.pl"

subject = "Nowe konto testowe"
body = "Udało Ci się wysłać maila!"
em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['Subject'] = subject
em.set_content(body)

contex = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contex) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())