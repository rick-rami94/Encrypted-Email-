# Importing the required libraries
import email, smtplib, ssl,getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('''█▀▀ █▄░█ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █▀▀ █▀▄
██▄ █░▀█ █▄▄ █▀▄ ░█░ █▀▀ ░█░ ██▄ █▄▀

█▀▀ █▀▄▀█ ▄▀█ █ █░░
██▄ █░▀░█ █▀█ █ █▄▄''')


#declaring the variables needed to create the email and message.
supported_servers = {'outlook':'smtp-mail.outlook.com', 'gmail':'smtp.gmail.com', 'yahoo': 'smtp.mail.yahoo.com'}
selected_server = supported_servers[input('\nPlease select your email provider: outlook, gmail, yahoo\nType your provider here:')]
sender_email = input('Please input your email address: ')
sender_password = getpass.getpass()
receiver_email = input('Please input destination email address: ')
subject = input(' Subject: ')
body = input('Body: ')

# Creating the email with the MIMEMultipart
msg = MIMEMultipart()
msg['From'],msg['To'],msg['Subject'],msg['Bcc'] = sender_email, receiver_email, subject, receiver_email
msg.attach(MIMEText(body,'plain'))
# Converting the message to a string 
text = msg.as_string()
#creating the ssl context 
context = ssl.create_default_context()
# connecting to email server and sending email. 
with smtplib.SMTP(selected_server,587) as s:
    s.starttls(context=context)
    s.login(sender_email,sender_password)
    s.sendmail(sender_email,receiver_email,text)
    
