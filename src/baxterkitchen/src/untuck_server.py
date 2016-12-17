#! /usr/bin/env python

'''
UC Berkeley EE 206A Fall 2016
Baxter Kitchen Assistant
Tony Abdo, Xiaotian Fan, Cheng Hao Yuan

'''

import roslib
import rospy

import actionlib

import baxterkitchen.msg


import sys

import moveit_commander
from moveit_msgs.msg import OrientationConstraint, Constraints
from geometry_msgs.msg import PoseStamped
from baxter_interface import gripper as baxter_gripper
import baxter_interface




class UntuckAction(object):
    # create messages that are used to publish feedback/result
    _feedback = baxterkitchen.msg.UntuckFeedback()
    _result   = baxterkitchen.msg.UntuckResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, baxterkitchen.msg.UntuckAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal): ###################### do action in this execute_cb
        # helper variables
        r = rospy.Rate(1)
        success = True

        # dummy feedback
        self._feedback.fb_x = 0.1
        self._feedback.fb_z = 0.1
        self._feedback.fb_y = 0.1

        # publish info to the console for the user
        #    rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i' % (self._action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))
        rospy.loginfo('placing stuff to moves')

        ## target position


        # start executing the action
        print 'server received goal: '

        ##################################################################################



        #Initialize moveit_commander
        moveit_commander.roscpp_initialize(sys.argv)
        #Set up the grippers
        left_gripper = baxter_gripper.Gripper('left')
        right_gripper = baxter_gripper.Gripper('right')


        #Initialize both arms
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        left_arm = moveit_commander.MoveGroupCommander('left_arm')
        right_arm = moveit_commander.MoveGroupCommander('right_arm')
        left_arm.set_planner_id('RRTConnectkConfigDefault')
        left_arm.set_planning_time(10)
        right_arm.set_planner_id('RRTConnectkConfigDefault')
        right_arm.set_planning_time(10)

        limb = baxter_interface.Limb('left')
        
        left_arm.set_joint_value_target('left_s0',-0.05)
        left_arm.set_joint_value_target('left_s1',-0.95)
        left_arm.set_joint_value_target('left_e0', -1.21)
        left_arm.set_joint_value_target('left_e1',1.93)
        left_arm.set_joint_value_target('left_w0', 0.676)
        left_arm.set_joint_value_target('left_w1',1.04)
        left_arm.set_joint_value_target('left_w2', -0.5)
        left_arm.execute(left_arm.plan())
        rospy.sleep(2.0)

        rimb = baxter_interface.Limb('right')
        
        right_arm.set_joint_value_target('right_s0',0.082)
        right_arm.set_joint_value_target('right_s1',-1.0)
        right_arm.set_joint_value_target('right_e0',1.188)
        right_arm.set_joint_value_target('right_e1',1.938)
        right_arm.set_joint_value_target('right_w0', -0.668)
        right_arm.set_joint_value_target('right_w1',1.032)
        right_arm.set_joint_value_target('right_w2', 0.498)
        right_arm.execute(right_arm.plan())
        rospy.sleep(2.0)


        #####################################################################################
        '''
        name: ['', '', 'left_e0', 'left_e1', 'left_s0', 'left_s1', 'left_w0', 'left_w1', 'left_w2', 
        posi: [ 0,  9,   -1.21,    1.929,     -0.0510,  -0.948357,  0.675718, 1.03697196, -0.498163, 
        'right_e0', 'right_e1', 'right_s0', 'right_s1', 'right_w0', 'right_w1', 'right_w2', 'torso_t0']
        1.18768465, 1.93818472, 0.0820679, -0.99862143, -0.6684369, 1.0316028, 0.49816813, -12.5659838]
        '''


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
    rospy.init_node('untuck_server')
    print 'untuck server running...'
    UntuckAction(rospy.get_name())
    rospy.spin()
