import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D, Point
import rclpy.qos
from std_msgs.msg import Float32
import yaml

class My_Publisher(Node):
    def __init__(self):
        super().__init__('Controller')
        self.odom = self.create_publisher(Twist, '/cmd_vel', 10)
        
        qos_profile = rclpy.qos.qos_profile_sensor_data
        self.subPose = self.create_subscription(Pose2D, "/odom", self.timer_callback_odometry, qos_profile)
        self.subPoint = self.create_subscription(Point, "/Point", self.timer_callback_point, qos_profile)
        
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        self.get_logger().info('|Controller node successfully initialized|')
        
        self.msg_vel = Twist()
        self.msg_pose = Pose2D()
        self.msg_point = Point()
    
    def timer_callback_controller(self):
        self.msg_vel.linear.x = 0.0
        self.msg_vel.angular.z = 0.0

    def timer_callback_odometry(self, msg):
        self.msg_pose.x = msg.x
        self.msg_pose.y = msg.y
        self.msg_pose.theta = msg.theta
    
    def timer_callback_point(self, msg):
        self.msg_point.x = msg.x
        self.msg_point.y = msg.y
        self.msg_point.z = msg.z
        
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()