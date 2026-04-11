import numpy as np

class KalmanFilter:

    def __init__(self):
        self.x = np.zeros((2,1))  # state [x, y]
        self.P = np.eye(2)

        self.F = np.eye(2)  # state transition
        self.Q = np.eye(2) * 0.01  # process noise

        self.H = np.eye(2)  # measurement
        self.R = np.eye(2) * 0.1  # measurement noise

    def predict(self, imu_acc_x):
        u = np.array([[imu_acc_x], [0]])
        self.x = self.F @ self.x + u
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, slam_pose, tof_distance):
        z = np.array([[slam_pose[0]], [slam_pose[1]]])

        # Adjust measurement using ToF constraint
        correction_factor = 1.0
        if tof_distance > 0:
            correction_factor = 1.0 / (1 + tof_distance/5000.0)

        z = z * correction_factor

        y = z - (self.H @ self.x)
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.x = self.x + K @ y
        self.P = (np.eye(2) - K @ self.H) @ self.P

        return self.x