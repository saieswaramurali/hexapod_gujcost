from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    joy_package = Node(
        package='joy',
        namespace='joystick',
        executable='joy_node',
        name='sai_joystick'
    )

    return LaunchDescription([
        joy_package, 
    ])
