#!/usr/bin/env python3
#acts as the low level control for the robot does the calculation of the servo anges for each command 
# and sends it to the controller.py to execute . 

import numpy as np 
import matplotlib.pyplot as plt

def generate_parabola(C, H):
    X = (C) ** 0.5  
    print(f"X = {X}")
    X_coords = np.linspace(0, 2 * X, 100)
    leg_path = []
    for i in X_coords:
        value = (C - (i - X)**2) * H / C  # Shift the x-values to get the same Y behavior
        leg_path.append(value)
    plt.plot(X_coords, leg_path)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Leg Path from 0 to 2X')
    plt.show()
    return leg_path, X_coords

# path, X_coords = generate_parabola(C, H)
# path


# assuming to set stand up is setting all zervos to 90
def stand_up():
    angles = []
    for i in range(18):
        angles.append(90)  # Append 90 to the list at each iteration
    return angles

def sit_down() : 
    angles = []
    for i in range(18) : 
        angles.append(0)
    return angles 

def inverse_kinematics() : 
    pass 
