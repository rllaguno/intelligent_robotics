import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D, Point
import rclpy.qos
from std_msgs.msg import Float32
import yaml
import math 

class My_Publisher(Node):
    def _init_(self):
        super()._init_('Controller')
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

        if ((self.msg_point.x > self.msg_pose.x) and (self.msg_point.y > self.msg_pose.y)):
            opuesto = self.msg_point.y - self.msg_pose.y
            adyacente = self.msg_point.x - self.msg_pose.x
            angleRadians = math.atan(opuesto/adyacente)
            angleTarget = math.degrees(angleRadians)

        elif ((self.msg_point.x > self.msg_pose.x) and (self.msg_point.y < self.msg_pose.y)):
            opuesto = self.msg_point.x - self.msg_pose.x
            adyacente = self.msg_pose.y - self.msg_point.y 
            angleRadians = math.atan(opuesto/adyacente)
            angleTarget = math.degrees(angleRadians) + 270

        elif ((self.msg_point.x < self.msg_pose.x) and (self.msg_point.y > self.msg_pose.y)):
            opuesto = self.msg_pose.x - self.msg_point.x
            adyacente = self.msg_point.y - self.msg_pose.y
            angleRadians = math.atan(opuesto/adyacente)
            angleTarget = math.degrees(angleRadians) + 90

        elif ((self.msg_point.x < self.msg_pose.x) and (self.msg_point.y < self.msg_pose.y)):
            opuesto = self.msg_pose.y - self.msg_point.y 
            adyacente = self.msg_pose.x - self.msg_point.x
            angleRadians = math.atan(opuesto/adyacente)
            angleTarget = math.degrees(angleRadians) + 180


        self.errorTheta =  angleTarget - self.msg_pose.theta 

        if (self.errorTheta > 180):
            self.errorTheta = self.errorTheta - 360 
            
        self.errorDistance = math.hypot((abs(self.msg_pose.x)  - abs(self.msg_point.x)), (abs(self.msg_pose.y)  - abs(self.msg_point.y)))



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

if _name_ == '_main_':
    main()