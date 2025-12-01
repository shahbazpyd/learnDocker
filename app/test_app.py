# test_app.py
import unittest

class TestApp(unittest.TestCase):
    def test_addition(self):
        # This is your dummy unit test
        self.assertEqual(1 + 1, 2)

    def test_failure(self):
        # Simulate a test that might fail in the future
        self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()