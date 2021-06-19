import unittest
from sixth_lab.second_ex import main
import numpy as np


class Test_6_2(unittest.TestCase):
    def test_main(self):
        b = main(a := np.random.randint(0, 100, 100), a[3])
        c = sorted(set(x for x in a if x != a[3]))
        self.assertListEqual(b, c)


if __name__ == '__main__':
    unittest.main()
