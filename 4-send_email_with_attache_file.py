import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os
import sys
 
fromaddr = "From_Email_Address"
toaddr = "To_Email_Address"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Ahmed Khaled"
 
body = "this is the message"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "message.txt"
attachment = open("message.txt", "r+")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.live.com', 587)
server.starttls()
server.login(fromaddr, "From_Email_Password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()