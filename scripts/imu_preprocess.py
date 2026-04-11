import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import smbus2
import time

# MPU6050 Registers
MPU_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

bus = smbus2.SMBus(1)

# Wake up MPU6050
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU_ADDR, addr)
    low = bus.read_byte_data(MPU_ADDR, addr + 1)
    value = (high << 8) | low

    if value > 32768:
        value = value - 65536
    return value

class ImuPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')
        self.publisher_ = self.create_publisher(Imu, '/imu/data', 10)
        self.timer = self.create_timer(0.05, self.publish_imu)  # 20 Hz

    def publish_imu(self):
        msg = Imu()

        # Timestamp
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "imu_link"

        # Read raw data
        acc_x = read_raw_data(ACCEL_XOUT_H)
        gyro_x = read_raw_data(GYRO_XOUT_H)

        # Convert to proper units
        acc_x = acc_x / 16384.0     # g
        gyro_x = gyro_x / 131.0     # deg/s

        # Fill ONLY X-axis values
        msg.linear_acceleration.x = acc_x
        msg.linear_acceleration.y = 0.0
        msg.linear_acceleration.z = 0.0

        msg.angular_velocity.x = gyro_x
        msg.angular_velocity.y = 0.0
        msg.angular_velocity.z = 0.0

        # Ignore orientation (not available)
        msg.orientation_covariance[0] = -1

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImuPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()