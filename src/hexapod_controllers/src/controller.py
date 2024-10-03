#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber')
        #change the self.y for the adjustment of the legs 
        self.L1 = 5.2
        self.L2 = 9.2
        self.L3 = 15.5
        self.leg_spread = self.L1 + self.L2
        self.straide_length = 8 # straide length of the robot
        self.RB = 0
        self.LB = 0
        self.X = 0  
        self.B = 0 
        self.H = 0 # height of the hexapod robot
        self.Y = 0 
        self.A = 0
        self.subscription = self.create_subscription(
            Joy,
            '/joystick/joy',  # Ensure this matches your joystick's topic
            self.joy_callback,
            10)
        self.subscription  # prevent unused variable warning

    def forward_kinematics(self) :
        pass


    def inverse_kinematics(self) : 
        pass

    def joy_callback(self, msg):
            # Check the state of button[0]
        if msg.buttons[0] == 1 and self.A == 0: 
            # Button is pressed for the first time
            if self.H > 0 : 
                self.H -= 2 
            self.A = 1  # Mark that the button has been pressed
            self.get_logger().info(f"Button pressed, self.height: {self.H}")
        elif msg.buttons[0] == 0:
            # Reset A when the button is released
            self.A = 0

            # Check the state of button[3]
        if msg.buttons[3] == 1 and self.Y == 0: 
            # Button is pressed for the first time
            if self.H < 30 : 
                self.H += 2 
            self.Y = 1  # Mark that the button has been pressed
            self.get_logger().info(f"Button pressed, self.height: {self.H}")
        elif msg.buttons[3] == 0:
            # Reset A when the button is released
            self.Y = 0

            # Check the state of button[1], for leg_spread positive 
        if msg.buttons[1] == 1 and self.B == 0: 
            # Button is pressed for the first time
            if self.leg_spread < (self.L1 + self.L2 + self.L3) : 
                self.leg_spread += 2 
            self.B = 1  # Mark that the button has been pressed
            self.get_logger().info(f"Button pressed, self.leg_spread: {self.leg_spread}")
        elif msg.buttons[1] == 0:
            # Reset A when the button is released
            self.B = 0


            # Check the state of button[2], for leg_spread positive 
        if msg.buttons[2] == 1 and self.X == 0: 
            # Button is pressed for the first time
            if self.leg_spread > (self.L1 + self.L2 ) : 
                self.leg_spread -= 2 
            self.X = 1  # Mark that the button has been pressed
            self.get_logger().info(f"Button pressed, self.leg_spread: {self.leg_spread}")
        elif msg.buttons[2] == 0:
            # Reset A when the button is released
            self.X = 0

        if msg.buttons[5] == 1 and self.RB == 0: 
            if self.straide_length < 15 : 
                self.straide_length += 1 
            self.RB = 1 
            self.get_logger().info(f"Button pressed, self.straide_length: {self.straide_length}")
        elif msg.buttons[5] == 0: 
            self.RB = 0 


        if msg.buttons[4] == 1 and self.LB == 0: 
            if self.straide_length > 0 : 
                self.straide_length -= 1 
            self.LB = 1 
            self.get_logger().info(f"Button pressed, self.straide_length: {self.straide_length}")
        elif msg.buttons[4] == 0: 
            self.LB = 0 

        



def main(args=None):
    rclpy.init(args=args)
    joy_subscriber = JoySubscriber()
    rclpy.spin(joy_subscriber)
    joy_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
