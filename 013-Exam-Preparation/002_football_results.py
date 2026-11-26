won = lost = drawn = 0
for _ in range(3):
    home, away = map(int, input().split(":"))
    if home > away:
        won += 1
    elif home < away:
        lost += 1
    else:
        drawn += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
