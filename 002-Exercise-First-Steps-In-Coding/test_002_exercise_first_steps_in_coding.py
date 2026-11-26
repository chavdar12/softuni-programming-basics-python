"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_usd_to_bgn.py", "22", "39.50078"),
    ("002_radians_to_degrees.py", "3.141592653589793", "180.0"),
    ("003_deposit_calculator.py", "200\n3\n5.7", "202.85"),
    ("003_deposit_calculator.py", "2350\n6\n7", "2432.25"),
    ("004_vacation_books_list.py", "212\n20\n2", "5"),
    ("005_school_supplies.py", "2\n3\n4\n25", "28.5"),
    ("005_school_supplies.py", "4\n2\n5\n13", "37.932"),
    ("006_repainting.py", "10\n11\n4\n8", "727.09"),
    ("007_food_delivery.py", "2\n4\n3", "116.2"),
    ("008_basketball_equipment.py", "365", "811.76"),
    ("009_fish_tank.py", "85\n75\n47\n17", "248.68875"),
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
