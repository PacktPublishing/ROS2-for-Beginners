#!/usr/bin/env python3
import rclpy
from my_robot_message.msg import Coordinates
from rclpy.node import Node

#Create a class called movement.
class movement(Node):
    def __init__(self):
        super().__init__("code")#Initializing the ros2 node
        self.pub = self.create_publisher(Coordinates,'/cmd_vel',100)#publish to cmd_vel topic.
        self.publishing = Coordinates() #An object that stores Coordinates.
        self.time = 0.05
        self.timer = self.create_timer(self.time,self.velocity_message)

    #A method called velocity_message.
    def velocity_message(self):
        self.publishing.linear.p = 0.2
        self.pub.publish(self.publishing)
        print("The robot moves foward:")


#Main function that stores the class called movement.
def main(args=None):
    rclpy.init(args=args)
    velocity_publishing = movement()
    rclpy.spin(velocity_publishing)
    velocity_publishing.destroy_node()


if __name__ == '__main__':
    main()        
