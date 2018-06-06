from unittest import TestCase
from processPrecipationsByWeek import ProcessPrecipationsByWeek


class TestProcessPrecipationsByWeek(TestCase):
    def test_wpre(self):
        x=ProcessPrecipationsByWeek(1)
        self.assertEqual(x.wpre, 1.8)

    def test_wpre(self):
        x = ProcessPrecipationsByWeek(2)
        self.assertEqual(x.wpre, 0.29)
