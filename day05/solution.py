import re

with open("input.txt", "r") as input_file:
    input_data = input_file.read().splitlines()
stacks_data = input_data[:9]
commands = input_data[10:]

def get_stacks(stacks_data: list):
    stack_indeces = stacks_data.pop()
    stacks = [[] for _ in range(int(stack_indeces[-1]))]
    for level in stacks_data[::-1]:
        stack_index = 0
        for cell in range(len(level)):
            if cell % 4 == 0:
                stacks[stack_index].append(level[cell+1])
                stack_index += 1
    return stacks

def move_stacks(stacks: list, times: str, origin: str, dest: str):
    for _ in range(int(times)):
        stacks[int(dest)-1].append(stacks[int(origin)-1].pop())

def process_commands(stacks: list, commands: list):
    search_command = re.compile(r"move (\d*) from (\d*) to (\d*)")
    for command in commands:
        result = re.search(search_command, command)
        move_stacks(stacks, *result.groups())

stacks = get_stacks(stacks_data)
print(stacks)
process_commands(stacks, commands)

print(''.join([stack[-1] for stack in stacks]))
print(stacks)
