cakes = int(input())
egg_packs = int(input())
cookies_kg = int(input())

total = cakes * 3.20 + egg_packs * 4.35 + cookies_kg * 5.40 + egg_packs * 12 * 0.15
print(f"{total:.2f}")
