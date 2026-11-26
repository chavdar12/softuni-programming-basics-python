budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_price = video_cards_count * 250
processors_price = processors_count * video_cards_price * 0.35
ram_price = ram_count * video_cards_price * 0.10
total = video_cards_price + processors_price + ram_price

if video_cards_count > processors_count:
    total *= 0.85

if total <= budget:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
