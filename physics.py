import numpy as np
import math

Atmospheric_Pressure = 101325
density_water = 1000
g = 9.81  # m/s^2


def calculate_buoyancy(volume: int or float, density_fluid: int or float):
    """Calulates the buoyancy of an object, taking in Volume and density of the fluid. metric units"""
    if volume < 0 or density_fluid < 0:
        raise ValueError("value cannot be less than 0")
    buoyancy = volume * density_fluid * g
    return buoyancy


def will_it_float(volume: int or float, mass: int or float):
    """determines whether an object will float or sink in water. Takes in volume and mass"""
    if volume < 0 or mass < 0:
        raise ValueError("value cannot be less than 0")
    density_object = mass / volume
    return density_object < density_water


def calculate_pressure(depth: int or float):
    """calculates the pressure at a given depth in water. Takes in depth"""
    if depth < 0:
        raise ValueError("value cannot be less than 0")

    return density_water * g * depth + Atmospheric_Pressure


def calculate_acceleration(force, mass):
    if mass < 0:
        raise ValueError("mass cannot be less than 0")
    return force / mass


def calculate_angular_acceleration(tau, I):
    if I < 0:
        raise ValueError("I cannot be less than 0")
    return tau / I


def calculate_torque(F_magnitude, F_direction, r):
    if r < 0:
        raise ValueError("r cannot be less than 0")
    return r * F_magnitude * np.sin(np.radians(F_direction))


def calculate_moment_of_inertia(m, r):
    if r < 0:
        raise ValueError("r cannot be less than 0")
    return m * r * r


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    if mass < 0:
        raise ValueError("mass cannot be less than 0")
    if F_magnitude > 100:
        raise ValueError("Thruster force cannot exceed 100N")
    if abs(F_angle) > np.radians(30):
        raise ValueError("Thruster angle cannot exceed 30 degreees")
    xAccel = calculate_acceleration(F_magnitude * np.cos(F_angle), mass)
    yAccel = calculate_acceleration(F_magnitude * np.sin(F_angle), mass)
    return np.array([xAccel, yAccel])


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    if abs(F_angle) > np.radians(30):
        raise ValueError("Thruster angle cannot exceed 30 degreees")
    if F_magnitude >= 100:
        raise ValueError("Thruster force cannot exceed 100N")
    torque = calculate_torque(F_magnitude, F_angle, thruster_distance)
    # return inertia
    # moment_of_inertia = calculate_moment_of_inertia(mass, thruster_distance)
    return calculate_angular_acceleration(torque, inertia)


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    # Force = np.array(shape=(2, 1))
    cosAngle = np.cos(alpha)
    sinAngle = np.sin(alpha)
    # ThrusterDirections = np.empty([2, 2], dtype=float)
    ThrusterDirections = np.array(
        [
            cosAngle,
            cosAngle,
            -cosAngle,
            -cosAngle,
            sinAngle,
            -sinAngle,
            -sinAngle,
            sinAngle,
        ]
    ).reshape(2, 4)
    RobotCos = np.cos(theta)
    RobotSin = np.sin(theta)
    RotationMatrix = np.array(
        [
            RobotCos,
            -RobotSin,
            RobotSin,
            RobotCos,
        ]
    ).reshape(2, 2)
    # ThrusterDirections = np.reshape
    # print(ThrusterDirections)
    # print(T)
    LocalForce = np.dot(ThrusterDirections, T)

    RobotForce = np.dot(RotationMatrix, LocalForce)
    Acceleration = np.divide(RobotForce, mass)
    # print(Force)
    # print(Acceleraton)
    return Acceleration


test = np.array([2, 2, 1, 1]).reshape(4, 1)
print(calculate_auv2_acceleration(test, 45, 45))


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    r = np.sqrt(np.power(L, 2) + np.power(l, 2))
    TotalTorque = 0
    counter = 0
    for i in T:
        # print(i)
        if counter % 2 == 0:
            TotalTorque += T[counter] * (np.sin(alpha) * L + np.cos(alpha) * l)
        else:
            TotalTorque -= T[counter] * (np.sin(alpha) * L + np.cos(alpha) * l)
        counter += 1
    # print(TotalTorque)
    return calculate_angular_acceleration(TotalTorque, inertia)


test = np.array([1, 3, 1, 2])
print(calculate_auv2_angular_acceleration(test, 0.5, 1.5, 1.8))
print(calculate_auv2_acceleration(test, 0.5, 0.3))
print(calculate_auv_acceleration(30, math.pi / 2, 0.3))
