from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'odom_frame',
            default_value='odom'
        ),
        DeclareLaunchArgument(
            'child_frame',
            default_value='base_link'
        ),
        DeclareLaunchArgument(
            'topic',
            default_value=''
        ),
        DeclareLaunchArgument(
            'deskew',
            default_value='false'
        ),
        DeclareLaunchArgument(
            'max_range',
            default_value='100.0'
        ),
        DeclareLaunchArgument(
            'min_range',
            default_value='5.0'
        ),
        DeclareLaunchArgument(
            'voxel_size',
            default_value=''
        ),
        Node(
            package='kiss_icp',
            executable='odometry_node',
            name='odometry_node',
            output='screen',
            remappings=[
                ('pointcloud_topic', LaunchConfiguration("topic")),
            ],
            parameters=[{
                "odom_frame": LaunchConfiguration("odom_frame"),
                "child_frame": LaunchConfiguration('child_frame'),
                "max_range": LaunchConfiguration('max_range'),
                "min_range": LaunchConfiguration('min_range'),
                "deskew": LaunchConfiguration('deskew'),
                "voxel_size": LaunchConfiguration('voxel_size'),
                "frame_rate": 10,
                "max_points_per_voxel": 20,
                "initial_threshold": 2.0,
                "min_motion_th": 0.1,
            }],

        ),
    ])