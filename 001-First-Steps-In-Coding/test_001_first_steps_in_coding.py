"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_hello_softuni.py", "", "Hello SoftUni"),
    ("002_nums_1_to_10.py", "", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"),
    ("003_rectangle_area.py", "2\n7", "14"),
    ("004_inches_to_centimeters.py", "5", "12.7"),
    ("005_greeting_by_name.py", "Peter", "Hello Peter!"),
    (
        "006_concatenate_data.py",
        "Peter\nPan\n20\nSofia",
        "You are Peter Pan, a 20-years old person from Sofia.",
    ),
    (
        "007_project_creation.py",
        "George\n4",
        "The architect George will need 12 hours to complete 4 project/s.",
    ),
    ("008_pet_shop.py", "5\n4", "28.5"),
    ("009_yard_greening.py", "100", "The final price is: 624.02\nThe discount is: 136.98"),
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
