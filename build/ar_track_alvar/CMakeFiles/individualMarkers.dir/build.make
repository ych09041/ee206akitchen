# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/team15/ee206akitchen/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/team15/ee206akitchen/build

# Include any dependencies generated for this target.
include ar_track_alvar/CMakeFiles/individualMarkers.dir/depend.make

# Include the progress variables for this target.
include ar_track_alvar/CMakeFiles/individualMarkers.dir/progress.make

# Include the compile flags for this target's objects.
include ar_track_alvar/CMakeFiles/individualMarkers.dir/flags.make

ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o: ar_track_alvar/CMakeFiles/individualMarkers.dir/flags.make
ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o: /home/team15/ee206akitchen/src/ar_track_alvar/nodes/IndividualMarkers.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/team15/ee206akitchen/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o"
	cd /home/team15/ee206akitchen/build/ar_track_alvar && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o -c /home/team15/ee206akitchen/src/ar_track_alvar/nodes/IndividualMarkers.cpp

ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.i"
	cd /home/team15/ee206akitchen/build/ar_track_alvar && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/team15/ee206akitchen/src/ar_track_alvar/nodes/IndividualMarkers.cpp > CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.i

ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.s"
	cd /home/team15/ee206akitchen/build/ar_track_alvar && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/team15/ee206akitchen/src/ar_track_alvar/nodes/IndividualMarkers.cpp -o CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.s

ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.requires:
.PHONY : ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.requires

ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.provides: ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.requires
	$(MAKE) -f ar_track_alvar/CMakeFiles/individualMarkers.dir/build.make ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.provides.build
.PHONY : ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.provides

ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.provides.build: ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o

# Object files for target individualMarkers
individualMarkers_OBJECTS = \
"CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o"

# External object files for target individualMarkers
individualMarkers_EXTERNAL_OBJECTS =

/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: ar_track_alvar/CMakeFiles/individualMarkers.dir/build.make
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /home/team15/ee206akitchen/devel/lib/libar_track_alvar.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /home/team15/ee206akitchen/devel/lib/libkinect_filtering.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libimage_transport.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libresource_retriever.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libcv_bridge.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libpcl_ros_filters.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libpcl_ros_io.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libpcl_ros_tf.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_common.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_octree.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_io.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_kdtree.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_search.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_sample_consensus.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_filters.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_features.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_keypoints.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_segmentation.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_visualization.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_outofcore.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_registration.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_recognition.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_surface.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_people.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_tracking.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libpcl_apps.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_serialization.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libqhull.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libOpenNI.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libflann_cpp_s.a
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libvtkCommon.so.5.8.0
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libvtkRendering.so.5.8.0
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libvtkHybrid.so.5.8.0
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libvtkCharts.so.5.8.0
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libnodeletlib.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libbondcpp.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libuuid.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libclass_loader.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/libPocoFoundation.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libdl.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libroslib.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/librosbag.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/librosbag_storage.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libroslz4.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/liblz4.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libtopic_tools.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libtf.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libtf2_ros.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libactionlib.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libmessage_filters.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libtf2.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libroscpp.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/librosconsole.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/librosconsole_log4cxx.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/librosconsole_backend_interface.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/liblog4cxx.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libxmlrpcpp.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libdynamic_reconfigure_config_init_mutex.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libroscpp_serialization.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/librostime.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /opt/ros/indigo/lib/libcpp_common.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers: ar_track_alvar/CMakeFiles/individualMarkers.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers"
	cd /home/team15/ee206akitchen/build/ar_track_alvar && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/individualMarkers.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
ar_track_alvar/CMakeFiles/individualMarkers.dir/build: /home/team15/ee206akitchen/devel/lib/ar_track_alvar/individualMarkers
.PHONY : ar_track_alvar/CMakeFiles/individualMarkers.dir/build

ar_track_alvar/CMakeFiles/individualMarkers.dir/requires: ar_track_alvar/CMakeFiles/individualMarkers.dir/nodes/IndividualMarkers.cpp.o.requires
.PHONY : ar_track_alvar/CMakeFiles/individualMarkers.dir/requires

ar_track_alvar/CMakeFiles/individualMarkers.dir/clean:
	cd /home/team15/ee206akitchen/build/ar_track_alvar && $(CMAKE_COMMAND) -P CMakeFiles/individualMarkers.dir/cmake_clean.cmake
.PHONY : ar_track_alvar/CMakeFiles/individualMarkers.dir/clean

ar_track_alvar/CMakeFiles/individualMarkers.dir/depend:
	cd /home/team15/ee206akitchen/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/team15/ee206akitchen/src /home/team15/ee206akitchen/src/ar_track_alvar /home/team15/ee206akitchen/build /home/team15/ee206akitchen/build/ar_track_alvar /home/team15/ee206akitchen/build/ar_track_alvar/CMakeFiles/individualMarkers.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : ar_track_alvar/CMakeFiles/individualMarkers.dir/depend

