#!/usr/bin/env python3
import unittest
from stop_watch import StopWatch


class StopWatchTest(unittest.TestCase):

    def setUp(self):
        self.stopwatch = StopWatch()

    def test_get_start_time(self):
        self.assertEqual(self.stopwatch.get_start_time(), self.stopwatch._StopWatch__startTime)

    def test_get_end_time(self):
        self.assertEqual(self.stopwatch.get_end_time(), self.stopwatch._StopWatch__endTime)

    def test_get_elapsed_time(self):
        elapsed = self.stopwatch.get_end_time() - self.stopwatch.get_start_time()
        self.assertEqual(self.stopwatch.get_elapsed_time(), elapsed)

if __name__ == "__main__":
    unittest.main()


