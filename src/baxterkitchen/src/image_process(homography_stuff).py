#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from lab4_cam.srv import ImageSrv, ImageSrvResponse
import cv2, time, sys
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from numpy.linalg import *
import math


# Nominal length of a tile side
TILE_LENGTH = 30.48 #cm

# Helper function to check computed homography
# This will draw dots in a grid by projecting x,y coordinates
# of tile corners to u,v image coordinates
def check_homography(image, H, nx, ny, length=TILE_LENGTH):
  # H should be a 3x3 numpy.array
  # nx is the number of tiles in the x direction
  # ny is the number of tiles in the y direction
  # length is the length of one side of a tile
  # image is an image array
  for i in range(nx+1):
    for j in range(ny+1):
      xbar = np.array([[i*length],[j*length],[1]])
      ubar = np.dot(H,xbar).T[0]
      u = np.int(ubar[0]/ubar[2])
      v = np.int(ubar[1]/ubar[2])
      print 'Dot location: ' + str((u,v))
      cv2.circle(image, (u,v), 5, 0, -1)
  cv2.imshow('Check Homography', image)

# Create a CvBridge to convert ROS messages to OpenCV images
bridge = CvBridge()

# Converts a ROS Image message to a NumPy array to be displayed by OpenCV
def ros_to_np_img(ros_img_msg):
  return np.array(bridge.imgmsg_to_cv2(ros_img_msg,'bgr8'))

# Define the total number of clicks we are expecting (4 corners)
TOT_CLICKS = 4

if __name__ == '__main__':
  
  # Waits for the image service to become available
  rospy.wait_for_service('last_image')
  
  # Initializes the image processing node
  rospy.init_node('image_processing_node')
  
  # Creates a function used to call the 
  # image capture service: ImageSrv is the service type
  last_image_service = rospy.ServiceProxy('last_image', ImageSrv)

  # Create an empty list to hold the coordinates of the clicked points
  points = []

  # Callback function for 'cv2.SetMouseCallback' adds a clicked point to the
  # list 'points'
  def on_mouse_click(event,x,y,flag,param):
    if(event == cv2.EVENT_LBUTTONUP):
      point = (x,y)
      print "Point Captured: " + str(point)
      points.append(point)

  while not rospy.is_shutdown():
    try:
      # Waits for a key input to continue
      raw_input('Press enter to capture an image:')
    except KeyboardInterrupt:
      print 'Break from raw_input'
      break
    
    try:
      # Request the last image from the image service
      # And extract the ROS Image from the ImageSrv service
      # Remember that ImageSrv.image_data was
      # defined to be of type sensor_msgs.msg.Image
      ros_img_msg = last_image_service().image_data

      # Convert the ROS message to a NumPy image
      np_image = ros_to_np_img(ros_img_msg)

      # Display the CV Image
      cv2.imshow("CV Image", np_image)

      # Tell OpenCV that it should call 'on_mouse_click' when the user
      # clicks the window. This will add clicked points to our list
      cv2.setMouseCallback("CV Image", on_mouse_click, param=1)

      # Zero out list each time we have a new image
      points = []

      # Loop until the user has clicked enough points
      while len(points) < TOT_CLICKS+2:
        if rospy.is_shutdown():
          raise KeyboardInterrupt
        cv2.waitKey(10)

      # Convert the Python list of points to a NumPy array of the form
      #   | u1 u2 u3 u4 |
      #   | v1 v2 v3 v4 |
      uv = np.array(points).T

# === YOUR CODE HERE ===========================================================
      
      # This is placeholder code that will draw a 4 by 3 grid in the corner of
      # the image
      nx = 4
      ny = 3
      H = np.eye(3)
      b = np.zeros((8,1))
      b[0] = uv[0,0]
      b[1] = uv[1,0]
      b[2] = uv[0,1]
      b[3] = uv[1,1]
      b[4] = uv[0,2]
      b[5] = uv[1,2]
      b[6] = uv[0,3]
      b[7] = uv[1,3]
      x1 = 0
      y1 = 0
      x2 = 0
      y2 = TILE_LENGTH*3
      x3 = TILE_LENGTH*3
      y3 = TILE_LENGTH*3
      x4 = TILE_LENGTH*3
      y4 = 0
      xy = np.array([[x1, x2, x3, x4],[y1, y2, y3, y4]])
      A = np.zeros((8,8))
      for i in range(0,4):
          A[2*i:2*i+2,:] = np.array([[xy[0,i],xy[1,i],1,0,0,0,-uv[0,i]*xy[0,i],-uv[0,i]*xy[1,i]],
                                [0,0,0,xy[0,i],xy[1,i],1,-uv[1,i]*xy[0,i],-uv[1,i]*xy[1,i]]])
      print A.shape
      print b.shape
      Hel = np.linalg.solve(A,b)
      print 'printing Hel'
      print Hel.shape
      H[0,0] = Hel[0]
      H[0,1] = Hel[1]
      H[0,2] = Hel[2]
      H[1,0] = Hel[3]
      H[1,1] = Hel[4]
      H[1,2] = Hel[5]
      H[2,0] = Hel[6]
      H[2,1] = Hel[7]
      H[2,2] = 1
      Q = np.linalg.inv(H)
      mu1 = uv[0,4]
      mv1 = uv[1,4]
      mu2 = uv[0,5]
      mv2 = uv[1,5]
      mx1 = (Q[0,0] * mu1 + Q[0,1] * mv1 + Q[0,2])/(Q[2,0] * mu1 + Q[2,1] * mv1 + Q[2,2])
      my1 = (Q[1,0] * mu1 + Q[1,1] * mv1 + Q[1,2])/(Q[2,0] * mu1 + Q[2,1] * mv1 + Q[2,2])
      mx2 = (Q[0,0] * mu2 + Q[0,1] * mv2 + Q[0,2])/(Q[2,0] * mu2 + Q[2,1] * mv2 + Q[2,2])
      my2 = (Q[1,0] * mu2 + Q[1,1] * mv2 + Q[1,2])/(Q[2,0] * mu2 + Q[2,1] * mv2 + Q[2,2])
      dist = math.sqrt((mx1 - mx2)**2+(my1 - my2)**2)
      print 'The distance between clicked point is '
      print dist
      



# ==============================================================================
      
      # Check the produced homography matrix
      check_homography(np_image, H, nx, ny)

      # Loop until the user presses a key
      key = -1
      while key == -1:
        if rospy.is_shutdown():
          raise KeyboardInterrupt
        key = cv2.waitKey(100)
      
      # When done, get rid of windows and start over
      # cv2.destroyAllWindows()

    except KeyboardInterrupt:
      print 'Keyboard Interrupt, exiting'
      break

    # Catch if anything went wrong with the Image Service
    except rospy.ServiceException, e:
      print "image_process: Service call failed: %s"%e
    
  cv2.destroyAllWindows()

