"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_easter_lunch.py", "3\n2\n3", "38.10"),
    ("001_easter_lunch.py", "4\n4\n3", "53.60"),
    ("001_easter_lunch.py", "2\n3\n2", "35.65"),
    (
        "002_football_results.py",
        "3:1\n0:2\n0:0",
        "Team won 1 games.\nTeam lost 1 games.\nDrawn games: 1",
    ),
    (
        "002_football_results.py",
        "4:2\n0:3\n1:0",
        "Team won 2 games.\nTeam lost 1 games.\nDrawn games: 0",
    ),
    (
        "002_football_results.py",
        "0:2\n0:1\n3:3",
        "Team won 0 games.\nTeam lost 2 games.\nDrawn games: 1",
    ),
    ("003_mobile_operator.py", "one\nSmall\nyes\n10", "154.80 lv."),
    ("003_mobile_operator.py", "two\nLarge\nno\n10", "227.05 lv."),
    ("003_mobile_operator.py", "two\nExtraLarge\nyes\n20", "686.07 lv."),
    ("003_mobile_operator.py", "two\nSmall\nyes\n20", "271.04 lv."),
    (
        "004_game_store.py",
        "4\nHearthstone\nFornite\nOverwatch\nCounter-Strike",
        "Hearthstone - 25.00%\nFornite - 25.00%\nOverwatch - 25.00%\nOthers - 25.00%",
    ),
    (
        "004_game_store.py",
        "3\nHearthstone\nDiablo 2\nStar Craft 2",
        "Hearthstone - 33.33%\nFornite - 0.00%\nOverwatch - 0.00%\nOthers - 66.67%",
    ),
    (
        "005_suitcases_load.py",
        "550\n100\n252\n72\nEnd",
        "Congratulations! All suitcases are loaded!\nStatistic: 3 suitcases loaded.",
    ),
    (
        "005_suitcases_load.py",
        "700.5\n180\n340.6\n126\n220",
        "No more space!\nStatistic: 3 suitcases loaded.",
    ),
    (
        "005_suitcases_load.py",
        "1200.2\n260\n380.5\n125.6\n305\nEnd",
        "Congratulations! All suitcases are loaded!\nStatistic: 4 suitcases loaded.",
    ),
    (
        "006_christmas_tournament.py",
        "2\n"
        "volleyball\n"
        "win\n"
        "football\n"
        "lose\n"
        "basketball\n"
        "win\n"
        "Finish\n"
        "golf\n"
        "win\n"
        "tennis\n"
        "win\n"
        "badminton\n"
        "win\n"
        "Finish",
        "You won the tournament! Total raised money: 132.00",
    ),
    (
        "006_christmas_tournament.py",
        "3\n"
        "darts\n"
        "lose\n"
        "handball\n"
        "lose\n"
        "judo\n"
        "win\n"
        "Finish\n"
        "snooker\n"
        "lose\n"
        "swimming\n"
        "lose\n"
        "squash\n"
        "lose\n"
        "table tennis\n"
        "win\n"
        "Finish\n"
        "volleyball\n"
        "win\n"
        "basketball\n"
        "win\n"
        "Finish",
        "You lost the tournament! Total raised money: 84.00",
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
