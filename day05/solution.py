import re

with open("input.txt", "r") as input_file:
    input_data = input_file.read().splitlines()
stacks_data = input_data[:9]
commands = input_data[10:]


def get_stacks(stacks_data: list):
    stack_indeces = stacks_data[-1]
    stacks = [[] for _ in range(int(stack_indeces[-1]))]
    for level in stacks_data[-2::-1]:
        stack_index = 0
        for cell in range(len(level)):
            if cell % 4 == 0:
                if level[cell + 1] != " ":
                    stacks[stack_index].append(level[cell + 1])
                stack_index += 1
    return stacks


def move_stacks(stacks: list, times: str, origin: str, dest: str):
    for _ in range(int(times)):
        stacks[int(dest) - 1].append(stacks[int(origin) - 1].pop())


def move_stacks_multiple(stacks: list, times: str, origin: str, dest: str):
    slice_end = int("-" + times)
    slice_origin = int(origin) - 1
    slice_destination = int(dest) - 1
    to_move = stacks[int(origin) - 1][slice_end:]
    stacks[slice_origin] = stacks[slice_origin][:slice_end]
    stacks[slice_destination] += to_move


def process_commands(stacks: list, commands: list, method):
    search_command = re.compile(r"move (\d*) from (\d*) to (\d*)")
    for command in commands:
        result = re.search(search_command, command)
        method(stacks, *result.groups())


stacks = get_stacks(stacks_data)
process_commands(stacks, commands, move_stacks)
print("".join([stack[-1] for stack in stacks]))

stacks = get_stacks(stacks_data)
process_commands(stacks, commands, move_stacks_multiple)
print("".join([stack[-1] for stack in stacks]))
