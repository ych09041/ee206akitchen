#! /usr/bin/env python

import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

# goal message and the result message.
import baxterkitchen.msg
from baxterkitchen.msg import Inventory
from baxter_interface import gripper as baxter_gripper

from moveit_python import *


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



class OrganizeAction(object):
    rospy.init_node('motion_organizer')

    # create messages that are used to publish feedback/result
    _feedback = baxterkitchen.msg.OrganizeFeedback()
    _result   = baxterkitchen.msg.OrganizeResult()
    #Set up the grippers
    left_gripper = baxter_gripper.Gripper('left')
    right_gripper = baxter_gripper.Gripper('right')
    #Calibrate the grippers (other commands won't work unless you do this first)
    print('Calibrating...')
    left_gripper.calibrate()
    right_gripper.calibrate()
    # Set the force limit on the grippers
    force_limit = 60 # approx 10N: 100 = 30N
    left_gripper.set_moving_force(force_limit)
    right_gripper.set_moving_force(force_limit)
    left_gripper.set_holding_force(force_limit)
    right_gripper.set_holding_force(force_limit)
    # setup scene
    #p = PlanningSceneInterface("base")
    #p.addbox("name",lx,ly,lz,px,py,pz)
    #p.clear()
    
    rospy.sleep(1.0)


    def __init__(self, name):
        self._action_name = name
        # add table to scene
        self._as = actionlib.SimpleActionServer(self._action_name, baxterkitchen.msg.OrganizeAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
        result = pick_client(0,0.85,0.25,0)
        result = pick_client(1,0.85,-0.25,0)
        while True:
            rospy.sleep(1)
    
    def execute_cb(self, goal): ###################### do action in this execute_cb
        # helper variables
        r = rospy.Rate(1)
        success = True

     



        #####################################################################################





        # check that preempt has not been requested by the client
        if self._as.is_preempt_requested():
            rospy.loginfo('%s: Preempted' % self._action_name)
            self._as.set_preempted()
            success = False


        # publish the feedback
        self._as.publish_feedback(self._feedback)
        # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
        r.sleep()
          
        if success:
            self._result.done = success
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)



if __name__ == '__main__':
    OrganizeAction(rospy.get_name())
    rospy.spin()

