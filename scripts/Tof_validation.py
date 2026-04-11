import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# -------------------------------
# LOAD DATA
# -------------------------------

def load_trajectory(file_path):
    """
    Expected format:
    timestamp x y z qx qy qz qw
    """
    data = np.loadtxt(file_path)
    timestamps = data[:, 0]
    positions = data[:, 1:3]  # use x, y only
    return timestamps, positions

def load_tof(file_path):
    df = pd.read_csv(file_path)
    return df["timestamp"].values, df["tof1_mm"].values

# -------------------------------
# SYNCHRONIZATION
# -------------------------------

def synchronize_data(traj_t, traj_xy, tof_t, tof_d):
    """
    Interpolate ToF to match trajectory timestamps
    """
    tof_interp = interp1d(tof_t, tof_d, fill_value="extrapolate")
    synced_tof = tof_interp(traj_t)
    return traj_xy, synced_tof

# -------------------------------
# ERROR DETECTION
# -------------------------------

def compute_expected_distance(traj_xy):
    """
    Compute distance from trajectory centerline
    """
    distances = np.linalg.norm(traj_xy, axis=1)
    return distances

def compute_error(expected, measured):
    """
    Convert mm → meters and compute difference
    """
    measured_m = measured / 1000.0
    error = expected - measured_m
    return error

# -------------------------------
# ERROR CORRECTION
# -------------------------------

def correct_trajectory(traj_xy, error):
    """
    Apply correction factor to trajectory
    """
    corrected = []

    for i in range(len(traj_xy)):
        x, y = traj_xy[i]
        e = error[i]

        scale = 1.0
        if abs(e) > 0.1:  # threshold (10 cm)
            scale = 1.0 - (e * 0.5)

        corrected.append([x * scale, y * scale])

    return np.array(corrected)

# -------------------------------
# MAP GENERATION
# -------------------------------

def generate_occupancy_map(points, resolution=0.05):
    """
    Convert points into 2D grid map
    """
    x = points[:, 0]
    y = points[:, 1]

    x_min, x_max = np.min(x), np.max(x)
    y_min, y_max = np.min(y), np.max(y)

    grid_x = int((x_max - x_min) / resolution)
    grid_y = int((y_max - y_min) / resolution)

    grid = np.zeros((grid_x, grid_y))

    for i in range(len(points)):
        gx = int((x[i] - x_min) / resolution)
        gy = int((y[i] - y_min) / resolution)

        if 0 <= gx < grid_x and 0 <= gy < grid_y:
            grid[gx, gy] = 1

    return grid

# -------------------------------
# VISUALIZATION
# -------------------------------

def plot_results(traj, corrected, error):
    plt.figure()

    plt.plot(traj[:, 0], traj[:, 1], label="Original SLAM")
    plt.plot(corrected[:, 0], corrected[:, 1], label="Corrected")

    plt.legend()
    plt.title("Trajectory Correction using ToF")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.grid()

    plt.show()

def plot_error(error):
    plt.figure()
    plt.plot(error)
    plt.title("Error between SLAM and ToF")
    plt.xlabel("Time Index")
    plt.ylabel("Error (m)")
    plt.grid()
    plt.show()

# -------------------------------
# MAIN PIPELINE
# -------------------------------

def main():

    # Load data
    traj_t, traj_xy = load_trajectory("trajectory.txt")
    tof_t, tof_d = load_tof("tof_data.csv")

    # Sync
    traj_xy, synced_tof = synchronize_data(traj_t, traj_xy, tof_t, tof_d)

    # Compute distances
    expected = compute_expected_distance(traj_xy)
    error = compute_error(expected, synced_tof)

    # Correct trajectory
    corrected = correct_trajectory(traj_xy, error)

    # Generate maps
    original_map = generate_occupancy_map(traj_xy)
    corrected_map = generate_occupancy_map(corrected)

    # Visualize
    plot_results(traj_xy, corrected, error)
    plot_error(error)

    print("Map correction complete!")

# -------------------------------

if __name__ == "__main__":
    main()