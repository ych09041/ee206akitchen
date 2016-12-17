# UC Berkeley EE206A Fall 2016


<https://baxterkitchen.weebly.com>

Baxter kitchen assistant is aimed at helping users with simple kitchen chores such as cleaning dishes and preparing ingredients for cooking. The robot receives user commands in the form of a text file, creates a list of tasks such as chopping vegetables and cleaning dishes, and completes them in an optimized sequence. 

## Launch files:

**calibrate.launch**: Moves Baxter arms to predefined locations. This should be run before placing the calibration bar on the table.  
**vision.launch**: Launches the camera feed and ar_track_alvar processing.  
**vision_cory.launch**: Same thing as vision.launch, but for use in Cory lab.  
**full_run.launch**: Starts the main program, nodes, and action servers. Performs the list of tasks.


## Nodes in baxterkitchen package:

**high_level_task_planner.py**: Parses recipe.txt and issues task requests.  
**motion_organizer.py**: Receives task request and formulates a sequence of action requests.  
**object_identifier.py**: Determines object positions and publishes to the *inventory* topic.  
**pick_server.py**: Action server for picking up an object at the specified location.  
**place_server.py**: Action server for placing an object at the specified location.  
**move_server.py**: Action server for moving the gripper to the specified location.  
**cut_server.py**: Action server for performing the cutting motion.  
**scrub_server.py**: Action server for performing the scrubbing motion.  
**untuck_server.py**: Action server for resetting the arms.  


## AR tag bundles:

All bundle definition for each object are placed in *ar_track_alvar/bundles*.
