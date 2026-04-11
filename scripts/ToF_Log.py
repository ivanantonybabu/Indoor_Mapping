import time
import board
import busio
import csv
from adafruit_vl53l0x import VL53L0X

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize sensors (different addresses)
sensor1 = VL53L0X(i2c, address=0x29)
sensor2 = VL53L0X(i2c, address=0x30)

# Open CSV file
file = open("tof_data.csv", mode="w", newline="")
writer = csv.writer(file)

# Write header
writer.writerow(["timestamp", "tof1_mm", "tof2_mm"])

print("Logging ToF data... Press Ctrl+C to stop")

try:
    while True:
        timestamp = time.time()

        dist1 = sensor1.range  # in mm
        dist2 = sensor2.range

        writer.writerow([timestamp, dist1, dist2])

        print(f"{timestamp:.2f} | {dist1} mm | {dist2} mm")

        time.sleep(0.05)  # 20 Hz

except KeyboardInterrupt:
    print("\nStopping logging...")

finally:
    file.close()