capacity = float(input())
loaded = 0

command = input()
while command != "End":
    volume = float(command)
    if (loaded + 1) % 3 == 0:
        volume *= 1.10  # every third suitcase takes 10% more space
    if volume > capacity:
        print("No more space!")
        break
    capacity -= volume
    loaded += 1
    command = input()
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {loaded} suitcases loaded.")
