import rclpy 
from geometry_msgs.msg import Twist 
from rclpy.node import Node


#class called sub,that takes in all the objects we need.
class sub(Node):
    def __init__(self):
        super().__init__('move_robot_sub')
        self.command_vel_sub = self.create_subscription(Twist,'/cmd_vel',self.sub_command_velocity,10) #passed in a call_back method that subscribes to the command velocity topic.

    #subscriber to the linear velocity of x(when robot drives forward of linear of x)
    def sub_command_velocity(self,data):
        self.message = data.linear.x  #store the data message of linear of x in an object called self.messages.
        self.get_logger().info('The robot drives forward, reading linear velocity of x ,which is: "%s"' %self.message) 

#Main function
def main(args=None):
    rclpy.init(args=args)
    sub_velocity = sub()
    rclpy.spin(sub_velocity)

if __name__ == '__main__':
    main()