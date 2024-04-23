import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D, Point
import rclpy.qos
from std_msgs.msg import Int32
import math 

class My_Publisher(Node):
    def _init_(self):
        super().__init__('Controller')
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.flag = self.create_publisher(Int32, '/flag', 10)
        
        qos_profile = rclpy.qos.qos_profile_sensor_data
        #Odometry es nuestro actual
        self.subPose = self.create_subscription(Pose2D, "/odom", self.timer_callback_odometry, qos_profile)
        #Point es nuestro deseado
        self.subPoint = self.create_subscription(Point, "/Point", self.timer_callback_point, qos_profile)
        
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        self.get_logger().info('|Controller node successfully initialized|')
        
        self.msg_vel = Twist()
        self.msg_pose = Pose2D() # actual
        self.msg_point = Point() # deseado
        self.msg_flag = Int32()
        #create a counter for msg_flag
        self.flag_counter = 0
        
    def timer_callback_controller(self):
        self.get_logger().info(self.flag_counter)

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

        if self.errorDistance < 0.05: 
            self.flag_counter += 1
            self.get_logger().info(self.msg_flag)

        self.msg_vel.linear.x = 0.0
        self.msg_vel.angular.z = 0.0

        self.msg_flag = self.flag_counter
        self.vel.publish(self.msg_vel)
        self.flag.publish(self.msg_flag)


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