from unittest import TestCase
from dataParser import DataParser

class TestDataParser(TestCase):
    def test_maxs(self):
        x = DataParser('test.csv')
        self.assertEqual(x.maxs, [89, 91])

    def test_mins(self):
        x = DataParser('test.csv')
        self.assertEqual(x.mins, [71, 75])

    def test_avgs(self):
        x = DataParser('test.csv')
        self.assertEqual(x.avgs, [80, 83])

    def test_precipations(self):
        x = DataParser('test.csv')
        self.assertEqual(x.precipations, [0, 0.22])
