from os import getenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
from os import getenv

sender_email = getenv('SENDER_EMAIL')
receiver_email = getenv('RECEIVER_EMAIL')
password = getpass("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Test email"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Test Email"""
html = """\
<html>
  <body>
    <p>Test Email</p>
    <img src="https://www.gettyimages.pt/gi-resources/images/500px/983794168.jpg">
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )