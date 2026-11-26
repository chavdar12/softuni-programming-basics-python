tournaments_count = int(input())
start_points = int(input())
won_points = 0
wins = 0

for i in range(tournaments_count):
    stage = input()

    if stage == "W":
        won_points += 2000
        wins += 1
    elif stage == "F":
        won_points += 1200
    elif stage == "SF":
        won_points += 720

print(f"Final points: {start_points + won_points}")
print(f"Average points: {won_points // tournaments_count}")
print(f"{wins / tournaments_count * 100:.2f}%")
