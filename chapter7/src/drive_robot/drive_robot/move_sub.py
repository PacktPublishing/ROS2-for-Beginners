import rclpy 
from geometry_msgs.msg import Twist 
from rclpy.node import Node
class sub(Node):
    def __init__(self):
        super().__init__('move_robot_sub')
        self.command_vel_sub = self.create_subscription(Twist,'/cmd_vel',self.sub_command_velocity,10) 

    def sub_command_velocity(self,data):
        self.message = data.linear.x  
        self.get_logger().info('The robot drives forward, reading linear velocity of x ,which is: "%s"' %self.message) 

def main(args=None):
    rclpy.init(args=args)
    sub_velocity = sub()
    rclpy.spin(sub_velocity)

if __name__ == '__main__':
    main()