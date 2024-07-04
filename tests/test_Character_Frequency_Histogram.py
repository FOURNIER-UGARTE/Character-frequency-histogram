import unittest

from Character_frequency_histogram import Character_Frequency_Histogram


class MyTestCase(unittest.TestCase):
    object_character_frequency_histogram = Character_Frequency_Histogram()
    
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
