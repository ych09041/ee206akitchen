#! /usr/bin/env python

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

        ## target position
        goal.p_x
        goal.p_y
        goal.p_z




        # start executing the action
        print 'server received goal: '
        print goal.p_x
        print goal.p_y
        print goal.p_z

        ##################################################################################
        limb = baxter_interface.Limb('left')
        '''

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



        #First goal pose ------------------------------------------------------
        goal_1 = PoseStamped()
        goal_1.header.frame_id = "base"

        #x, y, and z position
        goal_1.pose.position.x = goal.p_x
        goal_1.pose.position.y = goal.p_y
        goal_1.pose.position.z = goal.p_z

        #Orientation as a quaternion
        goal_1.pose.orientation.x = 0.0
        goal_1.pose.orientation.y = 0.0
        goal_1.pose.orientation.z = -1.0
        goal_1.pose.orientation.w = 0.0

        #Scrub is for left arm only
        #Set the goal state to the pose you just defined
        #left_arm.set_pose_target(goal_1)

        #Set the start state for the left arm
        #left_arm.set_start_state_to_current_state()

        #Plan a path
        #left_plan = left_arm.plan()

        #Execute the plan
        #left_arm.execute(left_plan)
        #rospy.sleep(2.0)

        '''
        ## scrub stuff
        # extract current configuration
        angles = limb.joint_angles()

        # print current config
        print angles

        # obtain the joint angles
        a0 = angles['left_s0']
        a1 = angles['left_s1']
        a2 = angles['left_e0']
        a3 = angles['left_e1']
        a4 = angles['left_w0']
        a5 = angles['left_w1']
        a6 = angles['left_w2']

        #generate the wave patterns
        delta_a5 = 0.1
        delta_a6 = 0.1
        #pos_1 = {'left_s0': a0, 'left_s1': a1, 'left_e0': a2, 'left_e1': a3, 'left_w0': a4, 'left_w1': a5+delta_a5, 'left_w2': a6+delta_a6}
        pos_1 = {'left_s0': 0, 'left_s1': 0, 'left_e0': 0, 'left_e1': 0, 'left_w0': 0, 'left_w1': -0.2, 'left_w2': -0.1}
        #pos_2 = {'left_s0': a0, 'left_s1': a1, 'left_e0': a2, 'left_e1': a3, 'left_w0': a4, 'left_w1': a5-delta_a5, 'left_w2': a6-delta_a6}
        pos_2 = {'left_s0': 0, 'left_s1': 0, 'left_e0': 0, 'left_e1': 0, 'left_w0': 0, 'left_w1': 0.2, 'left_w2': 0.1}

        # wipe three times
        for _move in range(3):
            print 'trying to move to scrub pos_1'
            limb.move_to_joint_positions(pos_1)
            print 'trying to move to scrub pos_2'
            limb.move_to_joint_positions(pos_2)




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
    rospy.init_node('scrub_server')
    print 'scrub server running...'
    ScrubAction(rospy.get_name())
    rospy.spin()
