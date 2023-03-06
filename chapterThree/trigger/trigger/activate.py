#!/usr/bin/env python3
import rclpy #import the python rclpy library.
from std_msgs.msg import Empty #import the std_msg package which has a type called Empty.
from rclpy.node import Node


#A class that handles all execution.
class trigg(Node):
    def __init__(self):
        super().__init__('activate')
        self.light_up = Empty()
        self.pub = self.create_publisher(Empty,"/led",10)
        

    #create a method that handles the node for turning on and of a L.E.D.
    def active(self):
        self.enter = input(" Press a key on your keyboard: ")
        if self.enter == "q":
            self.pub.publish(self.light_up)

#A function that stores the class which was saved in an object/variable 
def main(args=None):
    rclpy.init(args=args)
    store = trigg()
    rclpy.spin(store)
    #rclpy.shutdown()
    #store.destroy_node()

if __name__ == '__main__':
    main() #we call the main function in here.
