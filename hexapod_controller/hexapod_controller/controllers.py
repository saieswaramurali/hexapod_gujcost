#!/usr/bin/env python3
# acts as the high level controller for robot. 
import math 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Vector3

class JoystickMapper(Node):
    def __init__(self):
        super().__init__('joystick_mapper')
        self.subscription = self.create_subscription(
            Joy,
            '/joystick/joy',  # Updated to match the actual topic
            self.joy_callback,
            10)
        self.publisher = self.create_publisher(Vector3, 'joystick_direction', 10)
        self.get_logger().info("Joystick Mapper Node Initialized")

    def joy_callback(self, msg: Joy):
        # Get X and Y values from the joystick axes
        x = msg.axes[0]  # Assuming the X axis is at index 0
        y = msg.axes[1]  # Assuming the Y axis is at index 1

        # Calculate magnitude
        magnitude = (x**2 + y**2)**0.5

        # Calculate direction in degrees
        direction = (math.atan2(-y, x) * 180.0 / math.pi)% 360.0
        direction = ( direction + 180 ) % 360.0

        # Log the values
        self.get_logger().info(f"Magnitude: {magnitude:.2f}, Direction: {direction:.2f}°")

        # Publish the values
        output = Vector3()
        output.x = magnitude
        output.y = direction
        output.z = 0.0  # Unused, but can be extended for additional data
        self.publisher.publish(output)

def main(args=None):
    rclpy.init(args=args)
    node = JoystickMapper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    import math
    main()
