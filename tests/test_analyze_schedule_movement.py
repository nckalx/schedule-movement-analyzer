from datetime import date
from pathlib import Path
import sys
import unittest


# Add the project root to the import path so this test can import from src.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.analyze_schedule_movement import count_workdays_moved


class TestCountWorkdaysMoved(unittest.TestCase):
    def test_unchanged_dates_return_zero(self):
        result = count_workdays_moved(date(2026, 1, 5), date(2026, 1, 5))

        self.assertEqual(result, 0)

    def test_delayed_dates_return_positive_workdays(self):
        result = count_workdays_moved(date(2025, 10, 10), date(2025, 10, 17))

        self.assertEqual(result, 5)

    def test_accelerated_dates_return_negative_workdays(self):
        result = count_workdays_moved(date(2026, 2, 2), date(2026, 1, 29))

        self.assertEqual(result, -2)

    def test_weekends_are_not_counted_as_workdays(self):
        result = count_workdays_moved(date(2026, 1, 9), date(2026, 1, 12))

        self.assertEqual(result, 1)

    def test_holidays_are_not_counted_as_workdays(self):
        result = count_workdays_moved(date(2025, 12, 24), date(2025, 12, 26))

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
