import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32MultiArray

class SensorFusionNode(Node):

    def __init__(self):
        super().__init__('sensor_fusion_node')

        self.imu_sub = self.create_subscription(
            Imu, '/imu/data', self.imu_callback, 10)

        self.tof_sub = self.create_subscription(
            Float32MultiArray, '/tof/data', self.tof_callback, 10)

        self.pose_sub = self.create_subscription(
            Float32MultiArray, '/slam/pose', self.pose_callback, 10)

        self.latest_imu = None
        self.latest_tof = None
        self.latest_pose = None

    def imu_callback(self, msg):
        self.latest_imu = msg

    def tof_callback(self, msg):
        self.latest_tof = msg.data

    def pose_callback(self, msg):
        self.latest_pose = msg.data


def main(args=None):
    rclpy.init(args=args)
    node = SensorFusionNode()
    rclpy.spin(node)
    rclpy.shutdown()