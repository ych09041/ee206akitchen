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
#import exp_quat_func as eqf
#import ar_tag_subs as ar


listener = None

ar_tags = {}
ar_tags['knife'] = 'ar_marker_12'
ar_tags['board'] = 'ar_marker_2'
ar_tags['cucumber'] = 'ar_marker_4'
ar_tags['eye'] = 'usb_cam'
ar_tags['naval'] = 'naval'




def update_inventory(ar_tags):

    pub = rospy.Publisher('inventory', Inventory, queue_size=10)
    listener = tf.TransformListener()
    r = rospy.Rate(5.0) # 10hz
    
    while not rospy.is_shutdown():
        print '==================='
        message = Inventory()
        
        (trans1, rot1) = listener.lookupTransform(ar_tags['knife'], ar_tags['naval'], rospy.Time(0))
        message.knife_translation = trans1
        message.knife_rotation = rot1
        message.knife_seen = True
        
        (trans2, rot2) = listener.lookupTransform(ar_tags['cucumber'], ar_tags['naval'], rospy.Time(0))
        message.cucumber_translation = trans2
        message.cucumber_rotation = rot2
        message.cucumber_seen = True
        

        pub.publish(message)

        r.sleep()
  
  
if __name__=='__main__':
    rospy.init_node('object_identifier')
    update_inventory()
    rospy.spin()
