import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
import rclpy.qos
from std_msgs.msg import Float32
import numpy as np

class My_Publisher(Node):
    def __init__(self):
        super().__init__('Odometry')
        self.odom = self.create_publisher(Pose2D, '/odom', 10)
        
        qos_profile = rclpy.qos.qos_profile_sensor_data
        self.subL = self.create_subscription(Float32, "/VelocityEncL", self.timer_callback_l, qos_profile)
        self.subR = self.create_subscription(Float32, "/VelocityEncR", self.timer_callback_r, qos_profile)
        
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_odometry)
        self.get_logger().info('|Odometry node successfully initialized|')

        self.r = 0.05
        self.l = 0.18
        self.left_velocity = 0
        self.right_velocity = 0
        self.msg_pose = Pose2D()

    def timer_callback_odometry(self):
        self.msg_pose.x = self.msg_pose.x + self.r * ((self.left_velocity + self.right_velocity) / 2) * np.cos(self.msg_pose.theta) * self.timer_period_controller
        self.msg_pose.y = self.msg_pose.y + self.r * ((self.left_velocity + self.right_velocity) / 2) * np.sin(self.msg_pose.theta) * self.timer_period_controller
        self.msg_pose.theta = self.msg_pose.theta + ((self.right_velocity - self.left_velocity) / self.l) * self.r * self.timer_period_controller
        self.odom.publish(self.msg_pose)

    def timer_callback_l(self,msg):
        self.left_velocity = msg.data

    def timer_callback_r(self,msg):
        self.right_velocity = msg.data
        
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()