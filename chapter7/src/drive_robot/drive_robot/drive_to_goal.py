import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
import action_msgs.msg as action_msgs

class ToGoalNode(Node):
    def __init__(self):
        super().__init__('Drive_robot_to_goal')

        self.goal_pose_publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.navigation_action_client = self.create_client(NavigateToPose, '/pose_navigation')

        while not self.navigation_action_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Nav action not avaialable.....')

        self.navigation_goal_handle = None

    def navigate_to_goal(self, future):
        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Navigation goal rejected')
            return

        self.get_logger().info('Navigation goal accepted')

        while True:
            #Let's check if the goal has been reached.
            status = goal_handle.get_status()

            if status == action_msgs.GoalStatus.STATUS_SUCCEEDED:
                self.get_logger().info('Navigation goal reached')
                break
            elif status == action_msgs.GoalStatus.STATUS_ABORTED:
                self.get_logger().info('Navigation goal aborted')
                break

            rclpy.spin_once(self)
            
        goal_handle.destroy()


    def goal_sent(self, x, y, theta):
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.pose.position.x = x
        goal_pose.pose.position.y = y
        goal_pose.pose.orientation.z = theta

       
        self.goal_pose_publisher.publish(goal_pose)

        # Send a navigation goal to the Navigation2 stack
        navigation_goal_msg = NavigateToPose.Goal()
        navigation_goal_msg.pose = goal_pose
        navigation_goal_msg.behavior_tree = 'navigate_w_replanning'

        self.navigation_action_client.wait_for_server()

        self.navigation_goal_handle = self.navigation_action_client.send_goal_async(navigation_goal_msg)
        self.navigation_goal_handle.add_done_callback(self.navigation_goal_response_callback)

def main(args=None):
    rclpy.init(args=args)
    drive_to_goal_node = ToGoalNode()
    drive_to_goal_node.send_goal(1.0, 2.0, 0.0)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
