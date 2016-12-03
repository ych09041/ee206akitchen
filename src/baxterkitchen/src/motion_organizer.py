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

objectSize = {}

objectSize['knife'] =    (.3,.095,.095)  # slave 0 and 1
objectSize['carrot'] =   (2,2,2)  # slave 3 and 4
objectSize['cucumber'] = (2,2,2)  # slave 7 and 8
objectSize['dish'] =     (2,2,2)  # slave 10 and 11
objectSize['sponge'] =   (2,2,2) # slave 13 and 14

objectOffset = {}
objectOffset['knife'] = (objectSize['knife'][0]/2 + .03, 0, objectSize['knife'][2]/2)


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
knife_px = 0.0; knife_py = 0.0; knife_pz = 0.0; knife_ox = 0.0; knife_oy = 0.0; knife_oz = 0.0; knife_ow = 0.0; knife_seen = False
carrot_px = 0.0; carrot_py = 0.0; carrot_pz = 0.0; carrot_ox = 0.0; carrot_oy = 0.0; carrot_oz = 0.0; carrot_ow = 0.0; carrot_seen = False
cucumber_px = 0.0; cucumber_py = 0.0; cucumber_pz = 0.0; cucumber_ox = 0.0; cucumber_oy = 0.0; cucumber_oz = 0.0; cucumber_ow = 0.0; cucumber_seen = False
dish_px = 0.0; dish_py = 0.0; dish_pz = 0.0; dish_ox = 0.0; dish_oy = 0.0; dish_oz = 0.0; dish_ow = 0.0; dish_seen = False
sponge_px = 0.0; sponge_py = 0.0; sponge_pz = 0.0; sponge_ox = 0.0; sponge_oy = 0.0; sponge_oz = 0.0; sponge_ow = 0.0; sponge_seen = False



def sub_callback(data):
    global knife_px, knife_py, knife_pz, knife_ox, knife_oy, knife_oz, knife_ow, knife_seen, \
        carrot_px, carrot_py, carrot_pz, carrot_ox, carrot_oy, carrot_oz, carrot_ow, carrot_seen, \
        cucumber_px, cucumber_py, cucumber_pz, cucumber_ox, cucumber_oy, cucumber_oz, cucumber_ow, cucumber_seen, \
        dish_px, dish_py, dish_pz, dish_ox, dish_oy, dish_oz, dish_ow, dish_seen, \
        sponge_px, sponge_py, sponge_pz, sponge_ox, sponge_oy, sponge_oz, sponge_ow, sponge_seen
    knife_px = data.knife_px; knife_py = data.knife_py; knife_pz = data.knife_pz; knife_ox = data.knife_ox; knife_oy = data.knife_oy; knife_oz = data.knife_oz; knife_ow = data.knife_ow; knife_seen = data.knife_seen
    carrot_px = data.carrot_px; carrot_py = data.carrot_py; carrot_pz = data.carrot_pz; carrot_ox = data.carrot_ox; carrot_oy = data.carrot_oy; carrot_oz = data.carrot_oz; carrot_ow = data.carrot_ow; carrot_seen = data.carrot_seen
    cucumber_px = data.cucumber_px; cucumber_py = data.cucumber_py; cucumber_pz = data.cucumber_pz; cucumber_ox = data.cucumber_ox; cucumber_oy = data.cucumber_oy; cucumber_oz = data.cucumber_oz; cucumber_ow = data.cucumber_ow; cucumber_seen = data.cucumber_seen
    dish_px = data.dish_px; dish_py = data.dish_py; dish_pz = data.dish_pz; dish_ox = data.dish_ox; dish_oy = data.dish_oy; dish_oz = data.dish_oz; dish_ow = data.dish_ow; dish_seen = data.dish_seen
    sponge_px = data.sponge_px; sponge_py = data.sponge_py; sponge_pz = data.sponge_pz; sponge_ox = data.sponge_ox; sponge_oy = data.sponge_oy; sponge_oz = data.sponge_oz; sponge_ow = data.sponge_ow; sponge_seen = data.sponge_seen
    print 'inventory_updated'


class OrganizeAction(object):
    rospy.init_node('motion_organizer')

    # create messages that are used to publish feedback/result
    _feedback = baxterkitchen.msg.OrganizeFeedback()
    _result   = baxterkitchen.msg.OrganizeResult()
    sub = rospy.Subscriber('inventory', Inventory, sub_callback, queue_size=10)
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
    p = PlanningSceneInterface("base")
    #p.addbox("name",lx,ly,lz,px,py,pz)
    #p.clear()
    
    rospy.sleep(1.0)


    def __init__(self, name):
        self._action_name = name
        self.p.addBox("knife",objectSize['knife'][0],objectSize['knife'][1],objectSize['knife'][2],
            knife_px+objectOffset['knife'][0],knife_py+objectOffset['knife'][1],knife_pz+objectOffset['knife'][2])
        self._as = actionlib.SimpleActionServer(self._action_name, baxterkitchen.msg.OrganizeAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
    
    def execute_cb(self, goal): ###################### do action in this execute_cb
        # helper variables
        r = rospy.Rate(1)
        success = True

        ##################################################################################
        print 'motion org received request'
        print goal.chore
        print goal.target
        print goal.reps

        if goal.chore == 'wash': ########### wash execution
            print 'washing...'
            try:       
                print 'pick sponge'
                result = pick_client(0, sponge_px, sponge_py, sponge_pz)
                #p.removeCollisionObject("tall")
                print 'move sponge'
                result = move_client(0, 0.4, 0.3, 0.0)
                for times in range(0,goal.reps):
                    print 'pick dish ', times
                    result = pick_client(1, dish_px, dish_py, dish_pz)
                    #p.removeCollisionObject("tall")
                    print 'move dish ', times
                    result = move_client(1, 0.4, 0.6, 0.0)
                    print 'scrub the dish...'
                    result = scrub_client(0.0, 0.0, 0.0) # position input doesnt matter...
                    print "return dish ", times
                    result = place_client(1, 0.3, 0.1, 0.1)
                    #p.addbox("name",lx,ly,lz,px,py,pz)
                print 'return sponge'
                result = place_client(0, 0.6, 0.4, 0.0)
                #p.addbox("name",lx,ly,lz,px,py,pz)
                print "Finished washing: ", result
            except rospy.ROSInterruptException:
                print "program interrupted before completion"

        if goal.chore == 'cut': ############ cut execution
            print 'cutting...'
            try:       
                print 'pick knife'
                result = pick_client(0, knife_px, knife_py, knife_pz)
                self.p.removeCollisionObject('knife')

                # result = pick_client(0, 0.4, 0.5, 0.0)
                #p.removeCollisionObject("tall")
                print 'move knife'
                result = move_client(0, 0.4, 0.3, 0.0)
                print 'pick ', goal.target
                if goal.target == 'carrot':
                    print 'cut carrot'
                    #result = pick_client(1, carrot_px, carrot_py, carrot_pz)
                    # result = pick_client(1, 0.4, -0.3, 0.0)
                    #p.removeCollisionObject("tall")
                else:
                    print 'cut cucumber'
                    # result = pick_client(1, cucumber_px, cucumber_py, cucumber_pz)
                    #p.removeCollisionObject("tall")                    
                print 'move ', goal.target
                # result = move_client(1, 0.3, -0.4, 0.0)
                print 'cut...'
                result = cut_client(0.0, 0.0, 0.0) # position input doesnt matter...
                print 'return ', goal.target
                # result = place_client(1, 0.3, -0.1, 0.0)
                #p.addbox("name",lx,ly,lz,px,py,pz)
                print 'return knife'
                result = place_client(0, 0.6, 0.4, 0.0)
                self.p.addBox("knife",objectSize['knife'][0],objectSize['knife'][1],objectSize['knife'][2],
                    knife_px+objectOffset['knife'][0],knife_py+objectOffset['knife'][1],knife_pz+objectOffset['knife'][2])
                #p.addbox("name",lx,ly,lz,px,py,pz)
                print "Finished cutting: ", result
            except rospy.ROSInterruptException:
                print "program interrupted before completion"
        



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

