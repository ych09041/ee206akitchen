import rospy


def main():
  # # create a planning scene interface, provide name of root link
  # p = PlanningSceneInterface("torso")
  print("asfd")

  # # add a cube of 0.1m size, at [1, 0, 0.5] in the base_link frame
  # p.addCube("my_cube", 0.1, 1, 0, 0.5)

  # # do something

  # # remove the cube
  # p.removeCollisionObject("my_cube")



if __name__ == '__main__':
    rospy.init_node( "moveit_py")
    main()