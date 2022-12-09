from functools import reduce

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt", "r") as rucksack_file:
    rucksacks = rucksack_file.read().splitlines()


def split_rucksack(rucksack: str):
    half_index = int(len(rucksack) / 2)
    part_1, part_2 = rucksack[:half_index], rucksack[half_index:]
    return [part_1, part_2]


def get_priority(splitted_rucksack):
    part_1, part_2 = splitted_rucksack[0], splitted_rucksack[1]
    duplicate_letter = next(filter(lambda letter: letter in part_2, [*part_1]))
    return priorities.index(duplicate_letter) + 1


print(
    reduce(
        lambda sum, priority: sum + priority,
        map(get_priority, map(lambda x: x, map(split_rucksack, rucksacks))),
        0,
    )
)


def group_rucksacks(rucksacks, index):
    return [rucksacks[index], rucksacks[index + 1], rucksacks[index + 2]]


def get_duplicate_in_group(rucksack_group):
    duplicate_letter = next(
        filter(
            lambda letter: letter in rucksack_group[1] and letter in rucksack_group[2],
            [*rucksack_group[0]],
        )
    )
    return priorities.index(duplicate_letter) + 1


print(
    reduce(
        lambda sum, priority: sum + priority,
        map(
            get_duplicate_in_group,
            map(
                lambda index: group_rucksacks(rucksacks, index),
                range(0, len(rucksacks), 3),
            ),
        ),
        0,
    )
)
