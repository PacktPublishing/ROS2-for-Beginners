import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from math import pi

class Draw_traingle(Node):
    def __init__(self):
        super().__init__('Move_in_trangle')
        self.publisher_ = self.create_publisher(Twist,'/cmd_vel', 100)
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.triangle)
        self.get_logger().info('Robot Movement started')

    def triangle(self):
        velocity_messsage = Twist()

   
        velocity_messsage.linear.x = 0.5
        velocity_messsage.angular.z = 0.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Move forward...')
        rclpy.spin_once(self, timeout_sec=1.0)

        velocity_messsage.linear.x = 0.0
        velocity_messsage.angular.z = -pi / 3.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Turning right...')
        rclpy.spin_once(self, timeout_sec=1.0)

  
        velocity_messsage.linear.x = 0.5
        velocity_messsage.angular.z = 0.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Move forward...')
        rclpy.spin_once(self, timeout_sec=1.0)

      
        velocity_messsage.linear.x = 0.0
        velocity_messsage.angular.z = -pi / 3.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Turning right...')
        rclpy.spin_once(self, timeout_sec=1.0)

    
        velocity_messsage.linear.x = 0.5
        velocity_messsage.angular.z = 0.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Moving forward...')
        rclpy.spin_once(self, timeout_sec=1.0)

        velocity_messsage.linear.x = 0.0
        velocity_messsage.angular.z = -pi / 3.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Turning right...')
        rclpy.spin_once(self, timeout_sec=1.0)


      
        velocity_messsage.linear.x = 0.5
        velocity_messsage.angular.z = 0.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Move forward...')
        rclpy.spin_once(self, timeout_sec=1.0)


        velocity_messsage.linear.x = 0.0
        velocity_messsage.angular.z = 0.0
        self.publisher_.publish(velocity_messsage)
        self.get_logger().info('Triangle drawing completed.')

def main(args=None):
    rclpy.init(args=args)
    triangle_drawer = Draw_traingle()
    rclpy.spin(triangle_drawer)
    triangle_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
