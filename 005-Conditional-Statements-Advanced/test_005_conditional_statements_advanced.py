"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_animal_type.py", "dog", "mammal"),
    ("001_animal_type.py", "cat", "unknown"),
    ("002_cinema_ticket.py", "Monday", "12"),
    ("003_day_of_week.py", "2", "Tuesday"),
    ("003_day_of_week.py", "8", "Error"),
    ("004_fruit_or_vegetable.py", "banana", "fruit"),
    ("005_fruit_shop.py", "apple\nTuesday\n2", "2.40"),
    ("005_fruit_shop.py", "tomato\nMonday\n0.5", "error"),
    ("006_invalid_number.py", "75", "invalid"),
    ("006_invalid_number.py", "150", ""),
    ("007_number_in_range.py", "-25", "Yes"),
    ("007_number_in_range.py", "0", "No"),
    ("008_personal_titles.py", "12\nf", "Miss"),
    ("008_personal_titles.py", "17\nm", "Mr."),
    ("009_ski_trip.py", "14\napartment\npositive", "264.06"),
    ("010_small_shop.py", "coffee\nVarna\n2", "0.9"),
    ("011_trade_commissions.py", "Sofia\n1500", "120.00"),
    ("011_trade_commissions.py", "Kaspichan\n100", "error"),
    ("012_working_hours.py", "11\nSunday", "closed"),
    ("012_working_hours.py", "11\nMonday", "open"),
    ("013_weekend_or_working_day.py", "Monday", "Working day"),
    ("013_weekend_or_working_day.py", "Sunday", "Weekend"),
    ("013_weekend_or_working_day.py", "April", "Error"),
]


def normalize(text):
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


class TestLesson(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected in CASES:
            with self.subTest(script=script, stdin=stdin):
                result = subprocess.run(
                    [sys.executable, str(HERE / script)],
                    input=stdin + "\n",
                    capture_output=True,
                    text=True,
                    timeout=10,
                    cwd=HERE,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(normalize(result.stdout), normalize(expected))

    def test_every_script_has_a_case(self):
        scripts = {p.name for p in HERE.glob("*.py") if not p.name.startswith("test_")}
        self.assertEqual(scripts - {c[0] for c in CASES}, set())


if __name__ == "__main__":
    unittest.main()
