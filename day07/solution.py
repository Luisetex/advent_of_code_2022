from typing import List

with open("input.txt", "r") as input_file:
    commands = input_file.read().splitlines()


def process_line(line: str, current_directory: str | None, path_traversed: List[str], sizes: dict):
    words = line.split(" ")
    if words[0] == "$":
        if words[1] == "cd":
            if words[2] == "..":
                current_directory = path_traversed.pop()
            else:
                if current_directory:
                    previous_directory = current_directory
                    path_traversed.append(previous_directory)
                    current_directory = words[2]
                else:
                    current_directory = words[2]
                if current_directory not in sizes:
                    complete_path = "_".join(path_traversed + [current_directory])
                    sizes[complete_path] = 0
    elif words[0] != "dir":
        size = int(words[0])
        complete_path = "_".join(path_traversed + [current_directory])
        sizes[complete_path] += size
        if path_traversed:
            for directory_index in range(len(path_traversed)):
                sizes["_".join(path_traversed[: directory_index + 1])] += size

    return current_directory, path_traversed, sizes


def get_sizes(lines: List[str]):
    current_directory = None
    path_traversed = []
    sizes = {}
    for line in lines:
        current_directory, path_traversed, sizes = process_line(
            line, current_directory, path_traversed, sizes
        )
    return sizes


sizes = get_sizes(commands)
print(sum([size for _, size in sizes.items() if size <= 100000]))

TOTAL_DISK_AVAILABLE = 70000000
AMOUNT_NEEDED_FOR_UPDATE = 30000000

in_use_size = sizes["/"]
print(
    min(
        [
            size
            for _, size in sizes.items()
            if (TOTAL_DISK_AVAILABLE - in_use_size + size >= AMOUNT_NEEDED_FOR_UPDATE)
        ]
    )
)
