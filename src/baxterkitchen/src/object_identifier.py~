#! /usr/bin/env python

import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import baxterkitchen.msg

def pick_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (PickAction) to the constructor.
    client = actionlib.SimpleActionClient('pick_server', baxterkitchen.msg.PickAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = baxterkitchen.msg.PickGoal(p_x = 0.123, p_y = 0.234, p_z = 0.345)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A PickResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('motion_org')
        result = pick_client()
        print "Result from client:", result
    except rospy.ROSInterruptException:
        print "program interrupted before completion"

