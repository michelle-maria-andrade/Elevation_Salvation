import airsim
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
import struct
import numpy as np

class AirSimLidarPublisher(Node):
    def __init__(self):
        super().__init__('airsim_lidar_publisher')

        self.publisher_ = self.create_publisher(PointCloud2, 'airsim/pointcloud', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  

        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

        self.lidar_name = 'Lidar1'

        self.get_logger().info('AirSim Lidar publisher initialized.')

    def timer_callback(self):
        lidar_data = self.client.getLidarData(lidar_name=self.lidar_name)

        if len(lidar_data.point_cloud) < 3:
            self.get_logger().warn('No points received from Lidar')
            return

        points = np.array(lidar_data.point_cloud, dtype=np.float32).reshape(-1, 3)
        msg = self.create_pointcloud2(points)
        self.publisher_.publish(msg)

    def create_pointcloud2(self, points):
        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = 'odom'

        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1)
        ]

        data = b''.join([struct.pack('fff', *point) for point in points])
        pointcloud_msg = PointCloud2()
        pointcloud_msg.header = header
        pointcloud_msg.height = 1
        pointcloud_msg.width = len(points)
        pointcloud_msg.fields = fields
        pointcloud_msg.is_bigendian = False
        pointcloud_msg.point_step = 12
        pointcloud_msg.row_step = pointcloud_msg.point_step * pointcloud_msg.width
        pointcloud_msg.is_dense = True
        pointcloud_msg.data = data

        return pointcloud_msg

def main(args=None):
    rclpy.init(args=args)
    node = AirSimLidarPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
