PRICES = {
    "one": {"Small": 9.98, "Middle": 18.99, "Large": 25.98, "ExtraLarge": 35.99},
    "two": {"Small": 8.58, "Middle": 17.09, "Large": 23.59, "ExtraLarge": 31.79},
}

term = input()
contract = input()
internet = input()
months = int(input())

monthly = PRICES[term][contract]
if internet == "yes":
    monthly += 5.50 if monthly <= 10 else 4.35 if monthly <= 30 else 3.85

total = monthly * months
if term == "two":
    total *= 1 - 0.0375
print(f"{total:.2f} lv.")
