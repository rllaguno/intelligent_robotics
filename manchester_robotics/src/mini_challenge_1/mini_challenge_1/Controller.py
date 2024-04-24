import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import rclpy.qos
from std_msgs.msg import Float32 
from signal_msg.msg import SignalDecomposed 
import yaml
import time

class My_Publisher(Node):
    def _init_(self):
        super()._init_('Controller')
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10)
        #self.desired_sub = self.create_subscription(SignalDecomposed, 'desired', self.desired_params_callback, 10)
        self.timer_period_controller = 0.18
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        self.get_logger().info('|Controller node successfully initialized|')
        
        qos_profile = rclpy.qos.qos_profile_sensor_data
        self.subL = self.create_subscription(Float32, "/VelocityEncL", self.timer_callback_l, qos_profile)
        self.subR = self.create_subscription(Float32, "/VelocityEncR", self.timer_callback_r, qos_profile)

        self.msg_vel = Twist()

        #self.desired_distance = 0
        #self.desired_angle = 0
    
        self.flagA = True
        self.flagD = False
        self.actual_distance = 0
        self.actual_angle = 0
        self.left_velocity = 0
        self.right_velocity = 0


        self.a = [0, 90, 180, 270]
        self.d = [2.0, 4.0, 6.0, 8.0]

    def timer_callback_controller(self):

        self.actual_distance = self.actual_distance + ((0.05 * ((self.left_velocity + self.right_velocity) / 2))*0.18)
        self.actual_angle = self.actual_angle + ((0.05 * ((self.left_velocity - self.right_velocity) / 0.18))*-10.30842)
        #print(self.actual_distance)
        i=0
        n=0
        
        if (self.flagA):
            print("angle")
            print(self.actual_angle)
            if (self.actual_angle <= self.a[i]+5 and self.actual_angle >= self.a[i]-10):
                print("parar giro")
                self.msg_vel.angular.z = 0.0
                self.flagA = False
                i += 1
                self.flagD = True
                print("avanzar primera vez")
                self.msg_vel.linear.x = 0.2
                self.vel.publish(self.msg_vel) 
            else: 
                print("girar")
                self.msg_vel.angular.z = 0.2
                self.vel.publish(self.msg_vel)

        if (self.flagD):
            print("distance")
            print(self.actual_distance)
            self.vel.publish(self.msg_vel)
            
            if (self.d[n] >= self.actual_distance and self.d[n] < self.actual_distance + 0.10):
                print("frenar distance")
                self.msg_vel.linear.x = 0.0
                self.vel.publish(self.msg_vel)
                self.flagA = True
                self.flagD = False
                n += 1

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

if _name_ == '_main_':
        main()