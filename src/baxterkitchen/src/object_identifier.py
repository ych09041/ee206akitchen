#!/usr/bin/env python
import tf
import rospy
import roslib
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist, TransformStamped
#import exp_quat_func as eqf
#import ar_tag_subs as ar
#import timeit


listener = None

def follow_ar_tag(zumy, ar_tags):
    """
    This function should obtain the rigid body transform between the Zumy and the AR ar_tag
    Then compute and send the twist required to drive the Zumy to the AR ar_tag
    """
    # YOUR CODE HERE


    topic_name = zumy+'/cmd_vel'
    pub = rospy.Publisher(topic_name, Twist, queue_size=10)
    listener = tf.TransformListener()
    r = rospy.Rate(10.0) # 10hz
    start = timeit.timeit()
    
    while not rospy.is_shutdown():
        print '==================='
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))

            rbt = ar.return_rbt(trans=trans, rot=rot)
            (v,w) = ar.compute_twist(rbt=rbt)
            thing = Transform()
            thing.translation.x = trans[0]
            thing.translation.y = trans[1]
            thing.translation.z = trans[2]
            
            thing.rotation.x = rot[0]
            thing.rotation.y = rot[1]
            thing.rotation.z = rot[2]
            thing.rotation.w = rot[3]

            handle = rospy.ServiceProxy('innovation', NuSrv)
            resp1 = handle(thing,'usb_cam')

            r.sleep()
        except tf.LookupException or rospy.ServiceException as e:
            print e
  
if __name__=='__main__':
    rospy.init_node('follow_ar_tag')
    ar_tags = {}
    zumy_name = sys.argv[1]
    ar_tags['ar1'] = 'ar_marker_' + sys.argv[2]
   # ar_tags['arZ'] = 'ar_marker_' + sys.argv[3]
    ar_tags['arZ'] = 'usb_cam'

    follow_ar_tag(zumy=zumy_name, ar_tags=ar_tags)
    rospy.spin()
