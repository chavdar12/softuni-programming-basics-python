"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_bonus_points.py", "20", "6\n26"),
    ("001_bonus_points.py", "175", "37.0\n212.0"),
    ("002_metric_converter.py", "12\nm\ncm", "1200.000"),
    (
        "003_godzilla_vs_kong.py",
        "20000\n120\n55.5",
        "Action!\nWingard starts filming with 11340.00 leva left.",
    ),
    ("004_time_plus_15_minutes.py", "23\n59", "0:14"),
    ("005_scholarship.py", "300\n5.65\n420", "You get a Social scholarship 147 BGN"),
    ("005_scholarship.py", "1000\n5.5\n600", "You get a scholarship for excellent results 137 BGN"),
    ("005_scholarship.py", "480\n4.6\n450", "You cannot get a scholarship!"),
    ("006_sum_seconds.py", "35\n45\n44", "2:04"),
    ("007_speed_info.py", "8", "slow"),
    ("007_speed_info.py", "3500", "extremely fast"),
    (
        "008_world_swimming_record.py",
        "10464\n1500\n20",
        "No, he failed! He was 20786.00 seconds slower.",
    ),
    (
        "008_world_swimming_record.py",
        "1000\n29\n30",
        "Yes, he succeeded! The new world record is 882.50 seconds.",
    ),
    ("009_shopping.py", "900\n2\n1\n3", "You have 198.75 leva left!"),
    ("009_shopping.py", "920.45\n3\n1\n1", "Not enough money! You need 3.92 leva more!"),
    (
        "010_lunch_break.py",
        "Game of Thrones\n60\n96",
        "You have enough time to watch Game of Thrones and left with 0 minutes free time.",
    ),
    (
        "010_lunch_break.py",
        "Teen Wolf\n48\n60",
        "You don't have enough time to watch Teen Wolf, you need 11 more minutes.",
    ),
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
