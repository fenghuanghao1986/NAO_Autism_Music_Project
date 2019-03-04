# Get an image from NAO. Display it and save it using PIL.
import sys
import time
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from naoqi import ALProxy


def capture_image(IP, PORT):

  # First get an image from Nao, then show it on the screen with PIL.
  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  camera = 1  # 1 = bottom camera
  resolution = 2    # 2 = VGA, 3 = hd
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribeCamera("python_client",camera, resolution, colorSpace, 5)

  # Get a camera image.
  naoImage = camProxy.getImageRemote(videoClient)


  camProxy.unsubscribe(videoClient)

  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # Get the image size and pixel array.

  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]       # image[6] contains the image data passed as an array of ASCII chars.

  # Create a PIL Image from our pixel array and save it as colored.png
  im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
  im.save("colored.png", "PNG")


# while(1):
#     capture_image("192.168.0.105", 9559)
#
#     img = cv2.imread('colored.png')
#
#     cv2.imshow('flow', img)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#       break
