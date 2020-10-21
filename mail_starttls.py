 # Send email from python using .starttls encrpyted connection

# Import the modules
import smtplib
import ssl

# Create the context object which will verify connection certificates and host
context = ssl.create_default_context()

# Port for SMTP
port = 587

# Email Id and Password of the sender
EMAIL = "harshharshharshharsh46@gmail.com"
PASS = "harsh@123"

with smtplib.SMTP("smtp.gmail.com", port) as server:
    # Verify identity to the gmail server
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    # Login to the server
    server.login(EMAIL, PASS)
    msg = f"Subject:HI\n\nHow are you doing?"
    server.sendmail(EMAIL, "hs804527@gmail.com", msg)




