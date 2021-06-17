import unittest
from sixth_lab.first_ex import main


class Test_6_1(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main([x % 2 for x in range(100)]), ([x*2 for x in range(50)], 50))


if __name__ == '__main__':
    unittest.main()
