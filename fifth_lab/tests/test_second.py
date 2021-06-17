import unittest
from fifth_lab.second_ex import main
import numpy as np


class Test_5_1(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main(a := np.random.randint(0, 100, 100)), sorted(a))


if __name__ == '__main__':
    unittest.main()
