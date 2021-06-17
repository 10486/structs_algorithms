import unittest
from sixth_lab.second_ex import main
import numpy as np


class Test_6_2(unittest.TestCase):
    def test_main(self):
        self.assertTrue(np.allclose(
            main(a := np.random.randint(0, 100, 100), a[3]), sorted(a[:3] + a[4:])))


if __name__ == '__main__':
    unittest.main()
