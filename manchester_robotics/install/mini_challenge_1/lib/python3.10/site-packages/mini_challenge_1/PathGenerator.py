import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32, Int32, Bool
import yaml 
from signal_msg.msg import SignalDecomposed 

class My_Publisher(Node):
    def __init__(self):
        super().__init__('PathGenerator')
        self.vel = self.create_publisher(Twist, '/pose', 10)
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback)
        self.desired_msg = SignalDecomposed()
        self.desired_pub = self.create_publisher(SignalDecomposed, '/desired', 10)
        self.get_logger().info('|PathGenerator node successfully initialized|')

        self.path = 0
        self.t = 0.0
        self.vel = 0.0

        # Parameters from yaml

        self.declare_parameters(
            namespace='',
            parameters=[
                ('path_num', rclpy.Parameter.Type.INTEGER),
                ('no_path.point_1.distance', rclpy.Parameter.Type.DOUBLE), 
                ('no_path.point_1.angle', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_1.distance', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_1.angle', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_2.distance', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_2.angle', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_3.distance', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_3.angle', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_4.distance', rclpy.Parameter.Type.DOUBLE), 
                ('square.point_4.angle', rclpy.Parameter.Type.DOUBLE), 
                ('triangle.point_1.distance', rclpy.Parameter.Type.DOUBLE), 
                ('triangle.point_1.angle', rclpy.Parameter.Type.DOUBLE), 
                ('triangle.point_2.distance', rclpy.Parameter.Type.DOUBLE), 
                ('triangle.point_2.angle', rclpy.Parameter.Type.DOUBLE), 
                ('triangle.point_3.distance', rclpy.Parameter.Type.DOUBLE), 
                ('triangle.point_3.angle', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_1.distance', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_1.angle', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_2.distance', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_2.angle', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_3.distance', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_3.angle', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_4.distance', rclpy.Parameter.Type.DOUBLE), 
                ('zigzag.point_4.angle', rclpy.Parameter.Type.DOUBLE), 
            ]
        )

    def timer_callback(self):
        #self.flag = self.subFlag.data
        self.path = self.get_parameter('path_num').get_parameter_value().integer_value
        if self.path == 1:
            #self.get_logger().info('square')
            self.desired_msg.distance1 = self.get_parameter('square.point_1.distance').get_parameter_value().double_value
            self.desired_msg.distance2 = self.get_parameter('square.point_2.distance').get_parameter_value().double_value
            self.desired_msg.distance3 = self.get_parameter('square.point_3.distance').get_parameter_value().double_value
            self.desired_msg.distance4 = self.get_parameter('square.point_4.distance').get_parameter_value().double_value
            self.desired_msg.angle1 = self.get_parameter('square.point_1.angle').get_parameter_value().double_value
            self.desired_msg.angle2 = self.get_parameter('square.point_2.angle').get_parameter_value().double_value
            self.desired_msg.angle3 = self.get_parameter('square.point_3.angle').get_parameter_value().double_value
            self.desired_msg.angle4 = self.get_parameter('square.point_4.angle').get_parameter_value().double_value
            self.publsished = self.desired_pub.publish(self.desired_msg)
            print(self.publsished)

        elif self.path == 2:
            #self.get_logger().info('square')
            self.desired_msg.distance1 = self.get_parameter('triangle.point_1.distance').get_parameter_value().double_value
            self.desired_msg.distance2 = self.get_parameter('triangle.point_2.distance').get_parameter_value().double_value
            self.desired_msg.distance3 = self.get_parameter('triangle.point_3.distance').get_parameter_value().double_value
            self.desired_msg.angle1 = self.get_parameter('triangle.point_1.angle').get_parameter_value().double_value
            self.desired_msg.angle2 = self.get_parameter('triangle.point_2.angle').get_parameter_value().double_value
            self.desired_msg.angle3 = self.get_parameter('triangle.point_3.angle').get_parameter_value().double_value
            self.desired_pub.publish(self.desired_msg)

        elif self.path == 3:
            #self.get_logger().info('square')
            self.desired_msg.distance1 = self.get_parameter('zigzag.point_1.distance').get_parameter_value().double_value
            self.desired_msg.distance2 = self.get_parameter('zigzag.point_2.distance').get_parameter_value().double_value
            self.desired_msg.distance3 = self.get_parameter('zigzag.point_3.distance').get_parameter_value().double_value
            self.desired_msg.distance4 = self.get_parameter('zigzag.point_4.distance').get_parameter_value().double_value
            self.desired_msg.angle1 = self.get_parameter('zigzag.point_1.angle').get_parameter_value().double_value
            self.desired_msg.angle2 = self.get_parameter('zigzag.point_2.angle').get_parameter_value().double_value
            self.desired_msg.angle3 = self.get_parameter('zigzag.point_3.angle').get_parameter_value().double_value
            self.desired_msg.angle4 = self.get_parameter('zigzag.point_4.angle').get_parameter_value().double_value
            self.desired_pub.publish(self.desired_msg)
        else:
            self.desired_msg.distance1 = 0.0
            self.desired_msg.distance2 = 0.0
            self.desired_msg.distance3 = 0.0
            self.desired_msg.distance4 = 0.0
            self.desired_msg.angle1 = 0.0
            self.desired_msg.angle2 = 0.0
            self.desired_msg.angle3 = 0.0
            self.desired_msg.angle4 = 0.0
    
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
