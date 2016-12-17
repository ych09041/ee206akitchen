#!/usr/bin/env python  

'''
UC Berkeley EE 206A Fall 2016
Baxter Kitchen Assistant
Tony Abdo, Xiaotian Fan, Cheng Hao Yuan

'''

import roslib

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('my_tf_broadcaster')
    br = tf.TransformBroadcaster()
    br_test = tf.TransformBroadcaster()
    br_test2 = tf.TransformBroadcaster()
    rate = rospy.Rate(2.0)
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         'base',
                         'naval')
        rate.sleep()
