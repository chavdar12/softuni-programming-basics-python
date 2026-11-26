n = int(input())
counts = {"Hearthstone": 0, "Fornite": 0, "Overwatch": 0, "Others": 0}
for _ in range(n):
    game = input()
    counts[game if game in counts else "Others"] += 1

for game, count in counts.items():
    print(f"{game} - {count / n * 100:.2f}%")
