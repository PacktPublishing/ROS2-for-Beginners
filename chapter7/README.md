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
  ros2 run drive_robot move_sub
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

# INSTALL ALL DEPENDECIES FOR SLAM:
``` 
  sudo apt install ros-<ros2_distro>-slam-toolbox
```
```
  sudo apt install ros-foxy-slam-toolbox
```
# Navigation 2 :
```
  sudo apt install ros-<ros2-distro>-navigation2
```
```
  sudo apt install ros-foxy-navigation2
```
# Generating a map of the environemnt by the robot.
```
  ros2 launch robot online_async.launch 
```
Gazebo World:
![Screenshot from 2023-03-29 14-54-00](https://user-images.githubusercontent.com/97457075/228560723-45aeb5a2-e9b2-49e3-b5a3-c8b44ef68517.png)

Rviz2(Visualization).

![Screenshot from 2023-03-29 14-53-46](https://user-images.githubusercontent.com/97457075/228561488-94844965-0f0e-4b57-a4f4-11b9757ecb64.png)

Save the map by using the command below:
```
 ros2 run nav2_map_server map_saver_cli -f <name_of_map>
```
When done saving the map,you will get a .pgm and a .yaml file(The .pgm file contains the picture or image of how our map is, while the .yaml contains the information of the map,e.g the resolution of the map etc).

![Screenshot from 2023-03-29 15-12-04](https://user-images.githubusercontent.com/97457075/228566081-900645b7-f07e-4d29-9d6c-a7dd4ad98e8c.png)

# THE MAP SERVER NODE(nav2 map server).

   The map server provides maps to the other Nav2 system and this system use ros 2 topics and also services.Maps can be saved using the map_saver node .The saved map can be provided using the map_server node,which a map will be used and provided to the robot for localization and path-planning.The ROS 2 node that is modular is the Map server. The map server program instances one of these nodes by default ,but if more than one map server node is required,it is possible to combine them into a single process.In comparison to ROS1,the command line for the map server application has somewhat changed.When using ROS1,the map server was called while giving the map’s YAML filename.

# DISPLAY THE .yaml FILE:

image: first.yaml.pgm

mode: trinary

resolution: 0.05

origin: [-20.4, -12.9, 0]

negate: 0

occupied_thresh: 0.65

NOTE: By supplying the the params(parameter) file on the command line, one  can call the map service executable directly as follows:
```
  __params:=<name_of_map>.yaml
```

# PERFORMING PATH PLANNING(SEND THE ROBOT TO GO FROM POINT A TO POINT B).
We have been able to discuss about how we can generate a map of the environment using the slam_toolbox and also how we can save the  generated map.Now,we will be talking about how we can use this generated map,provided to the robot for Autonomous Navigation using Nav2.Open a new terminal and launch the Nav2(localization and Path-planning), all thanks to @Steven macenski for this great package.

```
  ros2 launch robot navigation.launch.py
```

The function which has a variable called use_sim_time , that takes a boolean (either 'true' or 'false').If we are using simulation phase or not (for a simulated robot set the default to ‘true’ , while for a real robot phase set the default parameter to ‘false’).We set to ‘true’ because we are using a simulated robot.

```
def generate_launch_description():
   use_sim_time = LaunchConfiguration('use_sim_time', default='true')
   
   map_dir = LaunchConfiguration(
  'map',
  
  default=os.path.join(
  
  get_package_share_directory('robot'),
  
  'maps',
  
  'offline.yaml'))
```

The param_file_name takes in the name of the nav2.yaml file that contains various parameters used in optimizing the robot when sending a goal to the robot.Ours is called ‘nav2.yaml’ which is located in a directory called ‘params’ and the package name is ‘robot’.	

```
  param_file_name = 'nav2.yaml'
  
  param_dir = LaunchConfiguration(
  
  'params_file',
  
  default=os.path.join(
  
  get_package_share_directory('robot'),
  
  'params',
  
  param_file_name))
```
Open a terminal and launch the following:
```
  ros2 launch robot show.robot.launch.py world:='path to where the created world was saved'
```

Then Open another terminal and launch the Navigation stack(Nav2)The launch file automatically launches the Localization and Path-planning Node.
```
  ros2 launch robot navigation.launch.py
```
# NOTE: The launch file includes the localization node and path planning node in a single thread(component).

After this is launched,we will have to set the initial pose of the robot in the map(initial pose meaning where you think the robot is in the map) This subscribes to the particle filters(it’s a probalistic localization system for a robot which is moving in 2D space it is also called Adaptive Monte Carlo Localization Node).Set the initial pose of the robot using the 2D pose estimate tool and then send navigation command to the robot using the Navigation2 Gaol tool.


![Screenshot from 2023-03-31 13-55-49](https://user-images.githubusercontent.com/97457075/229127893-1ec95da4-5106-4984-a2da-9249c0fcf16d.png)




![Screenshot from 2023-03-31 13-55-57](https://user-images.githubusercontent.com/97457075/229127922-045f6fc9-cf7e-408e-a963-e73c3bea404d.png)


[Screencast from 03-31-2023 01:54:09 PM.webm](https://user-images.githubusercontent.com/97457075/229128097-158af385-226b-4b83-a844-3520b5771a34.webm)

# Driving the robot in Trianglular manner:
```
 ros2 run drive_robot triangle
```
# ROBOT PROGRAMMING USING ROS 2
- let’s program our robot to drive to a certain distance and telling the robot to stop when it reaches that distance travelled. In this process, we will be making use of the odometry topic and also the command velocity topic.The odometry shows and tells the distance travelled by the robot in a pose and orientation.Let’s echo the    odom topic while the robot is at an initial pose.Open a terminal and spawn the robot into gazebo,like we did earlier.When the robot is spawned echo the odometry topic which is ‘/odom’.We will use  the command.

```
  ros2 topic echo /odom
```
We should see an ouput on the terminal,like what shows below.

![Screenshot from 2023-04-03 14-38-09](https://user-images.githubusercontent.com/97457075/229538029-9274bde7-fc64-4bf8-a870-ec23002a4457.png)

The traingluar.py script/node in the package drive_ribot explains the following:
- traingle_movement.py

- The script creates an extension of the “Node” class offered by rclpy called “Draw_traingle”. Initilizing a publisher to publish messages of type “Twist” to the subject “/cmd_vel” with a queue size of 10 is done in the constructor method. Additionally,it develops a timer that starts the “traingle” technique every two seconds.The robot’s motion to draw  a traingle is specified via the “traingle” approach. It uses the “Twist” message to set the robot’s linear and angular velocities,publishes the messages to the “/cmd_vel” topic,and uses the “get looger” method to log the robot’s current action. Then,it uses the “spin_once” technique offered by rclpy to wait for 1 second before moving on the following step. The script also provides a “main” method that starts the ROS event loop using the “spin” method,makes an instances of the “Draw_traingle” class,destroys the node when the loop ends,and closes  down the rclpy library.
     Overall,this script shows how to use the rclpy library to operate a robot in a ROS 2 environment to carry out a straightforward task.

# Driving the robot in circle with an incremental(++) velocity speed:
     
   We will be writing a python node that drives the robot in an incremental speed as the robot moves in circle,we want the robot speed to keep increasing,then when the speed limit get’s to a certain velocity we want the robot to stop.
   -  increment_circle.py 
  
  [Screencast from 04-04-2023 07:26:00 PM.webm](https://user-images.githubusercontent.com/97457075/229885964-3be269ce-87fe-4e11-8cfb-a6461fc6eaba.webm)
