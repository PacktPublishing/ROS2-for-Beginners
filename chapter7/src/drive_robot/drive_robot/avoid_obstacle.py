import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
# from nav_msgs.msg import Odometry

class obstacle(Node):
    def __init__(self):
        super().__init__("avoidance_node")
        self.pub = self.create_publisher(Twist,'/cmd_vel',100)
        self.sub_laser = self.create_subscription(LaserScan,'/scan',self.callback_laser,100)
        #self.sub_odometry = self.create_subscription(Odometry,'/odom',self.call_back_odom,100)
        self.velocity_message = Twist()
        self.turn_lefft = 0.2
        self.forward = 0.2
        self.stop = 0.0
        self.turn_right = 0.2
        
        
   #Drive the robot.
    def movement(self):
        print("The speed of the robot is",self.forward)
        self.velocity_message.linear.x = self.forward   
        self.pub.publish(self.velocity_message)

    def callback_laser(self,msg):
        self.get_logger().info('laser_scan ranges is: "%s"' % msg.ranges[100])

        #let's make the robot keep driving forward,the robot stops when it senses an obstacle.
        self.velocity_message.linear.x = self.forward
        self.pub.publish(self.velocity_message)
        #check if there is an obstacle at the front of the robot,then sending stop to the robot.
        for x in msg.ranges:
            if msg.ranges[100] < 1.88:
                self.velocity_message.linear.x = self.stop
                self.pub.publish(self.velocity_message)

            if msg.ranges[100] == 'inf':
                self.velocity_message.linear.x = self.turn_right
                self.pub.publish(self.velocity_message)

            while msg.ranges[100] < 1.88:
                self.velocity_message.angular.z = self.turn_right
                self.pub.publish(self.velocity_message)
                break
    
    #turn left 
    def turn_left(self):
        self.velocity_message.angular.z = -(self.turn_lefft)
        self.pub.publish(self.velocity_message)
        print("The robot is turning left")
    
    #speed incresed while the robot turn right
    def increased_speed_right(self):
        self.velocity_message.angular = self.turn_right + 0.2 
        self.pub.publish(self.velocity_message)
        print("The robot turns right with an incresed speed of " + str(0.2))

    #stop the robot.
    def stopp(self):
        self.velocity_message.linear.x = self.stop
        self.pub.publish(self.velocity_message)
        print("The robot has stopped")
            
                
#main function.
def main(args=None):
    rclpy.init(args=args)
    store = obstacle()
    #store.movement()
    rclpy.spin(store)


if __name__ == '__main__':
    main()


        
