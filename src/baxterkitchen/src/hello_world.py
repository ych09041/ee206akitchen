#!/usr/bin/env python


#Import the dependencies as described in example_pub.py
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState

import numpy as np
import scipy as sp
from scipy import linalg


def callback(m):
# parse the message to get joint angles
# plug into FK to compute
    print m



#Define the method which contains the node's main functionality
def hello():

    rospy.init_node('hello_world', anonymous=True)

    pub = rospy.Publisher("alive", String)
    rospy.Subscriber("alive", String, callback)
    r = rospy.Rate(1)


    while not rospy.is_shutdown():
        # Construct a string that we want to publish
        pub_string = "hello world %s" % (rospy.get_time())

        # Publish our string to the 'chatter_talk' topic
        pub.publish(pub_string)

        # Use our rate object to sleep until it is time to publish again
        r.sleep()


#Python's syntax for a main() method
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method
  try:
    hello()
  except rospy.ROSInterruptException: pass
