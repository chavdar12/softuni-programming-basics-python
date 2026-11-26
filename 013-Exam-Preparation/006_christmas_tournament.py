days = int(input())
total = 0
won_days = 0

for _ in range(days):
    day_money = 0
    wins = losses = 0
    sport = input()
    while sport != "Finish":
        if input() == "win":
            wins += 1
            day_money += 20
        else:
            losses += 1
        sport = input()
    if wins > losses:
        day_money *= 1.10
        won_days += 1
    total += day_money

if won_days > days - won_days:
    print(f"You won the tournament! Total raised money: {total * 1.20:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total:.2f}")
