#! /usr/bin/env python

import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import baxterkitchen.msg

def pick_client():
    client = actionlib.SimpleActionClient('pick_server', baxterkitchen.msg.PickAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.PickGoal(p_x = 0.123, p_y = 0.234, p_z = 0.345)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()  # A PickResult




class OrganizeAction(object):
  # create messages that are used to publish feedback/result
  _feedback = baxterkitchen.msg.OrganizeFeedback()
  _result   = baxterkitchen.msg.OrganizeResult()

  def __init__(self, name):
    self._action_name = name
    self._as = actionlib.SimpleActionServer(self._action_name, baxterkitchen.msg.OrganizeAction, execute_cb=self.execute_cb, auto_start = False)
    self._as.start()
    
  def execute_cb(self, goal): ###################### do action in this execute_cb
    # helper variables
    r = rospy.Rate(1)
    success = True
    

    ##################################################################################
    print 'doing task\n'
    print goal.chore
    print goal.target
    print goal.reps

    if goal.chore == 'wash':
        print 'dummy org received wash request'
        # formulate pick dish request by calling pick client
        # formulate scrub request by calling client
        # formulate place dish request

    if goal.chore == 'cut':
        print 'dummy org received cut request'
        # formulate pick knife request
        # formulate pick target request
        # etc

    
    
    
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
    rospy.init_node('dummy_motion_org')
    OrganizeAction(rospy.get_name())
    rospy.spin()

