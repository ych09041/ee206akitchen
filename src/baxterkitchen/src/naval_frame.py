#!/usr/bin/env python  
import roslib

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('my_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(2.0)
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 1.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         'usb_cam',
                         'naval')
        rate.sleep()
