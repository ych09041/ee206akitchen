import rospy
from moveit_python import *

rospy.init_node("moveit_py")
# # create a planning scene interface, provide name of root link
# p = PlanningSceneInterface("base_link")

# # add a cube of 0.1m size, at [1, 0, 0.5] in the base_link frame
# p.addCube("my_cube", 0.1, 1, 0, 0.5)

# # do something

# # remove the cube
# p.removeCollisionObject("my_cube")