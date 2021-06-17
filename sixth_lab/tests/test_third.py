import unittest
from sixth_lab.third_ex import main


class Test_6_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main("dsa", "asdasdasdasdasddsaasdasdasd"), 15)


if __name__ == '__main__':
    unittest.main()
