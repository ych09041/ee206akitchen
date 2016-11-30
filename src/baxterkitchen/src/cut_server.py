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



class CutAction(object):
    # create messages that are used to publish feedback/result
    _feedback = baxterkitchen.msg.CutFeedback()
    _result   = baxterkitchen.msg.CutResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, baxterkitchen.msg.CutAction, execute_cb=self.execute_cb, auto_start = False)
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
        rospy.loginfo('cutting up that cucumber')

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
        
        length = 0.02
        gap = -0.02
        height = 0.02
        
       
        for _move in range(0, 3):
            #Get ready ------------------------------------------------------
            print "getting ready"
            goal_1 = PoseStamped()
            goal_1.header.frame_id = "base"

            #x, y, and z position
            goal_1.pose.position.x = goal.p_x+length
            goal_1.pose.position.y = goal.p_y+gap
            goal_1.pose.position.z = goal.p_z+height

            #Orientation as a quaternion
            goal_1.pose.orientation.x = 0.0
            goal_1.pose.orientation.y = -1.0
            goal_1.pose.orientation.z = 0.0
            goal_1.pose.orientation.w = 0.0
        
            left_arm.set_pose_target(goal_1)
            left_arm.set_start_state_to_current_state()
            left_plan = left_arm.plan()
            left_arm.execute(left_plan)
            rospy.sleep(gap)
            
            #Descend ------------------------------------------------------
            print "descend the blade"
            goal_1 = PoseStamped()
            goal_1.header.frame_id = "base"

            #x, y, and z position
            goal_1.pose.position.x = goal.p_x+length
            goal_1.pose.position.y = goal.p_y+gap
            goal_1.pose.position.z = goal.p_z

            #Orientation as a quaternion
            goal_1.pose.orientation.x = 0.0
            goal_1.pose.orientation.y = -1.0
            goal_1.pose.orientation.z = 0.0
            goal_1.pose.orientation.w = 0.0
            
            left_arm.set_pose_target(goal_1)
            left_arm.set_start_state_to_current_state()
            left_plan = left_arm.plan()
            left_arm.execute(left_plan)
            rospy.sleep(gap)
            
            #Slide ------------------------------------------------------
            # how do we make sure it's a straight line? just use smaller increments? or should we do blade dropping type of cut
            print "slide!!!"
            goal_1 = PoseStamped()
            goal_1.header.frame_id = "base"

            #x, y, and z position
            goal_1.pose.position.x = goal.p_x-length
            goal_1.pose.position.y = goal.p_y+gap
            goal_1.pose.position.z = goal.p_z

            #Orientation as a quaternion
            goal_1.pose.orientation.x = 0.0
            goal_1.pose.orientation.y = -1.0
            goal_1.pose.orientation.z = 0.0
            goal_1.pose.orientation.w = 0.0
            
            left_arm.set_pose_target(goal_1)
            left_arm.set_start_state_to_current_state()
            left_plan = left_arm.plan()
            left_arm.execute(left_plan)
            rospy.sleep(gap)
            
            
            gap = gap + gap


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
    rospy.init_node('cut_server')
    print 'cut server running...'
    CutAction(rospy.get_name())
    rospy.spin()
