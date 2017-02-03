#Hpta4Arms 
is a buggy tool used to spy on your friends it consists of 4 main arms as i love to call them :D those arms are working together to 
grap data from pc and send it via email <br>
`First Arm` : is Key logger that will save your key logs to a file called `log.in` <br>
`Second Arm` : will take photo from your laptop camera and save it in a file called `logg.png` <br>
`Third Arm` : will detect your location using this API freegeoip.net <br>
`Fourth Arm` : will package the last three arms and send them to your email address that you provide <br>

#Working Technique
first thing this is a spying tool so it has to work secretly in the background and run every time the computer is restarting and that is exaclly what `hide()` and `addStartup()`
do so let's start from the beginning : <br>
1. Hpta4Arms will hide itself and added to your start-up apps with the value of true <br>
2. and after that it will open afile called `log.in` and write a `START::` word at the beginning it is a mark for your logs starting<br>
3. it will take a photo and save it to a file called logg.jpg this file will delete himself after it has been sent to the email address<br> 
4. it will detect your location (Lat & lng)--(this might not be accurate because of the API it will detect your first public IP and return it's location)<br>
5. it will send an email to the address you provided<br>
this message will have two files attached the log.in (Logs Text file) and logg.jpg (photo that has been captured from your friend cam)<br>
<img src = "https://github.com/GardiansLab/Hpta4Arms/blob/master/Capture.PNG">

#Install
first you need to install the python packages to help in building your exe files you can plant it in your friend PC so let's go <br>
1. you need to install the packages from the requirements.txt file using this command  (navigate to the tool folder using your CMD)
`pip install requirement.txt` <br>
2. you need to specify the from and to email address to can send the email 
open 'Hpta4Arms.py' and goto line 108 & 109 and change the value to your from and to email addresses
Note :you can use the same email to send the message from the same email.<br>
3. go to line 144 and type your password <br>
4. here im using hotmail so in line 142 iam using smtp.live.comif you are using another email i.e gmail,yahoo,...etc you should provide your correct protocol
`smtplib.SMTP('smtp.live.com', 587)`<br>
5. after that you need to get your exe file to prevent the victim from discovering your email and password if he discover the trick so you have pyinstaller then go to your CMD and run 
`pyinstaller Hpta4Arms.py`<br>
6. two files will be created `dist` and `build` navigate to `dist/Hpta4arms/Hpta4arms.exe` you friend has to run this file to enables you spying on him<br>
7. check the "Plant the tool in your friend PC" section to hide the tool with another software. <br>

#Plant the tool in your friend PC
now you have the exe file if you run it a cmd will open and close in a second (it's not closing it's hiding :D )
so more on hiding the tool without discovering it is to create a batch file that run a specific software and the tool in the same time
,most of people are using chrome so i will create a batch file that will run chrome and Hpta4Arms together so, go ahead and create a file called launch.bat
and paste the code in launch.bat in it . <br>
if your friend is using another software replace third line with the path of your friend's favourite software (make sure it is the exe file)
then go to desktop and right click and create shortcut and add the path to this batch file and rename the file chrome so your friend now will 
open this to start working on chrome and the tool is starting in the background <br>

#Give me more
let's suppose your friend is smart he will figure out that this batch file might be buggy so he avoid running it so now you will convert this batch file to exe file 
doing the same task go to bat2exe folder you will find a file called how_to_run.txt to convert any batch file to exe file 

#Examples
in the examples folder you will find testing for each arm alone feel free to edit them and made a pull request if there isn't anything 
working right with you contact me at ahmedkhaled36@hotmail.com

#If you have any problem 
if you are missing some of the modules you can install it using pip or check out this blog i wrote about installing any module [Here](http://ahmed-khd.blogspot.com.eg/2017/01/how-to-install-python-modules-very-easy.html)

#license
The package is open-sourced software licensed under the [MIT license].