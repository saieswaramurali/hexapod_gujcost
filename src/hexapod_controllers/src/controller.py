#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber')
        #change the self.y for the adjustment of the legs 
        self.y = 20 
        self.H = 0 
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
            self.get_logger().info(f"Button pressed, self.H: {self.H}")
        elif msg.buttons[0] == 0:
            # Reset A when the button is released
            self.A = 0

                # Check the state of button[3]
        if msg.buttons[3] == 1 and self.Y == 0: 
            # Button is pressed for the first time
            if self.H < 30 : 
                self.H += 2 
            self.Y= 1  # Mark that the button has been pressed
            self.get_logger().info(f"Button pressed, self.H: {self.H}")
        elif msg.buttons[3] == 0:
            # Reset A when the button is released
            self.Y = 0

def main(args=None):
    rclpy.init(args=args)
    joy_subscriber = JoySubscriber()
    rclpy.spin(joy_subscriber)
    joy_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
