import numpy as np

def calculate_buoyancy(volume: int or float, density_fluid: int or float):
    """Calulates the buoyancy of an object, taking in Volume and density of the fluid. metric units"""
    g = 9.81
    buoyancy = volume*density_fluid*g
    return buoyancy

def will_it_float(volume: int or float, mass: int or float):
    """determines whether an object will float or sink in water. Takes in volume and mass"""
    density_object = mass/volume
    density_water = 1000
    return density_object<density_water

def calculate_pressure(depth: int or float):
    """calculates the pressure at a given depth in water. Takes in depth"""
    g = 9.81# m/s^2
    density_water = 1000
    return density_water*g*depth

