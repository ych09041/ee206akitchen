#! /usr/bin/env python

import roslib
import rospy

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

def place_client(si, px, py, pz):
    client = actionlib.SimpleActionClient('place_server', baxterkitchen.msg.PlaceAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.PlaceGoal(side = si, p_x = px, p_y = py, p_z = pz) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def move_client(si, px, py, pz):
    client = actionlib.SimpleActionClient('move_server', baxterkitchen.msg.MoveAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.MoveGoal(side = si, p_x = px, p_y = py, p_z = pz) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def scrub_client(px, py, pz):
    client = actionlib.SimpleActionClient('scrub_server', baxterkitchen.msg.ScrubAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.ScrubGoal(p_x = px, p_y = py, p_z = pz) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

def cut_client(px, py, pz):
    client = actionlib.SimpleActionClient('cut_server', baxterkitchen.msg.CutAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.CutGoal(p_x = px, p_y = py, p_z = pz) # side: 0 - left; 1- right
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

# global variables for motion organizer to use
knife_px = 0.0
knife_py = 0.0
knife_pz = 0.0
knife_ox = 0.0
knife_oy = 0.0
knife_oz = 0.0
knife_ow = 0.0

def sub_callback(data):
    global knife_px, knife_py, knife_pz, knife_ox, knife_oy, knife_oz, knife_ow
    knife_px = data.knife_px
    knife_py = data.knife_py
    knife_pz = data.knife_pz
    knife_ox = data.knife_ox
    knife_oy = data.knife_oy
    knife_oz = data.knife_oz
    knife_ow = data.knife_ow




if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('motion_org')
        sub = rospy.Subscriber('inventory', Inventory, sub_callback, queue_size=10)
        
        #Set up the grippers
        left_gripper = baxter_gripper.Gripper('left')
        right_gripper = baxter_gripper.Gripper('right')
        #Calibrate the grippers (other commands won't work unless you do this first)
        print('Calibrating...')
        left_gripper.calibrate()
        right_gripper.calibrate()
        rospy.sleep(1.0)

        #############testing!!!!!!#############
        #left_gripper.close(block=True)
        #rospy.sleep(1.0)
        #############testing!!!!!!#############
        print "pick"
        result = pick_client(0, 0.4, 0.0, 0.0)
        #print 'pick knife'
        #print knife_px
        #print knife_py
        #print knife_pz
        #result = pick_client(0, knife_px, knife_py, knife_pz)
        print "move1"
        result = move_client(0, 0.4, 0.0, 0.1)
        print "scrub"
        result = scrub_client(0.4, 0.0, 0.1) # scrub should follow "move" with same input for complete performance/accuracy
        print "move2"
        result = move_client(0, 0.3, 0.1, 0.1)
        print "cut"
        result = cut_client(0.3, 0.1, 0.1) # cut should follow "move" with same input for complete performance/accuracy
        print "place"
        result = place_client(0, 0.3, 0.5, 0.0)
        print "Result from client:", result
    except rospy.ROSInterruptException:
        print "program interrupted before completion"

