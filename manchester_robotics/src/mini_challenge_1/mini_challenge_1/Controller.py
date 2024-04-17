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

        self.desired_distance = 0
        self.desired_angle = 0

    def timer_callback_controller(self):
        self.actual_distance = self.actual_distance + (0.05 * ((self.left_velocity + self.right_velocity) / 2))
        self.actual_angle = self.actual_angle + (0.05 * ((self.left_velocity - self.right_velocity) / 0.18))

        if (self.desired_distance == 0) :
            self.msg_vel.linear.x = 0.25
            self.vel.publish(self.msg_vel)

            if (self.actual_distance == 10) :
                self.msg_vel.linear.x = 0.5 #aqui va velocidad q se ocupa para completar recoorido en tiempo q dice el usuario
                self.vel.publish(self.msg_vel)
                self.desired_distance = self.d1
                self.desired_angle = self.a1

        if (self.actual_distance == self.desired_distance) :
            self.msg_vel.linear.x = 0.25
            self.vel.publish(self.msg_vel)

        if (self.path == 0) :
            if (self.actual_distance == self.desired_distance+10) :
                self.msg_vel.linear.x = 0.0
                self.msg_vel.angular.z = 0.2
                self.vel.publish(self.msg_vel)
                if (self.actual_angle == self.desired_angle and self.actual_distance <= self.desired_distance+20 ) :
                    self.msg_vel.linear.x = 0.25
                    self.msg_vel.angular.z = 0.0
                    self.vel.publish(self.msg_vel) 
                self.msg_vel.linear.x = 0.5 #aqui va velocidad q se ocupa para completar recoorido en tiempo q dice el usuario
                self.vel.publish(self.msg_vel)
                self.desired_distance = self.d2
                self.desired_angle = self.a2


    def desired_params_callback(self,msg):
        self.path = msg.path
        self.d1 = msg.distance1
        self.d2 = msg.distance2
        self.d3 = msg.distance3
        self.d4 = msg.distance4
        self.a1 = msg.angle1
        self.a2 = msg.angle2
        self.a3 = msg.angle3
        self.a4 = msg.angle4

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