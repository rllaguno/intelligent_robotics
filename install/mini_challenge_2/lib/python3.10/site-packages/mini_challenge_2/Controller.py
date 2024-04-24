import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose2D, Point
import rclpy.qos
from std_msgs.msg import Int32
import math 

class My_Publisher(Node):
    def __init__(self):
        super().__init__('Controller')
        self.vel = self.create_publisher(Twist, '/cmd_vel', 10)
        self.flag = self.create_publisher(Int32, '/flag', 10)

        qos_profile = rclpy.qos.qos_profile_sensor_data
        self.subPose = self.create_subscription(Pose2D, "/odom", self.timer_callback_odometry, qos_profile)
        self.subPoint = self.create_subscription(Point, "/Point", self.timer_callback_point, qos_profile)
        
        self.timer_period_controller = 0.18
        self.timer_controller = self.create_timer(self.timer_period_controller, self.timer_callback_controller)
        #self.timer_PID = self.create_timer(self.timer_period_controller, self.timer_callback_PID)
        self.get_logger().info('|Controller node successfully initialized|')
        
        self.msg_vel = Twist()
        self.msg_pose = Pose2D()
        self.msg_point = Point()
        self.msg_flag = Int32()

        self.flag_counter = 0
        self.bandera = False

        ### Distance ###
        self.kpDistance = 5.2536
        self.kiDistance = 0.1922
        self.kdDistance = 4.9357

        ### Angle ###
        self.kpAngle = 0.4535
        self.kiAngle = 0.0531
        self.kdAngle = 0.3597

        #Necesitan un valor inicial ya que al usarse sin declararse antes marca error
        self.integralDistance = 0  
        self.previousErrorDistance = 0
        self.integralAngle = 0
        self.previousErrorDAngle = 0
    
    def timer_callback_controller(self):
        angleTarget = 0
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

        self.errorAngle =  angleTarget - self.msg_pose.theta 
        print("Error angle: " + str(self.errorAngle))

        if (self.errorAngle > 180):
            self.errorAngle = self.errorAngle - 360 
            
        self.errorDistance = math.hypot((abs(self.msg_pose.x)  - abs(self.msg_point.x)), (abs(self.msg_pose.y)  - abs(self.msg_point.y)))
        print("Error distance: " + str(self.errorDistance))

        ### PID DISTANCE ###
        self.proportionalDistance = self.errorDistance
        self.integralDistance = self.integralDistance + (self.errorDistance * 0.1)
        self.derivativeDistance = (self.errorDistance - self.previousErrorDistance) / 0.1
        self.previousErrorDistance = self.errorDistance
        self.pidDistance = (self.kpDistance * self.proportionalDistance) + (self.kiDistance * self.integralDistance) + (self.kdDistance * self.derivativeDistance)
        print("PID distance: " + str(self.pidDistance))

        if (self.pidDistance > 0.3 or self.pidDistance < -0.3) :
            self.msg_vel.linear.x = 0.3
            self.vel.publish(self.msg_vel) 
        else :
            self.msg_vel.linear.x = self.pidDistance
            self.vel.publish(self.msg_vel) 
        print("Linear vel: " + str(self.msg_vel.linear.x))

        ### PID ANGLE ###
        self.proportionalAngle = self.errorAngle
        self.integralAngle = self.integralAngle + (self.errorAngle * 0.1)
        self.derivativeAngle = (self.errorAngle - self.previousErrorDAngle) / 0.1
        self.previousErrorDAngle = self.errorAngle
        self.pidAngle = (self.kpAngle * self.proportionalAngle) + (self.kiAngle * self.integralAngle) + (self.kdAngle * self.derivativeAngle)
        print("PID angle: " + str(self.pidAngle))
        
        if (self.pidAngle > 0.3 or self.pidAngle < -0.3) :
            self.msg_vel.angular.z = 0.3
            self.vel.publish(self.msg_vel) 
        else:
            self.msg_vel.angular.z = self.pidAngle
            self.vel.publish(self.msg_vel) 
        print("Angular vel: " + str(self.msg_vel.angular.z)) 

        ### SEND FLAG ###
        if (self.msg_point.y != 0):
            self.bandera = True 
            
        if ((self.errorAngle < 0.05 and self.errorDistance < 0.05) and self.bandera) :
            self.flag_counter += 1
            self.msg_flag.data = self.flag_counter
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