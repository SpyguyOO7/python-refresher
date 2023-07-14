import numpy as np

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
    return force / mass


def calculate_angular_acceleration(tau, I):
    return tau / I


def calculate_torque(F_magnitude, F_direction, r):
    return r * F_magnitude * np.sin(F_magnitude)


def calculate_moment_of_inertia(m, r):
    return m * (r ^ 2)
