#!/usr/bin/env python
import tf
import rospy
import roslib
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist, TransformStamped
import baxterkitchen.msg
from baxterkitchen.msg import Inventory
#import exp_quat_func as eqf
#import ar_tag_subs as ar


listener = None

ar_tags = {}
ar_tags['knife'] = 'test_frame'
ar_tags['board'] = 'ar_marker_2'
ar_tags['cucumber'] = 'ar_marker_4'
ar_tags['usb_cam'] = 'usb_cam'
ar_tags['naval'] = 'naval'
ar_tags['test_frame'] = 'test_frame'
ar_tags['test_frame2'] = 'test_frame2'



def update_inventory():

    pub = rospy.Publisher('inventory', Inventory, queue_size=10)
    listener = tf.TransformListener()
    r = rospy.Rate(5.0) # 10hz
    
    # initialize the inventory
    imsg = Inventory()
    imsg.knife_translation = (0,0,0)
    imsg.knife_rotation = (0,0,0,0)
    
    
    
    while not rospy.is_shutdown():
        print '==================='
        message = Inventory()
        try:
            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['knife'], rospy.Time(0))
            message.knife_translation = trans1
            message.knife_rotation = rot1
            message.knife_seen = True
            print 'published knife'
           # (trans2, rot2) = listener.lookupTransform(ar_tags['cucumber'], ar_tags['naval'], rospy.Time(0))
           # message.cucumber_translation = trans2
           # message.cucumber_rotation = rot2
          #  message.cucumber_seen = True
        except tf.LookupException or tf.ExtrapolationException or rospy.ServiceException as e:
            print e

        pub.publish(message)

        r.sleep()
  
  
if __name__=='__main__':
    rospy.init_node('object_identifier')
    update_inventory()
    rospy.spin()
