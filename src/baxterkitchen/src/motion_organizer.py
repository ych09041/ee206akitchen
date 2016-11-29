#! /usr/bin/env python

import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import baxterkitchen.msg
from baxter_interface import gripper as baxter_gripper

def pick_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (PickAction) to the constructor.
    client = actionlib.SimpleActionClient('pick_server', baxterkitchen.msg.PickAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = baxterkitchen.msg.PickGoal(side = 0, p_x = 0.4, p_y = 0.0, p_z = 0.0)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A PickResult

def place_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (PickAction) to the constructor.
    client = actionlib.SimpleActionClient('place_server', baxterkitchen.msg.PlaceAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = baxterkitchen.msg.PlaceGoal(side = 0, p_x = 0.4, p_y = 0.0, p_z = 0.2) # side: 0 - left; 1- right

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A PlaceResult

def move_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (PickAction) to the constructor.
    client = actionlib.SimpleActionClient('move_server', baxterkitchen.msg.MoveAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = baxterkitchen.msg.MoveGoal(side = 0, p_x = 0.2, p_y = 0.0, p_z = 0.0) # side: 0 - left; 1- right

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A PlaceResult

def scrub_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (PickAction) to the constructor.
    client = actionlib.SimpleActionClient('scrub_server', baxterkitchen.msg.ScrubAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = baxterkitchen.msg.ScrubGoal(p_x = 0.6, p_y = 0.0, p_z = 0.0) # side: 0 - left; 1- right

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A PlaceResult

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
        result = pick_client()
        result = move_client()
        result = scrub_client()
        result = place_client()
        print "Result from client:", result
    except rospy.ROSInterruptException:
        print "program interrupted before completion"

