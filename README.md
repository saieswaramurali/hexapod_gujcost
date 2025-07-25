# hexapod_gujcost

![hexapod_rendered](https://github.com/user-attachments/assets/9dc10749-d024-4cbf-97d7-f600535d30f0)

This repository contains the ROS 2 codebase for a hexapod robot developed as part of the GUJCOST-funded project.

## 🐜 Project Overview

The hexapod robot is designed for walking, sitting, and standing motions using servo motors controlled via joystick input. It publishes servo angles through ROS 2 topics and is built to support real-time movement with future plans for autonomous navigation using reinforcement learning.

## 🎮 Features

- Joystick-based control (using Xbox/PS controller)
- Servo angle publishing on ROS 2 topic `/servo_angles`
- Mode switching (walk, sit, stand) via button combinations
- Feedback-ready integration (for SC15 servo telemetry)
- Modular and scalable control logic

## 📦 ROS 2 Package Structure

- `hexapod_controller/`: Node handling joystick input and publishing servo angles
- `msg_interfaces/`: Custom message definitions (if applicable)
- `launch/`: Launch files to start the control stack

## 🧩 Topics

- `/servo_angles` – Publishes an array of angles for each leg's servos
- `/joy` – Subscribed topic from joystick device

## 🔧 Requirements

- ROS 2 Foxy or later
- A joystick (e.g., Xbox, PS4)
- SC15 servos (or compatible)
- ESP32 or servo driver board (subscriber to `/servo_angles`)

## 🚀 How to Launch

```bash
# Clone the repo inside your ROS 2 workspace
cd ~/your_ros2_ws/src
git clone https://github.com/saieswaramurali/hexapod_gujcost.git

# Build the workspace
cd ~/your_ros2_ws
colcon build

# Source and launch
source install/setup.bash
ros2 launch hexapod_controller controller.launch.py

