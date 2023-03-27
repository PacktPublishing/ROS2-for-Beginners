import rclpy 
from geometry_msgs.msg import Twist 
from rclpy.node import Node


class Move(Node):
    def __init__(self):
        super().__init__("move_robot") 
        self.pub = self.create_publisher(Twist,"/cmd_vel",1000) 
        self.velocity_message = Twist() 
        self.msg = "The robot is driving forward" 
        self.time = 0.05 
        self.timer = self.create_timer(self.time,self.velocity_direction)

    def velocity_direction(self):
        self.velocity_message.linear.x = 0.2
        self.pub.publish(self.velocity_message) 
        print(self.msg)

def main(args=None):
    rclpy.init(args=args)
    move = Move() 
    move.velocity_direction()
    rclpy.spin(move) 
  

if __name__ == '__main__':
    main()




