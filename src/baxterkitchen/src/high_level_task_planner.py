#!/usr/bin/env python

import sys

import rospy
import roslib
import actionlib
from std_msgs.msg import String
import baxterkitchen.msg

import numpy as np


def callback(m):
    print m

wash_list = []
wash_rep_list = []
cut_list = []
cut_rep_list = []


def dummy_organize_client(ch, ta, re):
    print ch
    print ta
    print re
    return True


def organize_client(ch, ta, re, rt):
    client = actionlib.SimpleActionClient('motion_organizer', baxterkitchen.msg.OrganizeAction)
    client.wait_for_server()
    goal = baxterkitchen.msg.OrganizeGoal(chore = ch, target = ta, reps = re, return_tool = rt)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()



#Define the method which contains the node's main functionality
def high_level_planning():

    rospy.init_node('high_level_task_planner', anonymous=True)

    recipe_file = open(sys.argv[1], 'r')
    for line in recipe_file:
        words = line.split()
        if words[0] == 'wash':
            if words[2] in wash_list:
                wash_rep_list[wash_list.index(words[2])] += int(words[1])
            else:
                wash_list.append(words[2])
                wash_rep_list.append(0);
                wash_rep_list[wash_list.index(words[2])] += int(words[1])
        elif words[0] == 'cut':
            if words[4] in cut_list: # skip the 'of'
                cut_rep_list[cut_list.index(words[4])] += int(words[1])
            else:
                cut_list.append(words[4])
                cut_rep_list.append(0);
                cut_rep_list[cut_list.index(words[4])] += int(words[1])
    recipe_file.close()

    print wash_list
    print wash_rep_list
    print cut_list
    print cut_rep_list

    print 'BEGIN CUTTING...'
    for i in range(len(cut_list)):
        if i==len(cut_list):
            result = organize_client('cut', cut_list[i], cut_rep_list[i], True)
        else:
            result = organize_client('cut', cut_list[i], cut_rep_list[i], False)
        print result
    print 'DONE CUTTING.'
    print 'BEGIN WASHING...'
    for i in range(len(wash_list)):
        result = organize_client('wash', wash_list[i], wash_rep_list[i])
        print result
    print 'DONE WASHING.'
    print 'ALL DONE!'        


#Python's syntax for a main() method
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method
    high_level_planning()
