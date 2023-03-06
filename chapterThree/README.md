# ros2_message.
This package explains how to create a ros2 custom message/interface.

Create a package in the src folder/directory:
```
 ros2 pkg create message_creation --build-type ament_cmake --dependecies rclcpp std_msgs
 ```
In the newly created folder/package,we will create a directory called msg.Once we are done with that we will cd into the msg directory/folder and use the command below to create a file called "Creation.msg".
```
 touch Creation.msg
```
In the Creation.msg file add the following below:
```
 int32 day
 string month
 int32 year
```
before we compile our workspace we have to modify our CMakeLists.txt and package.xml file.In the CMakeLists.txt add the following below:
```
find_package(rosidl_default_generators REQUIRED)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()
```
The function above includes all the messages of package to be compiled,this also should be added into the "CMakeLists.txt" file.
We also need to do some modification in the package.xml file.Add the following below to your package.xml file.
```
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>
```
Then after we are done with all the above modification,we will build our workspace with the:
```
colcon build or 
colcon build --symlink-install
```
Then we will the source the workspace:
```
source install/setup.bash
```
We source our workspace,so that we can use the newly created message.Type the following command to publish via the terminal.
```
ros2 topic pub /display message_creation/Creation "{day: '12', month: 'February', year: '2023'}"
```
We can check the topic ssigned to the message by opening a new terminal:
```
ros2 topic list
```
We will see the topic called /display publsihed to the terminal.![interface](https://user-images.githubusercontent.com/97457075/219212856-4b1a2ba7-d9d7-4180-b566-a2b25ff50f65.png)

# TO LEARN MORE ABOUT ROS2 INTERFACES:
https://github.com/ros2/common_interfaces

# RUNNING THE ROS2 NODE THAT PUBLISH TO THE "/toggle_led" Topic.

To run this node make sure you source the ros2 distro version, you got installed on your ubuntu machine.
command:
```
  source /opt/ros/<ros2_distro>/setup.bash
```

Once you have done this,go into your ros2 catkin_ws and soure the workspace typing the command below:
```
  source install/setup.bash
```

Now,let's run the node to publsih to the L.E.D topic.
```
  ros2 run trigger trig
```

We check the topic,by typing the command below:
```
  ros2 topic list
```

Also,we can echo the topic by:
```
  ros2 echo /toggle_led
```

To make use of the arduino Node that subscribes to the "/led" topic. Navigate into src folder of the workspace and you will see the folder called toogle_led.Copy the Node in the .ino file and paste into the arduino.

```
 cd src
```

NOTE:
 We need to install the rossrial libabry so we can be able to use the .ino Node.
 
Once the Node is uploaded into the Arduino Micro-controller,we will need to use the rosserial arduino to bridge the topics over to ros. Install the rosserial package in ros.
command:
```
  sudo apt-get install ros-<ros_distro>-rosserial
  sudo apt-get install ros-<ros_distro>-rosserial-arduino
```

To run the ros2 publisher node,type the command below.
```
   ros2 run trigger trig
```

Type the below command to check the topic available:
```
  ros2 topic list
```

