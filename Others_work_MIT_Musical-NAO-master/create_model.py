import numpy as np
import cv2
import numpy as np
import imutils
import cv2
import math
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import time
from PIL import Image
import json
import glob
import almath


def stiffness_on(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def get_image(IP, PORT):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    camera = 1  # 1 = bottom camera , 0 = top camera
    resolution = 2  # 2 = VGA
    colorSpace = 11  # RGB

    videoClient = camProxy.subscribeCamera("python_client", camera, resolution, colorSpace, 5)

    t0 = time.time()

    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = camProxy.getImageRemote(videoClient)

    t1 = time.time()

    # Time the image transfer.
    print "acquisition delay ", t1 - t0

    camProxy.unsubscribe(videoClient)

    # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]


    # Create a PIL Image from our pixel array.
    im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
    im.save("model_image.png", "PNG")


def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global count
        count = count + 1
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        cv2.putText(img, str(count), (x,y), font, 0.6, (255, 50, 0), 1, cv2.LINE_AA)
        points.append([x,y])

##########################################################
###################### "MAIN"  ###########################
##########################################################

with open('config.txt') as data_file:
    data = json.loads(data_file.read())

robotIP = str(data["robotIP"])  # Change robotIP with the robot's IP
PORT = int(data["PORT"])  # Change PORT with the robot's PORT

tts = ALProxy("ALTextToSpeech", robotIP, PORT)
motionProxy = ALProxy("ALMotion", robotIP, PORT)
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

stiffness_on(motionProxy)
postureProxy.goToPosture("StandInit", 0.5)
time.sleep(2.0)

points = []
# mouse callback function
font = cv2.FONT_HERSHEY_SIMPLEX

count = 0
# Create a black image, a window and bind the function to window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
#
tts.say("Move the metallophone until both red keys are completely visible")

while(1):
    get_image(robotIP, PORT)
    # Create a PIL Image from our pixel array.
    img = cv2.imread('model_image.png')  # queryImage
    cv2.imshow('image', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
      break

tts.say("Alright! Now move the mouse and double click to mark the points")

img = cv2.imread('model_image.png')  # queryImage
im = cv2.imread('model_image.png')
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

file = open('model_points.txt', 'w')
file.write(str(points))
file.close()
print points

size = img.shape

# Image Processsing
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
filtered = cv2.GaussianBlur(gray, (3, 3), 0)
v = np.median(filtered)
# apply automatic Canny edge detection using the computed median
lower = int(max(0, (1.0 - 0.33) * v))
upper = int(min(255, (1.0 + 0.33) * v))
edges = cv2.Canny(filtered, lower, upper)
im = cv2.dilate(edges, None, iterations=1)


# Clean up some information (remove the base)
# find the lowest point on the image that contains usefull information (the metallophone)
lowest_y = 0
for i in points:
    print i[1]
    if i[1] >  lowest_y:
        lowest_y = i[1]

cv2.rectangle(im, (0, lowest_y+15), (639, 479), (0, 0, 0), -1)


cv2.imwrite("model_image.png", im)

tts.say("Perfect! See you later.")
motionProxy.rest()