#! /usr/bin/env python

import roslib
import rospy
from moveit_python import *

# Brings in the SimpleActionClient
import actionlib

# goal message and the result message.
import baxterkitchen.msg
from baxterkitchen.msg import Inventory
from baxter_interface import gripper as baxter_gripper

def pick_client(si, px, py, pz):
    client = actionlib.SimpleActionClient('pick_server', baxterkitchen.msg.PickAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.PickGoal(side = si, p_x = px, p_y = py, p_z = pz)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()


if __name__ == '__main__':
    rospy.init_node("add_box")
    print("here")
    p = PlanningSceneInterface("base")
    p.clear()
    p.addBox("tall", .1,.3,1.5, .4, .6, 0)
    # p.addCube("cube4", 0.1, 1, -2, 0.5)


