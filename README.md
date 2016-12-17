EE 206A Fall 2016

UC Berkeley

[baxterkitchen.weebly.com](baxterkitchen.weebly.com)


Baxter kitchen assistant is aimed at helping users with simple kitchen chores such as cleaning dishes and preparing ingredients for cooking. The robot receives user commands in the form of a text file, creates a list of tasks such as chopping vegetables and cleaning dishes, and completes them in an optimized sequence. 
​
This project takes a step towards solving interesting problems of robotic manipulation in household and kitchen setting. The problem involves complicated sequences of motions that need to be executed by Baxter, and requires accurate object detection and robust obstacle avoidance. If implemented correctly, Baxter kitchen assistant could significantly reduce human labor in food preparation, improve safety, and provide better, more consistent quality service. ​

The goal of the project is to have Baxter determine the sequence of tasks to perform from the user input recipe, determine the location of object and tools, plan the arm motion trajectory, and lastly, execute the trajectory. For safety, all tools and objects such as dish, foods, and knife will represented with toy props. All objects in the workspace will be marked with Augmented Reality (AR) tags to assist position and pose estimation.

Baxter should be able to perform two tasks: cutting vegetables and cleaning dishes. For the cutting task, Baxter should be able to accurately pick up the knife and the vegetable (carrot and/or corn depending on the recipe text). Baxter should perform the cutting motion with specified number of repetitions (eg. 3 pieces) and then place everything back to where they belong. For the washing task, Baxter should be able to pick up the dish from the tray, pick up sponge, perform the scrubbing motion then return each item. to where they belong. During the process, Baxter should plan its movement without hitting other objects on the table.
