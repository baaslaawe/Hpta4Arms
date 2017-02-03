import time
import cv2

camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.5)  # If you don't wait, the image will be dark
image = camera.read()[1]
cv2.imwrite("opencv.png", image)
del(camera)  # so that others can use the camera as soon as possible