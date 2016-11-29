#! /usr/bin/env python

import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

# goal message and the result message.
import baxterkitchen.msg
from baxter_interface import gripper as baxter_gripper

def pick_client():
    client = actionlib.SimpleActionClient('pick_server', baxterkitchen.msg.PickAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.PickGoal(side = 0, p_x = 0.4, p_y = 0.0, p_z = 0.0)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def place_client():
    client = actionlib.SimpleActionClient('place_server', baxterkitchen.msg.PlaceAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.PlaceGoal(side = 0, p_x = 0.4, p_y = 0.0, p_z = 0.2) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def move_client():
    client = actionlib.SimpleActionClient('move_server', baxterkitchen.msg.MoveAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.MoveGoal(side = 0, p_x = 0.4, p_y = 0.2, p_z = 0.0) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def scrub_client():
    client = actionlib.SimpleActionClient('scrub_server', baxterkitchen.msg.ScrubAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.ScrubGoal(p_x = 0.3, p_y = 0.3, p_z = 0.0) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('motion_org')

        #Set up the grippers
        left_gripper = baxter_gripper.Gripper('left')
        right_gripper = baxter_gripper.Gripper('right')
        #Calibrate the grippers (other commands won't work unless you do this first)
        print('Calibrating...')
        left_gripper.calibrate()
        right_gripper.calibrate()
        rospy.sleep(2.0)

        #############testing!!!!!!#############
        #left_gripper.close(block=True)
        rospy.sleep(1.0)
        #############testing!!!!!!#############
      #  result = pick_client()
      #  result = move_client()
        result = scrub_client()
      #  result = place_client()
        print "Result from client:", result
    except rospy.ROSInterruptException:
        print "program interrupted before completion"

