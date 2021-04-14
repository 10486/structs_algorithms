import unittest
from first_lab.second_ex import main


class Test_1_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main("qwertyuiop", 0, 3), "qwe")
        self.assertEqual(main("qwertyuiop", 1, 3), "wer")
        self.assertEqual(main("qwertyuiop", 1, 4), "wert")


if __name__ == '__main__':
    unittest.main()
