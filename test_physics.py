import unittest
import physics

class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(3,2), 6*9.81)
        self.assertNotEqual(physics.calculate_buoyancy(4,2), 6*9.81)
        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(-1,0)
        with self.assertRaises(ValueError):
            physics.calculate_buoyancy(1,-1)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(1,1), True)
        self.assertEqual(physics.will_it_float(1,1001), False)
        with self.assertRaises(ValueError):
            physics.will_it_float(-1,0)
        with self.assertRaises(ValueError):
            physics.will_it_float(1,-1)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(20), 1000*9.81*20)
        self.assertEqual(physics.calculate_pressure(10), 1000*9.81*10)
        with self.assertRaises(ValueError):
            physics.calculate_pressure(-1)

if __name__ == "__main__":
    unittest.main()
