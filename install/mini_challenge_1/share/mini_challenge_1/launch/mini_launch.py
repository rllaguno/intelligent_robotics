import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('mini_challenge_1'),
            'config',
            'params.yaml'
    )

    controller_node = Node(
        package='mini_challenge_1',
        executable='Controller',
        output='screen',
    )

    path_generator_node = Node(
        package='mini_challenge_1',
        executable='PathGenerator',
        output='screen',
        parameters=[config],
    )

    l_d = LaunchDescription([controller_node, path_generator_node])
    return l_d