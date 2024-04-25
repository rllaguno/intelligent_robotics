import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import yaml

class My_Publisher(Node):
    def __init__(self):
        super().__init__('PointGenerator')
        self.odom = self.create_publisher(Point, '/Point', 10)
        
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_point)
        self.get_logger().info('|Point Generator node successfully initialized|')

        self.msg_point = Point()

    def timer_callback_point(self):
        self.msg_point.x = 1.0
        self.msg_point.y = 1.0
        self.msg_point.z = 1.0
        
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()