#!/usr/bin/env python
import tf
import rospy
import roslib
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Quaternion, Twist, TransformStamped
import baxterkitchen.msg
from baxterkitchen.msg import Inventory
#import exp_quat_func as eqf
#import ar_tag_subs as ar


listener = None

ar_tags = {}

ar_tags['knife'] =    'ar_marker_2'  # slave 0 and 1
ar_tags['corn'] =     'ar_marker_5'  # slave 3 and 4
ar_tags['carrot'] =   'ar_marker_8'  # slave 7 and 6
ar_tags['dish'] =     'ar_marker_19' # slave 12 and 13
ar_tags['sponge'] =   'ar_marker_11' # slave 9 and 10
ar_tags['rack'] =     'ar_marker_18' # slave 14
ar_tags['usb_cam'] =  'usb_cam'
ar_tags['naval'] =    'ar_marker_16' # slave 15 and 17

def sub_callback(data):
    print 'sub received data'
    #print data


def update_inventory():

    pub = rospy.Publisher('inventory', Inventory, queue_size=10)
    #sub = rospy.Subscriber('inventory', Inventory, sub_callback, queue_size=10)
    listener = tf.TransformListener()
    r = rospy.Rate(2.0) # 10hz
    

    
    while not rospy.is_shutdown():
        #print '==================='
        m = Inventory()
        try:
            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['knife'], rospy.Time(0))
            m.knife_px = trans1[0]; m.knife_py = trans1[1]; m.knife_pz = trans1[2]; m.knife_ox = rot1[0]; m.knife_oy = rot1[1]; m.knife_oz = rot1[2]; m.knife_ow = rot1[3]; m.knife_seen = True

            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['carrot'], rospy.Time(0))
            m.carrot_px = trans1[0]; m.carrot_py = trans1[1]; m.carrot_pz = trans1[2]; m.carrot_ox = rot1[0]; m.carrot_oy = rot1[1]; m.carrot_oz = rot1[2]; m.carrot_ow = rot1[3]; m.carrot_seen = True
            
            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['corn'], rospy.Time(0))
            m.corn_px = trans1[0]; m.corn_py = trans1[1]; m.corn_pz = trans1[2]; m.corn_ox = rot1[0]; m.corn_oy = rot1[1]; m.corn_oz = rot1[2]; m.corn_ow = rot1[3]; m.corn_seen = True
            
            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['dish'], rospy.Time(0))
            m.dish_px = trans1[0]; m.dish_py = trans1[1]; m.dish_pz = trans1[2]; m.dish_ox = rot1[0]; m.dish_oy = rot1[1]; m.dish_oz = rot1[2]; m.dish_ow = rot1[3]; m.dish_seen = True

            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['sponge'], rospy.Time(0))
            m.sponge_px = trans1[0]; m.sponge_py = trans1[1]; m.sponge_pz = trans1[2]; m.sponge_ox = rot1[0]; m.sponge_oy = rot1[1]; m.sponge_oz = rot1[2]; m.sponge_ow = rot1[3]; m.sponge_seen = True

            (trans1, rot1) = listener.lookupTransform(ar_tags['naval'], ar_tags['rack'], rospy.Time(0))
            m.rack_px = trans1[0]; m.rack_py = trans1[1]; m.rack_pz = trans1[2]; m.rack_ox = rot1[0]; m.rack_oy = rot1[1]; m.rack_oz = rot1[2]; m.rack_ow = rot1[3]; m.rack_seen = True
            
                              
            
        except tf.LookupException or tf.ExtrapolationException or rospy.ServiceException as e:
            print e

        pub.publish(message)

        r.sleep()
  
  
if __name__=='__main__':
    rospy.init_node('object_identifier')
    update_inventory()
    rospy.spin()
