import smtplib
import codecs
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
# server.login("management.flashadeal@gmail.com" , "jlmdeyouhpnljmih")

# message = """From: Flashadeal Management <management.flashadeal@gmail.com>
# MIME-Version: 1.0
# Content-type: text/html
# Subject: Thanks for Subscribing

# """
# message += "Welcome to Flashadeal"
# file = codecs.open("email/welcomeEmail.html", "r", "utf-8")
# message += file.read()

# server.sendmail("management.flashadeal@gmail.com" , "j_kesineni@yahoo.co.in" , message)

def send_mail(bodyContent,to_email):
    from_email = 'management.flashadeal@gmail.com'
    subject = 'Welcome to Flashadeal'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(bodyContent, "html"))
    msgBody = message.as_string()

    server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
    server.login("management.flashadeal@gmail.com" , "jlmdeyouhpnljmih")
    server.sendmail(from_email, to_email, msgBody)
    server.quit()

with open("email/welcomeEmail.html" , 'r') as file:
    l = ['gayatridivi1234@gmail.com']
    for i in l:
        send_mail(file.read() , i)