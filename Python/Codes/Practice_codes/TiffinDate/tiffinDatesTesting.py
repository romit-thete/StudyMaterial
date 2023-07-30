import unittest
from tiffinDates import tiffin_next_date


class TiffinDatesTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(tiffin_next_date("2023-07-24", "26"), ("2023-09-05", "2023-09-06"))

    def test2(self):
        self.assertEqual(tiffin_next_date("2023-06-07", "26"), ("2023-07-20", "2023-07-24"))

    def test3(self):
        self.assertEqual(tiffin_next_date("2023-07-31", "26"), ("2023-09-12", "2023-09-13"))


if __name__ == "__main__":
    unittest.main()
