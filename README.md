
# INDOOR-NAVIGATION

## A Low-Cost ToF LiDAR-Assisted Visual–Inertial SLAM System Using Multi-Sensor Fusion for Indoor Localization on Raspberry Pi 5

---

## 📌 Overview

This project presents a **low-cost indoor localization and mapping system** using **Visual–Inertial SLAM combined with ToF LiDAR**. It is designed to operate on a **Raspberry Pi 5**, enabling real-time indoor navigation in GPS-denied environments such as libraries, malls, and office buildings.

The system integrates data from:

* 📷 Camera (Visual SLAM)
* 🧭 IMU (Inertial sensing)
* 📡 ToF LiDAR (Distance measurement)

Using **multi-sensor fusion**, the system improves accuracy, robustness, and reliability compared to single-sensor SLAM systems.

---

## 🎯 Objectives

* Develop a **low-cost indoor navigation system**
* Perform **real-time mapping and localization**
* Fuse **LiDAR + Camera + IMU data** for improved accuracy
* Enable **QR-based initialization for navigation**
* Deploy on **edge hardware (Raspberry Pi 5)**

---

## 🧠 System Architecture

```
        +---------------------+
        |     Camera Input    |
        +---------------------+
                  |
        +---------------------+
        |   Visual SLAM       |
        +---------------------+
                  |
        +---------------------+
        |   Sensor Fusion     | <---- IMU Data
        +---------------------+
                  |
        +---------------------+
        |   LiDAR Correction  |
        +---------------------+
                  |
        +---------------------+
        | Mapping + Localization |
        +---------------------+
                  |
        +---------------------+
        | Navigation Output   |
        +---------------------+
```

---

## 🛠️ Hardware Requirements

* Raspberry Pi 5
* ToF LiDAR Sensor (e.g., RPLiDAR A1 / S1)
* IMU Sensor (MPU6050 or equivalent)
* USB Camera / Pi Camera
* Power Supply
* Jumper Wires & Mounting Setup

---

## 💻 Software Stack

* Ubuntu / Raspberry Pi OS
* ROS 2 (Robot Operating System)
* OpenCV
* Python 3
* SLAM Framework (ORB-SLAM / Visual-Inertial SLAM)

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/INDOOR-NAVIGATION.git
cd INDOOR-NAVIGATION
```

### 2. Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip git
pip3 install opencv-python numpy
```

### 3. ROS 2 Setup

```bash
source /opt/ros/humble/setup.bash
```

---

## ▶️ Usage

### 1. Start Sensors

* Connect IMU and LiDAR
* Start camera feed

### 2. Run SLAM

```bash
python3 main.py
```

### 3. Visualize Output

* RViz (for mapping)
* OpenCV window (for camera tracking)

---

## 📊 Features

* ✅ Real-time indoor mapping
* ✅ Multi-sensor fusion (Camera + IMU + LiDAR)
* ✅ Low-cost hardware implementation
* ✅ Edge deployment on Raspberry Pi 5
* ✅ Scalable for multi-floor environments

---

## 🚀 Applications

* Indoor navigation (malls, libraries)
* Search & Rescue robotics
* Autonomous robots
* Smart campus systems

---

## 📁 Project Structure

```
INDOOR-NAVIGATION/
│── src/
│   ├── slam/
│   ├── sensor_fusion/
│   ├── lidar/
│   └── imu/
│── scripts/
│── config/
│── launch/
│── data/
│── README.md
```

---

## 🔬 Future Improvements

* Integration with mobile app navigation
* 3D SLAM support
* AI-based obstacle detection
* Cloud-based map storage

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Authors

* Ivan Antony Babu
* Team Members (Add names here)

---

## 📬 Contact

For queries or collaborations:

📧 Email: [your-email@example.com](mailto:your-email@example.com)

---

⭐ If you found this project useful, consider giving it a star!
