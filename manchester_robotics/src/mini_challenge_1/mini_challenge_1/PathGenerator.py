import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import rclpy.qos
from std_msgs.msg import Float32 
from signal_msg.msg import SignalDecomposed 
import yaml
import time

class My_Publisher(Node):
    def __init__(self):
        super().__init__('PathGenerator')
        self.path_angle = self.create_publisher(Float32, '/path_angle', 10)
        self.path_distance = self.create_publisher(Float32, '/path_distance', 10)

        self.timer_period = 0.1
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.get_logger().info('|Controller node successfully initialized|')

        self.declare_parameter('path_num', 0)

        self.path = 0
        self.msg_angle = Float32()
        self.msg_distance = Float32()

    def timer_callback(self):
        self.path = self.get_paramater('path_num').value

        if(self.path = 1):
             self.path_angle 
    
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()