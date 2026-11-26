"""Runs every script in this lesson with the example input from the course PDF and checks its output."""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [
    ("001_divide_without_remainder.py", "3\n3\n6\n9", "33.33%\n100.00%\n0.00%"),
    ("002_half_sum_element.py", "3\n3\n4\n1", "Yes\nSum = 4"),
    ("002_half_sum_element.py", "2\n1\n5", "No\nDiff = 4"),
    ("003_histogram.py", "3\n1\n450\n900", "33.33%\n0.00%\n33.33%\n0.00%\n33.33%"),
    (
        "004_numbers_ending_in_7.py",
        "",
        "7\n"
        "17\n"
        "27\n"
        "37\n"
        "47\n"
        "57\n"
        "67\n"
        "77\n"
        "87\n"
        "97\n"
        "107\n"
        "117\n"
        "127\n"
        "137\n"
        "147\n"
        "157\n"
        "167\n"
        "177\n"
        "187\n"
        "197\n"
        "207\n"
        "217\n"
        "227\n"
        "237\n"
        "247\n"
        "257\n"
        "267\n"
        "277\n"
        "287\n"
        "297\n"
        "307\n"
        "317\n"
        "327\n"
        "337\n"
        "347\n"
        "357\n"
        "367\n"
        "377\n"
        "387\n"
        "397\n"
        "407\n"
        "417\n"
        "427\n"
        "437\n"
        "447\n"
        "457\n"
        "467\n"
        "477\n"
        "487\n"
        "497\n"
        "507\n"
        "517\n"
        "527\n"
        "537\n"
        "547\n"
        "557\n"
        "567\n"
        "577\n"
        "587\n"
        "597\n"
        "607\n"
        "617\n"
        "627\n"
        "637\n"
        "647\n"
        "657\n"
        "667\n"
        "677\n"
        "687\n"
        "697\n"
        "707\n"
        "717\n"
        "727\n"
        "737\n"
        "747\n"
        "757\n"
        "767\n"
        "777\n"
        "787\n"
        "797\n"
        "807\n"
        "817\n"
        "827\n"
        "837\n"
        "847\n"
        "857\n"
        "867\n"
        "877\n"
        "887\n"
        "897\n"
        "907\n"
        "917\n"
        "927\n"
        "937\n"
        "947\n"
        "957\n"
        "967\n"
        "977\n"
        "987\n"
        "997",
    ),
    (
        "005_odd_even_position.py",
        "2\n1.5\n-2.5",
        "OddSum=1.50,\nOddMin=1.50,\nOddMax=1.50,\nEvenSum=-2.50,\nEvenMin=-2.50,\nEvenMax=-2.50",
    ),
    (
        "005_odd_even_position.py",
        "1\n1",
        "OddSum=1.00,\nOddMin=1.00,\nOddMax=1.00,\nEvenSum=0.00,\nEvenMin=No,\nEvenMax=No",
    ),
    ("006_salary.py", "3\n500\nFacebook\nInstagram\nReddit", "200"),
    ("006_salary.py", "2\n200\nFacebook\nFacebook", "You have lost your salary."),
    (
        "007_oscars.py",
        "Zahari Baharov\n205\n4\nJohnny Depp\n45\nWill Smith\n29\nJet Lee\n10\nMatthew Mcconaughey\n39",
        "Sorry, Zahari Baharov you need 247.5 more!",
    ),
    (
        "007_oscars.py",
        "Sandra Bullock\n340\n5\nRobert De Niro\n50\nJulia Roberts\n40.5\nDaniel Day-Lewis\n39.4\nNicolas Cage\n29.9\nStoyanka Mutafova\n33",
        "Congratulations, Sandra Bullock got a nominee for leading role with 1268.5!",
    ),
    (
        "008_trekking_mania.py",
        "10\n10\n5\n1\n100\n12\n26\n17\n37\n40\n78",
        "1.84%\n6.75%\n5.21%\n31.60%\n54.60%",
    ),
    ("008_trekking_mania.py", "5\n25\n41\n31\n250\n6", "0.00%\n1.70%\n7.08%\n8.78%\n82.44%"),
    (
        "009_tennis_ranklist.py",
        "5\n1400\nF\nSF\nW\nW\nSF",
        "Final points: 8040\nAverage points: 1328\n40.00%",
    ),
    (
        "009_tennis_ranklist.py",
        "4\n750\nSF\nW\nSF\nW",
        "Final points: 6190\nAverage points: 1360\n50.00%",
    ),
    (
        "009_tennis_ranklist.py",
        "7\n1200\nSF\nF\nW\nF\nW\nSF\nW",
        "Final points: 11040\nAverage points: 1405\n42.86%",
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
