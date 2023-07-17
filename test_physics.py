import unittest
import physics
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(3, 2), 6 * 9.81)
        self.assertNotEqual(physics.calculate_buoyancy(4, 2), 6 * 9.81)
        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(-1, 0)
        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(1, -1)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(1, 1), True)
        self.assertEqual(physics.will_it_float(1, 1001), False)
        with self.assertRaises(ValueError):
            physics.will_it_float(-1, 0)
        with self.assertRaises(ValueError):
            physics.will_it_float(1, -1)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(20), 1000 * 9.81 * 20 + 101325)
        self.assertEqual(physics.calculate_pressure(10), 1000 * 9.81 * 10 + 101325)
        with self.assertRaises(ValueError):
            physics.calculate_pressure(-1)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(6, 2), 3)
        self.assertNotEqual(physics.calculate_acceleration(6, 2), 0)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(6, 2), 3)
        self.assertNotEqual(physics.calculate_angular_acceleration(6, 2), 0)

    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(6, 90, 2), 12)
        self.assertNotEqual(physics.calculate_torque(6, 90, 2), 0)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(6, 2), 24)
        self.assertNotEqual(physics.calculate_moment_of_inertia(6, 90), 0)

    def test_calculate_auv_acceleration(self):
        result = physics.calculate_auv_acceleration(6, 0.1, 2)
        self.assertEqual(result[0], 3)
        self.assertEqual(result[1], 3)

    def test_calculate_auv_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv_angular_acceleration(6, 0.1, 2, 2), 6)
        self.assertNotEqual(physics.calculate_auv_angular_acceleration(6, 0.1, 2, 2), 0)

    def test_calculate_auv2_acceleration(self):
        testArray = np.array([1, 3, 1, 2])
        result = physics.calculate_auv2_acceleration(testArray, 0.5, 0.3)
        self.assertEqual(result[0], 0.009800665778412416)
        self.assertEqual(result[1], -0.001986693307950612)

    def test_calculate_auv2_angular_acceleration(self):
        testArray = np.array([1, 3, 1, 2])
        result = physics.calculate_auv2_angular_acceleration(testArray, 0.5, 1.5, 1.8)
        print(result)
        self.assertEqual(result, -0.06896360757926927)


if __name__ == "__main__":
    unittest.main()
