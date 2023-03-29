'''
   Distance travelled by robot,sending velocity command to the wheel of the robot after reaching a certain distance.
'''
import rclpy 
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry 
from rclpy.node import Node 



class distance_travelled(Node):
    def __init__(self):
        super().__init__("distance_travelled")
        self.pub = self.create_publisher(Twist,'/cmd_vel',100)
        self.callback_odometry = self.create_subscription(Odometry,'/odom',self.callback_odom,10)
        self.forward = 0.2
        self.stop = 0.0
        self.angular_right = 0.2
        self.angular_left = 0.2
        self.velocity_message = Twist()
        self.distance = 0.0


    def callback_odom(self,msg):
        self.message_odom_x = msg.pose.pose.position.x
        self.message_orientation_y = msg.pose.pose.orientation.y
        self.message_orientation_z = msg.pose.pose.position.z 
        self.get_logger().info('The distance travelled by x is: "%s"' %self.message_odom_x)
        self.get_logger().info('The orientation of the robot at y is: "%s"' %self.message_orientation_y)
        self.get_logger().info('The orientation of the robot at z is: "%s"' %self.message_orientation_z)
        self.move_forward()
        for x in range (1,100):
        #loop through and check if the distance travelled is > 2m
            if self.message_odom_x > 2.950:
                    self.stopp()
                    #self.turn_right()
            
        
    #move_forward.
    def move_forward(self):
        self.velocity_message.linear.x = self.forward
        self.pub.publish(self.velocity_message)
        self.get_logger().info("The robot moves forward at velocity speed of:" + str(self.forward))

    #robot_stop.
    def stopp(self):
        self.velocity_message.linear.x = self.stop
        self.pub.publish(self.velocity_message)
        self.get_logger().info("The robot stops at velocity speed of:" + str(self.stop))

    #turn_right.
    def turn_right(self):
        self.velocity_message.angular.z = -self.angular_left
        self.pub.publish(self.velocity_message)
        self.get_logger().info("The robot turns right at velocity speed of:" + str(-self.angular_left))
       
    #turn_left.
    def turn_left(self):
        self.velocity_message.angular.z = self.angular_left
        self.pub.publish(self.velocity_message)
        self.get_logger().info("The robot turns left at velocity speed of:"+ str(self.angular_left))


def main(args=None):
    rclpy.init(args=args)
    speed = distance_travelled()
    rclpy.spin(speed)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


