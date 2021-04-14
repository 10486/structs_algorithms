import unittest
from second_lab.second_ex import main


class Test_2_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main([x for x in range(1, 11)]), 4.528728688116765)
        self.assertEqual(main([x for x in range(1, 21)]), 8.304361203739344)
        self.assertEqual(main([4, 1]), 2)


if __name__ == '__main__':
    unittest.main()
