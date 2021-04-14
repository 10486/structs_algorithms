import unittest
from first_lab.first_ex import main
import numpy as np


class Test_1_1(unittest.TestCase):
    def test_main(self):
        self.assertTrue(np.allclose(
                        main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                        np.array([10, 8, 6, 4, 2])))

        self.assertTrue(np.allclose(
                        main([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                        np.array([8, 6, 4, 2])))

        self.assertTrue(np.allclose(
                        main([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
                        np.array([2, 4, 6, 8, 10])))


if __name__ == '__main__':
    unittest.main()
