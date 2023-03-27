# Ros-2-simulated-robot.
A ros 2 simulated robot.

NOTE: You can also use a cad design software(FUSION 360, SOLIDWORKS......) to design the robot and export to ROS  and also ROS 2,but this is just a repository that describes how to design a robot manually, by writing .xacro files which are said to be robot meshes.

Fisrt step in building the differential-drive robot:

Launch the Node:
```
  ros2 launch <name_of_package> robot.launch.py
```

The joint state publisher node must be launched/be active when launching the robot in rviz2.
```
  ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

Open Rviz2:
```
  ros2 run rviz2 rviz2
```

Set the fixed frame to "base_link".

The centre of the robot which is the "base_link".

Plugins used in simulation of the robot can be gotten from:
https://classic.gazebosim.org/tutorials?tut=ros_gzplugins


STEPS TO TAKE TO GET THE ROBOT UP AND READY:
1. Launch the robot_state_publisher in simulation mode.
2. Launch Gazebo.
3. Spawn the robot into Gazebo.

Set the sim time to true,we dealing with simulation.So our the boolean has to be true.
```
   ros2 launch robot robot.launch.py use_sim_time:=true
```
Start up Gazebo:
```
   ros2 launch gazebo_ros gazebo.launch.py 
```

# SPAWNING THE ROBOT INTO GAZEBO:
     To spawn the robot into gazebo, launch the file called show.robot.launch.py (Note: launch files in ROS 2 are python scripts/files)
 Command:
 ```
   ros2 launch robot show.robot.launch.py
 ```
 Check if the topics are available.This list all topics which are available:
 ```
   ros2 topic list
 ```
 Now,we can drive the robot around once we use the teleop_twist_keyboard node to publish to the "/cmd_vel" topic that the robot subscribes to.
 
 ```
   ros2 run teleop_twist_keyboard  teleop_twist_keyboard
 ```
 
 You can give colour to the robot,by adding colour to the .xacro file.Video decription below,while using the teleop_twist_keyboard to drive the robot.
 
 We can also write a python script that publish certain velocity to make the robot move and also perform some basic task.
 Create a ROS 2 package called drive_robot ,its dependecies on rclpy,the package should be created in the src directory of your workspace.
 
 ```
   cd src
 ```
 
 ```
   ros2 pkg create drive_robot --build-type ament_python --dependencies rclpy
 
 ```
 Run the node in the pasckage to make the robot drive forward, in linear of x.
 ```
   ros2 run drive_robot velocity_drive
 ```

# LAUNCHING SAVED GAZEBO WORLD WITH ROBOT SPAWNED IN IT.
 ```
    ros2 launch robot show.robot.launch.py world:='path to where you saved your Gazebo world'
 ```
 ![Screenshot from 2023-03-07 16-57-01](https://user-images.githubusercontent.com/97457075/223492102-4b27dd07-a5f6-4b56-91f1-b20b52a065ba.png)
![Screenshot from 2023-03-07 17-02-44](https://user-images.githubusercontent.com/97457075/223492458-2b3d6ffe-db92-44e4-8a41-42573fa984d6.png)

You can check the TF2 TREE:
```
  ros2 run rqt_tf_tree rqt_tf_tree
```
![Screenshot from 2023-03-08 19-52-28](https://user-images.githubusercontent.com/97457075/223807831-64f8f7f3-c000-4d08-82b0-b4725c639a14.png)

# To LAUNCH THE WORLD:
 
```
   ros2 launch robot show.robot.launch.py world:="path to the .world file"
```
Mine is:
```
  ros2 launch robot show.robot.launch.py world:=/home/magnum/simuate_ws/src/robot/worlds/new.world
```
![Screenshot from 2023-03-08 23-10-51](https://user-images.githubusercontent.com/97457075/223862718-2ca56db5-4b6a-4a9e-a5b2-625d82918a81.png)

# SLAM 
Run the slam_toolbox node.
```
  ros2 launch robot online_async.launch.py 
```
[Screencast from 03-09-2023 11:21:33 AM.webm](https://user-images.githubusercontent.com/97457075/224001965-dfaaf7e7-9660-437a-94b4-5b78740142ad.webm)

# DRIVING THE ROBOT PROGRAMMATICALLY:
Open a new terminal and type the command below:
```
  ros2 run drive_robot velocity_drive
```
You will see the robot drive forward like the video illustracted below:

[Screencast from 03-26-2023 03:47:34 PM.webm](https://user-images.githubusercontent.com/97457075/227783989-12f4b40f-e356-4ea7-907f-0c4183c9544b.webm)

We can echo the '/cmd_vel' topic to see the amount of velocity speed which is being published to the robot,since the robot is driving forward at 0.2.We should see 0.2  at linear of x ,being echoed out.Command as stated below:
```
  ros2 topic echo /cmd_vel
```
![Screenshot from 2023-03-26 16-02-30](https://user-images.githubusercontent.com/97457075/227784606-ca28d38e-26b3-483f-96de-ce14dbcfb8a0.png)

# We can write a node to subscribes to the '/cmd_vel' topic when velocity is being pubslished to the robot.
Run the node with the command below:
```
  ros2 run drive_robot move_sub.py
```
We should see the robot drive at a certain velocity,while the move_sub.py node subscibes to the velocity speed.Illustration below:

![Screenshot from 2023-03-26 17-19-37](https://user-images.githubusercontent.com/97457075/227789768-c0acbf3e-9d65-4fa2-9dd6-060e9a163ee1.png)





![Screenshot from 2023-03-26 17-19-45](https://user-images.githubusercontent.com/97457075/227789676-2828ce54-b4ea-4f2e-911a-a501025ed30f.png)

[Screencast from 03-26-2023 05:31:06 PM.webm](https://user-images.githubusercontent.com/97457075/227790106-023d7f1a-f0fb-4f7b-bd36-4efef240cf9c.webm)

# Obstacle Avoidance Node:
To run the node , Open a new terminal and execute the node with the command below:
```
  ros2 run drive_robot obstacle_avoidance
```
The node helps to avoid obstacle and tells to robot to rotate to the available free space.While avoiding the obstacle.


[Screencast from 03-27-2023 09:30:39 AM.webm](https://user-images.githubusercontent.com/97457075/227890748-a77d4407-c20c-4d64-ad29-abedcb7a3e39.webm)


