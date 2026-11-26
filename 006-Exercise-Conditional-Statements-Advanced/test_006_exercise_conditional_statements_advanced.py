"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_cinema.py", "Premiere\n10\n12", "1440.00"),
    ("002_fishing_boat.py", "3000\nSummer\n11", "Not enough money! You need 570.00 leva."),
    ("003_hotel_room.py", "May\n15", "Apartment: 877.50 lv.\nStudio: 525.00 lv."),
    ("004_journey.py", "50\nsummer", "Somewhere in Bulgaria\nCamp - 15.00"),
    ("005_new_house.py", "Roses\n55\n250", "Not enough money, you need 25.00 leva more."),
    ("006_on_time_for_the_exam.py", "9\n30\n9\n50", "Late\n20 minutes after the start"),
    ("006_on_time_for_the_exam.py", "16\n0\n15\n0", "Early\n1:00 hours before the start"),
    ("007_operations_between_numbers.py", "10\n12\n+", "10 + 12 = 22 - even"),
    ("007_operations_between_numbers.py", "0\n5\n/", "0 / 5 = 0.00"),
    ("007_operations_between_numbers.py", "10\n0\n%", "Cannot divide 10 by zero"),
    ("008_summer_outfit.py", "16\nMorning", "It's 16 degrees, get your Sweatshirt and Sneakers."),
    ("009_volleyball.py", "leap\n5\n2", "45"),
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
