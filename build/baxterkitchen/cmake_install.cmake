# Install script for directory: /home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/src/baxterkitchen

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/install")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen/action" TYPE FILE FILES
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/src/baxterkitchen/action/Fibonacci.action"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/src/baxterkitchen/action/Pick.action"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen/msg" TYPE FILE FILES
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciAction.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciActionGoal.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciActionResult.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciActionFeedback.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciGoal.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciResult.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/FibonacciFeedback.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen/msg" TYPE FILE FILES
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickAction.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickActionGoal.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickActionResult.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickActionFeedback.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickGoal.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickResult.msg"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/baxterkitchen/msg/PickFeedback.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen/cmake" TYPE FILE FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/build/baxterkitchen/catkin_generated/installspace/baxterkitchen-msg-paths.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/include/baxterkitchen")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/share/common-lisp/ros/baxterkitchen")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/lib/python2.7/dist-packages/baxterkitchen")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/devel/lib/python2.7/dist-packages/baxterkitchen")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/build/baxterkitchen/catkin_generated/installspace/baxterkitchen.pc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen/cmake" TYPE FILE FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/build/baxterkitchen/catkin_generated/installspace/baxterkitchen-msg-extras.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen/cmake" TYPE FILE FILES
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/build/baxterkitchen/catkin_generated/installspace/baxterkitchenConfig.cmake"
    "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/build/baxterkitchen/catkin_generated/installspace/baxterkitchenConfig-version.cmake"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxterkitchen" TYPE FILE FILES "/home/cc/ee106a/fa16/class/ee106a-acu/ee206akitchen/src/baxterkitchen/package.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

