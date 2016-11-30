#!/usr/bin/env python  
import roslib

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('my_tf_broadcaster')
    br = tf.TransformBroadcaster()
    br_test = tf.TransformBroadcaster()
    br_test2 = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 1.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         'usb_cam',
                         'naval')
        br_test.sendTransform((3.4, 1.2, 1.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         'test_frame',
                         'naval')
        br_test2.sendTransform((2.0, 1.0, 1.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         'test_frame2',
                         'naval')
        rate.sleep()
