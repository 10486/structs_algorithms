import unittest
from third_lab.second_ex import main


class Test_3_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main([x for x in range(10)]),
                         [x for x in range(10) if x % 10 != 5])
        self.assertEqual(main([x for x in range(10, 0, -1)]),
                         [x for x in range(10, 0, -1) if x % 10 != 5])
        self.assertEqual(main([x for x in range(10, 100)]),
                         [x for x in range(10, 100) if x % 10 != 5])
        self.assertEqual(main([x for x in range(100, 900)]),
                         [x for x in range(100, 900) if x % 10 != 5])


if __name__ == '__main__':
    unittest.main()
