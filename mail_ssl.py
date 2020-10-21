# Send mails using smtplib and smtplib.smtp_ssl encryption

# Import necessary modules
import smtplib
import ssl

# Create object of context which verifies host and other certificates.
context = ssl.create_default_context()

# Mail Id using which you will send mails.
MAIL = "*********************@gmail.com"

# Password of the mail
PASS = "**********"

# Port
port = 465

# Creating SMTP connection for sending mails
with smtplib.SMTP_SSL("smtp.gmail.com", port , context=context) as server:
    server.login(MAIL, PASS)
    msg = f"Subject:HI\n\nHow are you doing?"
    server.sendmail(MAIL, "*************@gmail.com", msg)
