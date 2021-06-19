import unittest
from fourth_lab.third_ex import main


class Test_4_2(unittest.TestCase):
    def test_main(self):
        self.assertGreater(main([10**x + 1 for x in range(100)], 1),
                           main([x for x in range(100)], 1))


if __name__ == '__main__':
    unittest.main()
