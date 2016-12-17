EE 206A Fall 2016

UC Berkeley

baxterkitchen.weebly.com


Baxter kitchen assistant is aimed at helping users with simple kitchen chores such as cleaning dishes and preparing ingredients for cooking. The robot receives user commands in the form of a text file, creates a list of tasks such as chopping vegetables and cleaning dishes, and completes them in an optimized sequence. 

Launch files:

calibrate.launch: Moves Baxter arms to predefined locations. This should be run before placing the calibration bar on the table.

vision.launch: Launches the camera feed and ar_track_alvar processing.

vision_cory.launch: Same thing as vision.launch, but for use in Cory lab.

full_run.launch: Starts the main program, nodes, and action servers. Performs the list of tasks.


Nodes:

ar_track_alvar/bundles contains the AR tag bundle defintion for each object.
