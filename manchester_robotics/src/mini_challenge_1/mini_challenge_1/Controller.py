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
        super().__init__('Controller')
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.desired_sub = self.create_subscription(SignalDecomposed, '/desired', self.desired_params_callback, 10)
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        self.get_logger().info('|Controller node successfully initialized|')
        
        qos_profile = rclpy.qos.qos_profile_sensor_data
        self.subL = self.create_subscription(Float32, "/VelocityEncL", self.timer_callback_l, qos_profile)
        self.subR = self.create_subscription(Float32, "/VelocityEncR", self.timer_callback_r, qos_profile)

        self.msg_vel = Twist()
    
        self.flagA = True
        self.flagD = False
        self.actual_distance = 0
        self.actual_angle = 0
        self.left_velocity = 0
        self.right_velocity = 0
        self.desdis = 2.0
        self.desang = 0

        self.i = 0
        self.n = 0

        self.a = [0, 0, 0, 0]
        self.d = [0, 0, 0, 0]
        self.path = 0

    def desired_params_callback(self,msg):
        self.path = msg.path
        print(self.path)
        self.d1 = msg.distance1
        self.d2 = msg.distance2
        self.d3 = msg.distance3
        self.d4 = msg.distance4
        self.a1 = msg.angle1
        self.a2 = msg.angle2 
        self.a3 = msg.angle3
        self.a4 = msg.angle4
        self.get_logger().info(f"Received parameters: Path={self.path}, Distances={self.d1}, {self.d2}, {self.d3}, {self.d4}, Angles={self.a1}, {self.a2}, {self.a3}, {self.a4}")

        self.a = [self.a1, self.a2, self.a3, self.a4]
        self.d = [self.d1, self.d2, self.d3, self.d4]

    def timer_callback_controller(self):

        self.actual_distance = self.actual_distance + ((0.05 * ((self.left_velocity + self.right_velocity) / 2))*0.1)
        self.actual_angle = self.actual_angle + ((0.05 * ((self.left_velocity - self.right_velocity) / 0.18))*-5.7269)
        if (self.flagA):
            print("angle")
            print(self.actual_angle)
            if (self.actual_angle <= self.a[self.i] + 5 and self.actual_angle >= self.a[self.i] - 10):
                print("parar giro")
                self.msg_vel.angular.z = 0.0
                self.flagA = False
                print("i: " )
                print(self.i)
                self.flagD = True
                print("avanzar primera vez")
                self.msg_vel.linear.x = 0.2
                self.vel.publish(self.msg_vel) 
                self.i = self.i + 1
                #if (self.i <= 4):self.i=0
            else: 
                print("girar")
                self.msg_vel.angular.z = 0.15
                self.vel.publish(self.msg_vel)

        elif (self.flagD):
            print("distance")
            print(self.actual_distance)
            self.vel.publish(self.msg_vel)
            
            if(self.actual_distance <= self.d[self.n] + .5 and self.actual_distance >= self.d[self.n]- 0.5):
                print("frenar distance")
                self.msg_vel.linear.x = 0.0
                self.vel.publish(self.msg_vel)
                self.flagA = True
                self.flagD = False
                print("n: " )
                print(self.n)
                self.n = self.n+1
                #if (self.n <= 4):self.n=0
                
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