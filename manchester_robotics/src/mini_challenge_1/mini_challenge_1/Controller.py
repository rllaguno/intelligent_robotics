import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32 
from signal_msg.msg import SignalDecomposed 
import yaml

class My_Publisher(Node):
    def __init__(self):
        super().__init__('Controller')
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.desired_sub = self.create_subscription(SignalDecomposed, 'desired', self.desired_params_callback, 10)
        self.timer_period_controller = 0.1
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        self.get_logger().info('|Controller node successfully initialized|')
        self.sub = self.create_subscription(Float32, "VelocityEncL", self.listener_callback_l, 10)
        self.sub = self.create_subscription(Float32, "VelocityEncR", self.listener_callback_r, 10)

        self.msg_vel = Twist()

        #self.desired_distance = 0
        #self.desired_angle = 0
    
        flagA = True
        flagD = False
        n = 0
        i = 0

        self.a = [0, 90, 180, 270]
        self.d = [200, 400, 600, 800]

    def timer_callback_controller(self):
        self.actual_distance = self.actual_distance + (0.05 * ((self.left_velocity + self.right_velocity) / 2))
        self.actual_angle = self.actual_angle + (0.05 * ((self.left_velocity - self.right_velocity) / 0.18))

        if (flagA):
            if (self.actual_angle == self.a[i]):
                self.msg_vel.angular.z = 0.0
                self.msg_vel.linear.x = 0.25
                self.vel.publish(self.msg_vel) 
                i += 1
                flagD = True
                flagA = False
            else: 
                self.msg_vel.angular.z = 0.2
                self.vel.publish(self.msg_vel)

        if (flagD):
            if (self.actual_distance >= 15 and self.actual_distance < 20):
                self.msg_vel.linear.x = 0.5 #aqui va velocidad q se ocupa para completar recorrido en tiempo q dice el usuario
                self.vel.publish(self.msg_vel)
            
            if (self.array_dd[n] -15 >= self.actual_distance and self.array_dd[n] -10 < self.actual_distance):
                self.msg_vel.linear.x = 0.25
                self.vel.publish(self.msg_vel)
            
            if (self.array_dd[n] >= self.actual_distance and self.array_dd[n] < self.actual_distance + 10):
                self.msg_vel.linear.x = 0.0
                self.vel.publish(self.msg_vel)
                flagA = True
                flagD = False
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

if __name__ == '__main__':
        main()