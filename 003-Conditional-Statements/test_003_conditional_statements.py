"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_area_of_figures.py", "square\n5", "25.000"),
    ("001_area_of_figures.py", "circle\n6", "113.097"),
    ("002_even_or_odd.py", "2", "even"),
    ("002_even_or_odd.py", "7", "odd"),
    ("003_excellent_result.py", "6", "Excellent!"),
    ("003_excellent_result.py", "5", ""),
    ("004_greater_number.py", "5\n3", "5"),
    ("005_number_100_to_200.py", "150", "Between 100 and 200"),
    ("006_password_guess.py", "qwerty", "Wrong password!"),
    ("006_password_guess.py", "s3cr3t!P@ssw0rd", "Welcome"),
    ("007_toy_shop.py", "40.8\n20\n25\n30\n50\n10", "Yes! 418.20 lv left."),
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
