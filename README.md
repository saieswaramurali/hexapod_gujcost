# hexapod_gujcost

![hexapod_rendered](https://github.com/user-attachments/assets/9dc10749-d024-4cbf-97d7-f600535d30f0)

This repository contains the ROS 2 codebase for a hexapod robot developed under the GUJCOST-funded project. It includes joystick-based control, SLAM integration, step detection, and modular movement control.

## 🐜 Project Overview

The hexapod robot is designed to perform walking, sitting, and standing motions using servo motors. Control is handled via joystick input, and servo angles are published through ROS 2 topics. The robot is being extended to include autonomous navigation using SLAM and stair/step detection.

---

## 🗂️ Package Structure

| Package Name             | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `hexapod_controller`     | Handles joystick input and publishes servo angles                           |
| `hexapod_publisher`      | Publishes data to topics (legacy/support module)                            |
| `hexapod_description`    | URDF and robot model descriptions                                            |
| `hexapod_mapping`        | Contains SLAM configuration and launch files                                |
| `hexapod_step_detection` | Detects steps/stairs using vision or sensor data                            |
| `src/`                   | Additional scripts or raw ROS 2 nodes                                       |

---

## 🎮 Key Features

- Joystick control with mode switching (walk/sit/stand)
- Servo angle publishing to `/servo_angles`
- SLAM mapping using `slam_toolbox`
- Step detection module for stair-aware movement
- URDF-based robot visualization in RViz
- SC15 servo driver compatible (feedback-ready)

---

## 🔧 Requirements

- ROS 2 Foxy or later
- Joystick (Xbox/PS)
- ESP32 or other servo driver board
- SC15 or compatible servos
- Depth camera (e.g., Intel RealSense) for step detection

---

## 🚀 Quick Start

```bash
# Clone the repo inside your ROS 2 workspace
cd ~/ros2_ws/src
git clone https://github.com/saieswaramurali/hexapod_gujcost.git

# Build the workspace
cd ~/ros2_ws
colcon build

# Source and launch the controller
source install/setup.bash
ros2 launch hexapod_controller controller.launch.py

