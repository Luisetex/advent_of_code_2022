from functools import reduce

with open("input.txt", "r") as input_file:
    calories = input_file.read().splitlines()


def sum_calories(all_calories, calories):
    if calories == "":
        all_calories.append(0)
        return all_calories
    all_calories[-1] += int(calories)
    return all_calories


calories_per_elf = reduce(sum_calories, calories, [0])

print(max(calories_per_elf))

calories_per_elf.sort(reverse=True)

print(reduce(lambda x, y: x + y, calories_per_elf[:3], 0))
