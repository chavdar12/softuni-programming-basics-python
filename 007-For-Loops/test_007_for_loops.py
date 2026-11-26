"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_character_sequence.py", "abc", "a\nb\nc"),
    ("002_clever_lily.py", "10\n170\n6", "Yes! 5.00"),
    ("003_even_powers_of_2.py", "4", "1\n4\n16"),
    ("004_left_and_right_sum.py", "2\n10\n90\n60\n40", "Yes, sum = 100"),
    ("005_min_max_number.py", "3\n1\n-3\n5", "Max number: 5\nMin number: -3"),
    (
        "006_numbers_1_to_100.py",
        "",
        "1\n"
        "2\n"
        "3\n"
        "4\n"
        "5\n"
        "6\n"
        "7\n"
        "8\n"
        "9\n"
        "10\n"
        "11\n"
        "12\n"
        "13\n"
        "14\n"
        "15\n"
        "16\n"
        "17\n"
        "18\n"
        "19\n"
        "20\n"
        "21\n"
        "22\n"
        "23\n"
        "24\n"
        "25\n"
        "26\n"
        "27\n"
        "28\n"
        "29\n"
        "30\n"
        "31\n"
        "32\n"
        "33\n"
        "34\n"
        "35\n"
        "36\n"
        "37\n"
        "38\n"
        "39\n"
        "40\n"
        "41\n"
        "42\n"
        "43\n"
        "44\n"
        "45\n"
        "46\n"
        "47\n"
        "48\n"
        "49\n"
        "50\n"
        "51\n"
        "52\n"
        "53\n"
        "54\n"
        "55\n"
        "56\n"
        "57\n"
        "58\n"
        "59\n"
        "60\n"
        "61\n"
        "62\n"
        "63\n"
        "64\n"
        "65\n"
        "66\n"
        "67\n"
        "68\n"
        "69\n"
        "70\n"
        "71\n"
        "72\n"
        "73\n"
        "74\n"
        "75\n"
        "76\n"
        "77\n"
        "78\n"
        "79\n"
        "80\n"
        "81\n"
        "82\n"
        "83\n"
        "84\n"
        "85\n"
        "86\n"
        "87\n"
        "88\n"
        "89\n"
        "90\n"
        "91\n"
        "92\n"
        "93\n"
        "94\n"
        "95\n"
        "96\n"
        "97\n"
        "98\n"
        "99\n"
        "100",
    ),
    ("007_numbers_n_to_1.py", "3", "3\n2\n1"),
    ("008_numbers_1_to_n_step_3.py", "10", "1\n4\n7\n10"),
    ("009_sum_numbers.py", "2\n10\n20", "30"),
    ("010_vowels_sum.py", "hello", "6"),
    ("011_odd_even_sum.py", "4\n10\n50\n60\n20", "Yes\nSum = 70"),
    ("011_odd_even_sum.py", "4\n3\n5\n1\n-2", "No\nDiff = 1"),
    ("011_odd_even_sum.py", "3\n5\n8\n1", "No\nDiff = 2"),
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
