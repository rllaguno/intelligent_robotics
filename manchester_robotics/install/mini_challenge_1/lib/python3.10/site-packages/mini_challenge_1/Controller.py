import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import yaml

class My_Publisher(Node):
    def __init__(self):
        super().__init__('Controller')
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        self.get_logger().info('|Controller node successfully initialized|')

        self.msg_vel = Twist()

    def timer_callback_controller(self):

        self.msg_vel.linear.x = 0.2
        self.vel.publish(self.msg_vel)
    
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()