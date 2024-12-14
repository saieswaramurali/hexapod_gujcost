from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    joy_node = Node(
        package='joy',
        namespace='joystick',
        executable='joy_node',
        name='sai_joystick',
        output='screen'
    )

    joystick_mapper_node = Node(
        package='hexapod_controller',  # Replace with your package name
        executable='joystick_mapper',  # Replace with your node executable name
        name='joystick_mapper',
        output='screen'
    )

    return LaunchDescription([
        joy_node,
        joystick_mapper_node,
    ])
