import unittest
from second_lab.first_ex import main
from second_lab.first_ex import Drug


class Test_2_1(unittest.TestCase):
    def test_main(self):
        drugs = [
            Drug(drugstore_number=1, name='asd', count=10, cost=1000,
                 receipt_date=[2004, 10, 12], shelf_life=10),
            Drug(drugstore_number=2, name='dsa', count=101, cost=10,
                 receipt_date=[2003, 10, 12], shelf_life=100),
            Drug(drugstore_number=3, name='aaa', count=100, cost=100,
                 receipt_date=[2003, 9, 12], shelf_life=1000)
        ]
        self.assertCountEqual(
            main(drugs, 'drugstore_number'),
            drugs)

        self.assertCountEqual(
            main(drugs, 'name'),
            [drugs[2], drugs[0], drugs[1]])

        self.assertCountEqual(
            main(drugs, 'count'),
            [drugs[0], drugs[2], drugs[1]])

        self.assertCountEqual(
            main(drugs, 'cost'),
            [drugs[1], drugs[0], drugs[2]])

        self.assertCountEqual(
            main(drugs, 'receipt_date'),
            [drugs[2], drugs[1], drugs[0]])

        self.assertCountEqual(
            main(drugs, 'shelf_life'),
            drugs)


if __name__ == '__main__':
    unittest.main()
