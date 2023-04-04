import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import Twist 
from math import pi 
from rclpy.clock import Clock
import time 

class circle_incremental(Node):
    def __init__(self):
        super().__init__('increment_speed')
        self.pub = self.create_publisher(Twist,'/cmd_vel',10)
        self.velocity_message = Twist()
        self.clock__ = self.get_clock()
        self.start_time = self.clock__.now()
        self.time = 0.05
        self.nano_seconds = 30000000000
        

    #method circle_increment.
    def circle_increment(self,speed_forward,speed_left,stop):
        self.velocity_message.linear.x =speed_forward
        self.velocity_message.angular.z = speed_left
        self.get_logger().info('The summation of the combined speed of velocity of linear.x & angular.z is: ' + str(speed_forward+-(speed_left)))
        self.pub.publish(self.velocity_message)
        self.get_logger().info('The robot is moving in circle....')

        while True:
            self.velocity_message.linear.x ++0.05
            self.velocity_message.angular.z ++0.05
            self.get_logger().info('Both velocity of linear x & angular velocity increased by 0.05.....')
            self.pub.publish(self.velocity_message)
            self.current_time = self.clock__.now()
            self.time_elapsed = self.current_time - self.start_time
            if (self.time_elapsed.nanoseconds >self.nano_seconds): #30 seconds.
                self.velocity_message.linear.x = stop
                self.velocity_message.angular.z = stop
                self.get_logger().info('The robot has stopped at velocity speed of:'+str(stop))
            

def main(args=None):
    rclpy.init(args=args)
    objectt = circle_incremental()
    objectt.circle_increment(0.2,-0.2,0.0)
    rclpy.spin(objectt)

if __name__ == '__main__':
    main()
        
