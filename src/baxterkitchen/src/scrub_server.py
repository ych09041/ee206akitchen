#! /usr/bin/env python

import roslib
import rospy

import actionlib

import baxterkitchen.msg
import numpy as np

import sys

import moveit_commander
from moveit_msgs.msg import OrientationConstraint, Constraints
from geometry_msgs.msg import PoseStamped
from baxter_interface import gripper as baxter_gripper
import baxter_interface
from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal, MoveGroupFeedback, MoveGroupResult, JointConstraint



class ScrubAction(object):
    # create messages that are used to publish feedback/result
    _feedback = baxterkitchen.msg.ScrubFeedback()
    _result   = baxterkitchen.msg.ScrubResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, baxterkitchen.msg.ScrubAction, execute_cb=self.execute_cb, auto_start = False)
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
        rospy.loginfo('scrubbing that dish')

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
        delta_w0 = 0.2
        time_gap = 0.5
        
        left_arm.set_joint_value_target('left_s0',-0.73)
        left_arm.set_joint_value_target('left_s1',-0.47)
        left_arm.set_joint_value_target('left_e0',0.0157)
        left_arm.set_joint_value_target('left_e1',2.05)
        left_arm.set_joint_value_target('left_w0',-1.62)
        left_arm.set_joint_value_target('left_w1',1.55)
        left_arm.set_joint_value_target('left_w2',3.05)
        print "going to scrub position"
        left_arm.execute(left_arm.plan())
        rospy.sleep(2.0)




        angles = limb.joint_angles()
        a0 = angles['left_s0']
        a1 = angles['left_s1']
        a2 = angles['left_e0']
        a3 = angles['left_e1']
        a4 = angles['left_w0']
        a5 = angles['left_w1']
        a6 = angles['left_w2']

        for times in range(0,3):
            # first scrub
            left_arm.set_joint_value_target('left_s0',a0)
            left_arm.set_joint_value_target('left_s1',a1)
            left_arm.set_joint_value_target('left_e0',a2)
            left_arm.set_joint_value_target('left_e1',a3)
            left_arm.set_joint_value_target('left_w0',a4+delta_w0)
            left_arm.set_joint_value_target('left_w1',a5)
            left_arm.set_joint_value_target('left_w2',a6)
            left_arm.execute(left_arm.plan())
            print 'first scrub'
            rospy.sleep(time_gap)

            # second scrub
            left_arm.set_joint_value_target('left_s0',a0)
            left_arm.set_joint_value_target('left_s1',a1)
            left_arm.set_joint_value_target('left_e0',a2)
            left_arm.set_joint_value_target('left_e1',a3)
            left_arm.set_joint_value_target('left_w0',a4-delta_w0)
            left_arm.set_joint_value_target('left_w1',a5)
            left_arm.set_joint_value_target('left_w2',a6)
            left_arm.execute(left_arm.plan())
            print 'second scrub'
            rospy.sleep(time_gap)

       
       
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
    rospy.init_node('scrub_server')
    print 'scrub server running...'
    ScrubAction(rospy.get_name())
    rospy.spin()
