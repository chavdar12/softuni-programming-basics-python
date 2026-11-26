actor_name = input()
points = float(input())
evaluators_count = int(input())

for i in range(evaluators_count):
    evaluator_name = input()
    evaluator_points = float(input())
    points += len(evaluator_name) * evaluator_points / 2

    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points:.1f} more!")
