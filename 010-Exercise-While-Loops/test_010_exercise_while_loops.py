"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_cake.py", "10\n10\n20\n20\n20\n20\n21", "No more cake left! You need 1 pieces more."),
    ("001_cake.py", "10\n2\n2\n4\n6\nSTOP", "8 pieces are left."),
    ("002_coins.py", "1.23", "4"),
    ("002_coins.py", "1.15", "3"),
    (
        "003_exam_preparation.py",
        "3\nMoney\n6\nStory\n4\nSpring Time\n5\nBus\n6\nEnough",
        "Average score: 5.25\nNumber of problems: 4\nLast problem: Bus",
    ),
    (
        "003_exam_preparation.py",
        "2\nIncome\n3\nGame Info\n6\nBest Player\n4",
        "You need a break, 2 poor grades.",
    ),
    ("004_old_books.py", "Troy\nStronger\nLife Style\nTroy", "You checked 2 books and found it."),
    (
        "004_old_books.py",
        "The Spot\nHunger Games\nHarry Potter\nTorronto\nSpotify\nNo More Books",
        "The book you search is not here!\nYou checked 4 books.",
    ),
    ("005_vacation.py", "2000\n1000\nspend\n1200\nsave\n2000", "You saved the money for 2 days."),
    (
        "005_vacation.py",
        "110\n60\nspend\n10\nspend\n10\nspend\n10\nspend\n10\nspend\n10",
        "You can't save the money.\n5",
    ),
    (
        "006_walking.py",
        "1000\n1500\n2000\n6500",
        "Goal reached! Good job!\n1000 steps over the goal!",
    ),
    ("006_walking.py", "1500\n300\n2500\n3000\nGoing home\n200", "2500 more steps to reach goal."),
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
