#!/usr/bin/env python3
# acts as the high level controller for robot. 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray  # Import the Float32MultiArray message type
from kinematics import stand_up, sit_down

class JoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber')
        # Parameters for the leg adjustment
        self.mode = 0 # to select between sit stand or walk 
        self.L1 = 5.2
        self.L2 = 9.2
        self.L3 = 15.5
        self.leg_spread = self.L1 + self.L2
        self.straide_length = 8  # Stride length of the robot
        self.RB = 0
        self.LB = 0
        self.X = 0  
        self.B = 0 
        self.H = 0  # Height of the hexapod robot
        self.Y = 0 
        self.A = 0
        self.select = 0

        # Joystick subscription
        self.subscription = self.create_subscription(
            Joy,
            '/joystick/joy',  # Ensure this matches your joystick's topic
            self.joy_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Servo angles publisher
        self.servo_publisher = self.create_publisher(
            Float32MultiArray, 
            'servo_angles', 
            10)
        
    def publish_servo_angles(self, angles):
        msg = Float32MultiArray()
        msg.data = [0.0] * 18  # Initialize with 18 zeros or any default values
        
        # Now set individual elements based on your angles
        for i in range(18):
            msg.data[i] = angles[i]
        
        self.servo_publisher.publish(msg)
        self.get_logger().info(f"Published servo angles: {msg.data}")

    def stand(self):
        angles = stand_up() 
        self.publish_servo_angles(angles) 


    def sit(self):
        angles = sit_down()
        self.publish_servo_angles(angles)

    def generate_parabola(self):
        pass

    def inverse_kinematics(self):
        # Here you should calculate the servo angles (dummy values for now)
        angles = [0.0] * 18  # Replace with actual inverse kinematics calculation
        return angles



    def joy_callback(self, msg):
        # create stand, sit and walk functions using select button index 10, 
        # intitalise with sit, then stand then walk, 
        # Process joystick inputs
        if msg.buttons[10] == 1 and self.select == 0: 
            self.mode = (self.mode + 1) % 3 
            self.select = 1
            self.get_logger().info(f"Button pressed, self.height: {self.mode}")
        elif msg.buttons[10] == 0:
            self.select = 0

        if self.mode == 0 : 
            self.sit()
        
        if self.mode == 1 : 
            self.stand()
        
        if self.mode == 2 : 
            if msg.buttons[0] == 1 and self.A == 0: 
                if self.H > 0: 
                    self.H -= 2
                self.A = 1
                self.get_logger().info(f"Button pressed, self.height: {self.H}")
            elif msg.buttons[0] == 0:
                self.A = 0

            if msg.buttons[4] == 1 and self.Y == 0: 
                if self.H < 30: 
                    self.H += 2
                self.Y = 1
                self.get_logger().info(f"Button pressed, self.height: {self.H}")
            elif msg.buttons[4] == 0:
                self.Y = 0

            if msg.buttons[1] == 1 and self.B == 0: 
                if self.leg_spread < (self.L1 + self.L2 + self.L3): 
                    self.leg_spread += 2
                self.B = 1
                self.get_logger().info(f"Button pressed, self.leg_spread: {self.leg_spread}")
            elif msg.buttons[1] == 0:
                self.B = 0

            if msg.buttons[3] == 1 and self.X == 0: 
                if self.leg_spread > (self.L1 + self.L2): 
                    self.leg_spread -= 2
                self.X = 1
                self.get_logger().info(f"Button pressed, self.leg_spread: {self.leg_spread}")
            elif msg.buttons[3] == 0:
                self.X = 0

            if msg.buttons[7] == 1 and self.RB == 0: 
                if self.straide_length < 15: 
                    self.straide_length += 1
                self.RB = 1
                self.get_logger().info(f"Button pressed, self.straide_length: {self.straide_length}")
            elif msg.buttons[7] == 0: 
                self.RB = 0

            if msg.buttons[6] == 1 and self.LB == 0: 
                if self.straide_length > 0: 
                    self.straide_length -= 1
                self.LB = 1
                self.get_logger().info(f"Button pressed, self.straide_length: {self.straide_length}")
            elif msg.buttons[6] == 0: 
                self.LB = 0

        # Publish servo angles after processing joystick inputs
            # Dummy angles for testing
        #self.stand()


def main(args=None):
    rclpy.init(args=args)
    joy_subscriber = JoySubscriber()
    rclpy.spin(joy_subscriber)
    joy_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
