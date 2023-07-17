import numpy as np
import matplotlib.pyplot as plt
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
    """calculates the acceleration of an object given the force applied to it and its mass"""
    if mass <= 0:
        raise ValueError("mass cannot be less than 0")
    return force / mass


def calculate_angular_acceleration(tau, I):
    """calculates the angular acceleration of an object given the torque applied to it and its moment of inertia"""
    if I <= 0:
        raise ValueError("I cannot be less than 0")
    return tau / I


def calculate_torque(F_magnitude, F_direction, r):
    """calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied
    Takes in Degrees
    """
    if r < 0:
        raise ValueError("r cannot be less than 0")
    return r * F_magnitude * np.sin(np.radians(F_direction))


def calculate_moment_of_inertia(m, r):
    """calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object"""
    if r <= 0:
        raise ValueError("r cannot be less than 0")
    return m * np.power(r, 2)


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    """calculates the acceleration of the AUV in the 2D plane. Takes in radians"""
    if mass <= 0:
        raise ValueError("mass cannot be less than 0")
    if abs(F_magnitude) > 100:
        raise ValueError("Thruster force cannot exceed 100N")
    if abs(F_angle) > np.radians(30):
        raise ValueError("Thruster angle cannot exceed 30 degreees")
    ForceMatrix = np.array(
        [
            F_magnitude * np.cos(F_angle),
            F_magnitude * np.sin(F_angle),
        ]
    )
    return calculate_acceleration(ForceMatrix, mass)


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """calculates the angular acceleration of the AUV."""
    if abs(F_angle) > np.radians(30):
        raise ValueError("Thruster angle cannot exceed 30 degreees")
    if F_magnitude >= 100:
        raise ValueError("Thruster force cannot exceed 100N")
    torque = calculate_torque(F_magnitude, F_angle, thruster_distance)
    # return inertia
    # moment_of_inertia = calculate_moment_of_inertia(mass, thruster_distance)
    return calculate_angular_acceleration(torque, inertia)


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    # print(type(T))
    # print(np.shape(T))
    if type(T) != np.ndarray:
        raise TypeError("first param must be np.array")

    if np.shape(T) != (4, 1) and np.shape(T) != (4,):
        raise ValueError("first param must be array of dimensions (4,)")
    # Force = np.array(shape=(2, 1))
    cosAngle = np.cos(alpha)
    sinAngle = np.sin(alpha)
    # ThrusterDirections = np.empty([2, 2], dtype=float)
    ProjectionMatrix = np.array(
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
    # print(theta)
    RobotCos = np.cos(theta)
    # print(RobotCos)
    RobotSin = np.sin(theta)
    # print("I am working!")
    RotationMatrix = np.array(
        [
            RobotCos,
            -RobotSin,
            RobotSin,
            RobotCos,
        ]
    ).reshape(2, 2)
    # print(RotationMatrix)
    # ThrusterDirections = np.reshape
    # print(ThrusterDirections)
    # print(T)
    LocalForce = np.dot(ProjectionMatrix, T)

    RobotForce = np.dot(RotationMatrix, LocalForce)
    Acceleration = np.divide(RobotForce, mass)
    # print(ProjectionMatrix)
    # print(T)
    # print(RobotForce)
    # print(f"Acceleraton:")
    # print(RotationMatrix)
    return Acceleration


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    if type(T) != np.ndarray:
        raise TypeError("first param must be np.array")

    if np.shape(T) != (4, 1) and np.shape(T) != (4,):
        raise ValueError("first param must be array of dimensions (4,)")
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


def simulate_auv2_motion(
    T,
    angleThruster,
    L,
    l,
    mass=100,
    inertia=100,
    dt=0.1,
    t_final=10,
    x0=0,
    y0=0,
    theta0=0,
):
    time = np.arange(0, t_final, dt)
    num_rows = time.shape[0]

    position = np.zeros((num_rows, 2))
    velocity = np.zeros((num_rows, 2))
    acceleration = np.zeros((num_rows, 2))
    print(acceleration)
    AUV_Angle = np.zeros((num_rows, 1))
    AUV_Angle[0] = theta0
    angular_velocity = np.zeros((num_rows, 1))
    angular_acceleration = np.zeros((num_rows, 1))
    # print("aa SHAPE")
    # print(acceleration.shape)
    for i in range(1, len(time)):
        angular_acceleration[i] = calculate_auv2_angular_acceleration(
            T, angleThruster, L, l, inertia
        ).ravel()
        acceleration[i] = calculate_auv2_acceleration(
            T, angleThruster, AUV_Angle[i - 1], mass
        ).ravel()

        velocity[i] = acceleration[i] * dt + velocity[i - 1]
        angular_velocity[i] = angular_acceleration[i] * dt + angular_velocity[i - 1]

        position[i] = velocity[i] * dt + position[i - 1]
        AUV_Angle[i] = angular_velocity[i] * dt + AUV_Angle[i - 1]
        # print(calculate_auv2_acceleration(T, angleThruster, AUV_Angle[i], mass)[0])
        # print(position[i])
        # print(AUV_Angle[i])
        # print("thing")
        plt.plot(time, position, label="Position")
    return position, AUV_Angle, velocity, angular_velocity, acceleration


if __name__ == "__main__":
    test = np.array([10, 2, 1, 1]).reshape((4, 1))
    simulate_auv2_motion(test, 0.2, 3, 1)
    # print(np.array([2, 2, 1, 1]).reshape(4, 1))
    # print(calculate_auv2_acceleration(test, 45, 45))
    # test = np.array([[1], [3], [1], [2]])
    # print(calculate_auv2_angular_acceleration(test, 0.5, 1.5, 1.8))
    # print(calculate_auv2_acceleration(test, 0.5, 0.3))
    # print(calculate_auv_acceleration(30, math.pi / 2, 0.3))
