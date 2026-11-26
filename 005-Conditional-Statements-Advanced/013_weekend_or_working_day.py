day = input()

if day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print(f"Working day")
elif day in ("Saturday", "Sunday"):
    print(f"Weekend")
else:
    print(f"Error")
