import unittest
import hello
import math

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "Hi, world!")

    def test_add(self):
        self.assertEqual(hello.add(0,1), 1)
        self.assertEqual(hello.add(1,2), 3)

    def test_sub(self):
        self.assertEqual(hello.sub(0,1), -1)
        self.assertEqual(hello.sub(1,2), -1)

    def test_mul(self):
        self.assertEqual(hello.mul(0,1), 0)
        self.assertEqual(hello.mul(1,2), 2)

    def test_div(self):
        self.assertEqual(hello.div(0,1), 0)
        self.assertEqual(hello.div(1,4), .25)
        #self.assertRaises(hello.div(1,0), ValueError)
        with self.assertRaises(ValueError):
            hello.div(1,0)
        #self.assertEqual(str(message.exception), 'Can\'t divide by zero!')
    def test_sqrt(self):
        self.assertEqual(hello.sqrt(1), 1)
        self.assertEqual(hello.sqrt(4), 2)


    def test_power(self):
        self.assertEqual(hello.power(0,1), 0)
        self.assertEqual(hello.power(1,4), 1)

    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertEqual(hello.log(math.e), 1)

    def test_exp(self):
        self.assertEqual(hello.power(0,1), 0)
        self.assertEqual(hello.power(1,4), 1)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
