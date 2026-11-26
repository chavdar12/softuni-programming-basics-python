groups_count = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(groups_count):
    people = int(input())

    if people <= 5:
        musala += people
    elif people <= 12:
        monblan += people
    elif people <= 25:
        kilimanjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people

total = musala + monblan + kilimanjaro + k2 + everest

for climbers in (musala, monblan, kilimanjaro, k2, everest):
    print(f"{climbers / total * 100:.2f}%")
