import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32MultiArray
from kalman_filter import KalmanFilter

class FusionNode(Node):

    def __init__(self):
        super().__init__('fusion_node')

        self.kf = KalmanFilter()

        self.imu_sub = self.create_subscription(Imu, '/imu/data', self.imu_cb, 10)
        self.tof_sub = self.create_subscription(Float32MultiArray, '/tof/data', self.tof_cb, 10)
        self.pose_sub = self.create_subscription(Float32MultiArray, '/slam/pose', self.pose_cb, 10)

        self.pub = self.create_publisher(Float32MultiArray, '/corrected_pose', 10)

        self.imu = None
        self.tof = None
        self.pose = None

    def imu_cb(self, msg):
        self.imu = msg.linear_acceleration.x

    def tof_cb(self, msg):
        self.tof = msg.data[0]

    def pose_cb(self, msg):
        self.pose = msg.data

        if self.imu is None or self.tof is None:
            return

        self.kf.predict(self.imu)
        corrected = self.kf.update(self.pose, self.tof)

        out = Float32MultiArray()
        out.data = [float(corrected[0]), float(corrected[1])]

        self.pub.publish(out)


def main(args=None):
    rclpy.init(args=args)
    node = FusionNode()
    rclpy.spin(node)
    rclpy.shutdown()