"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    (
        "001_account_balance.py",
        "5.51\n69.42\n100\nNoMoreMoney",
        "Increase: 5.51\nIncrease: 69.42\nIncrease: 100.00\nTotal: 174.93",
    ),
    ("001_account_balance.py", "10\n-5", "Increase: 10.00\nInvalid operation!\nTotal: 10.00"),
    (
        "002_graduation.py",
        "Gosho\n5\n5.5\n6\n5.43\n5.5\n6\n5.55\n5\n6\n6\n5.43\n5",
        "Gosho graduated. Average grade: 5.53",
    ),
    ("002_graduation.py", "Mimi\n5\n6\n2\n3", "Mimi has been excluded at 3 grade"),
    ("003_max_number.py", "100\n99\n80\n70\nStop", "100"),
    ("004_min_number.py", "100\n99\n80\n70\nStop", "70"),
    (
        "005_moving.py",
        "10\n10\n2\n20\n20\n20\n20\n122",
        "No more free space! You need 2 Cubic meters more.",
    ),
    ("005_moving.py", "10\n1\n2\n4\n6\nDone", "10 Cubic meters left."),
    ("006_password.py", "Nakov\n1234\npass\n1324\n1234", "Welcome Nakov!"),
    ("007_read_text.py", "Nakov\nSoftUni\nStop", "Nakov\nSoftUni"),
    ("008_sequence_2k_plus_1.py", "31", "1\n3\n7\n15\n31"),
    ("009_sum_numbers.py", "100\n10\n20\n30\n40", "100"),
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
