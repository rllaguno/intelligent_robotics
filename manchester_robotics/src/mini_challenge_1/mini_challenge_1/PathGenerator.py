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
        self.subFlag = self.create_subscription(Bool, '/flag', self.check_flag_callback, 10)
        self.timer_period_controller = 0.1
        self.timer_period_publisher = 1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback)
        self.get_logger().info('|Controller node successfully initialized|')

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

        self.desired_msg = SignalDecomposed()
        self.desired_pub = self.create_publisher(SignalDecomposed, '/desired', 10)
        self.signal_timer = self.create_timer(self.timer_period_publisher, self.timer_callback_publisher)

    def timer_callback(self):
        #self.flag = self.subFlag.data
        self.path = self.get_parameter('path_num').get_parameter_value().integer_value


        if self.path == 0:
            #self.get_logger().info('default')
            self.d1 = self.get_parameter('square.point_1.distance').get_parameter_value().double_value
            self.d2 = self.get_parameter('square.point_2.distance').get_parameter_value().double_value
            self.d3 = self.get_parameter('square.point_3.distance').get_parameter_value().double_value
            self.d4 = self.get_parameter('square.point_4.distance').get_parameter_value().double_value
            self.a1 = self.get_parameter('square.point_1.angle').get_parameter_value().double_value
            self.a2 = self.get_parameter('square.point_2.angle').get_parameter_value().double_value
            self.a3 = self.get_parameter('square.point_3.angle').get_parameter_value().double_value
            self.a4 = self.get_parameter('square.point_4.angle').get_parameter_value().double_value

        elif self.path == 1:
            #self.get_logger().info('square')
            self.d1 = self.get_parameter('triangle.point_1.distance').get_parameter_value().double_value
            self.d2 = self.get_parameter('triangle.point_2.distance').get_parameter_value().double_value
            self.d3 = self.get_parameter('triangle.point_3.distance').get_parameter_value().double_value
            self.a1 = self.get_parameter('triangle.point_1.angle').get_parameter_value().double_value
            self.a2 = self.get_parameter('triangle.point_2.angle').get_parameter_value().double_value
            self.a3 = self.get_parameter('triangle.point_3.angle').get_parameter_value().double_value
        elif self.path == 2:
            #self.get_logger().info('square')
            self.d1 = self.get_parameter('zigzag.point_1.distance').get_parameter_value().double_value
            self.d2 = self.get_parameter('zigzag.point_2.distance').get_parameter_value().double_value
            self.d3 = self.get_parameter('zigzag.point_3.distance').get_parameter_value().double_value
            self.d4 = self.get_parameter('zigzag.point_4.distance').get_parameter_value().double_value
            self.a1 = self.get_parameter('zigzag.point_1.angle').get_parameter_value().double_value
            self.a2 = self.get_parameter('zigzag.point_2.angle').get_parameter_value().double_value
            self.a3 = self.get_parameter('zigzag.point_3.angle').get_parameter_value().double_value
            self.a4 = self.get_parameter('zigzag.point_4.angle').get_parameter_value().double_value
        
    
    def timer_callback_publisher(self):
        self.desired_msg.path = self.path
        self.desired_msg.distance1 = self.d1
        self.desired_msg.distance2 = self.d2
        self.desired_msg.distance3 = self.d3
        self.desired_msg.distance4 = self.d4
        self.desired_msg.angle1 = self.a1
        self.desired_msg.angle2 = self.a2
        self.desired_msg.angle3 = self.a3
        self.desired_msg.angle4 = self.a4
        self.desired_pub.publish(self.desired_msg)



    def check_flag_callback(self):
        self.flag = self.subFlag.data

    
def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
