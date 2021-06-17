import unittest
from fourth_lab.first_ex import main


class Test_4_1(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main("abc")[1], 3)
        self.assertEqual(main("aaabc")[1], 3)
        self.assertEqual(main("abcd")[1], 4)
        self.assertEqual(main("Lorem ipsum dolor sit amet, consectetur")[1], 17)


if __name__ == '__main__':
    unittest.main()
