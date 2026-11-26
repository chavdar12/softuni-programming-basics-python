"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_equal_sums_even_odd_position.py", "10\n30", "11 22"),
    ("002_number_pyramid.py", "7", "1\n2 3\n4 5 6\n7"),
    ("003_password_generator.py", "2\n1", "11aa2"),
    (
        "004_special_numbers.py",
        "3",
        "1111 1113 1131 1133 1311 1313 1331 1333 3111 3113 3131 3133 3311 3313 3331 3333",
    ),
    (
        "005_sum_prime_non_prime.py",
        "3\n9\n0\n7\n19\n4\nstop",
        "Sum of all prime numbers is: 29\nSum of all non prime numbers is: 13",
    ),
    (
        "005_sum_prime_non_prime.py",
        "-5\nstop",
        "Number is negative.\nSum of all prime numbers is: 0\nSum of all non prime numbers is: 0",
    ),
    (
        "006_train_the_trainers.py",
        "2\nWhile-Loop\n6.0\n5.5\nFor-Loop\n5.84\n5.66\nFinish",
        "While-Loop - 5.75.\nFor-Loop - 5.75.\nStudent's final assessment is 5.75.",
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
