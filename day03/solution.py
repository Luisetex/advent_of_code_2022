priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_priority(item: str):
    return priorities.index(item) + 1

with open('input.txt', 'r') as rucksack_file:
    rucksacks = rucksack_file.read().splitlines()


duplicated_item_priorities = []
for rucksack in rucksacks:
    half_index = int(len(rucksack)/2)
    first_half, second_half = rucksack[:half_index], rucksack[half_index:]
    for item in first_half:
        if item in second_half:
            duplicated_item_priorities.append(get_priority(item))
            break

print(sum(duplicated_item_priorities))

badges_priorities = []
for first_rucksack_index in range(0, len(rucksacks), 3):
    for item in rucksacks[first_rucksack_index]:
        if item in rucksacks[first_rucksack_index+1] and item in rucksacks[first_rucksack_index+2]:
            badges_priorities.append(get_priority(item))
            break

print(sum(badges_priorities))
