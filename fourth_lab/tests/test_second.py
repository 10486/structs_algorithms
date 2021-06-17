import unittest
from fourth_lab.second_ex import main


class Test_4_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main("a a a a b", 10).search("a"), 4)
        self.assertEqual(main("a b b ab a b", 10).search("a"), 2)
        self.assertEqual(main("a aaa b", 10).search("a"), 1)
        self.assertEqual(main("a a a a b bababa", 10).search("b"), 1)
        self.assertEqual(main("a a a a b ababa", 10).search("ababa"), 1)


if __name__ == '__main__':
    unittest.main()
