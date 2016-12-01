#! /usr/bin/env python

import roslib
import sys
import rospy
import moveit_commander
from moveit_msgs.msg import OrientationConstraint, Constraints
from geometry_msgs.msg import PoseStamped
from baxter_interface import gripper as baxter_gripper
from moveit_python import *

# Brings in the SimpleActionClient
import actionlib

# goal message and the result message.

def pick_client(si, px, py, pz):
    client = actionlib.SimpleActionClient('pick_server', baxterkitchen.msg.PickAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.PickGoal(side = si, p_x = px, p_y = py, p_z = pz)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()


if __name__ == '__main__':
	# moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node("moveit_py")
	# scene = moveit_commander.planning_scene_interface.PlanningSceneInterface()
	# scene.remove_world_object("cube1")
	# goal_1 = PoseStamped()
	# goal_1.pose.position.x = 0.4
	# goal_1.pose.position.y = 0.0
	# goal_1.pose.position.z = 0.0

	# #Orientation as a quaternion
	# goal_1.pose.orientation.x = 0.0
	# goal_1.pose.orientation.y = -1.0
	# goal_1.pose.orientation.z = 0.0
	# goal_1.pose.orientation.w = 0.0
	# scene.add_box("cube3",goal_1)
	print("here")
	p = PlanningSceneInterface("base")
	p.addCube("cube1", 0.1, 2, 0, 0.5)
	p.addCube("cube2", 0.1, 2, 2, 0.5)



