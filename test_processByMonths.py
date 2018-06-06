from unittest import TestCase
from processByMonths import ProcessByMonths

class TestProcessByMonths(TestCase):
    def test_mmax(self):
        x=ProcessByMonths(1)
        self.assertEqual(x.mmax, 59)

    def test_mmin(self):
        x = ProcessByMonths(1)
        self.assertEqual(x.mmin, 11)

    def test_mavg(self):
        x = ProcessByMonths(1)
        self.assertEqual(x.mavg, 34.45161290322581)
