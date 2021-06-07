import unittest
from third_lab.first_ex import main


class Test_3_2(unittest.TestCase):
    def test_main(self):
        self.assertEqual(len(main("aaaaaab")),
                         len(["b"]))
        self.assertEqual(set(main("aaaaaab")),
                         set(["b"]))

        self.assertEqual(len(main("asd")),
                         len(["a", "d", "s"]))
        self.assertEqual(set(main("asd")),
                         set(["a", "d", "s"]))

        self.assertEqual(len(main("")),
                         len([]))
        self.assertEqual(set(main("")),
                         set([]))

        self.assertEqual(len(main("aa")),
                         len([]))
        self.assertEqual(set(main("aa")),
                         set([]))


if __name__ == '__main__':
    unittest.main()
