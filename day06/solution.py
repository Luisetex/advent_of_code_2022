from functools import reduce

with open("input.txt", "r") as input_file:
    packet = input_file.read()


def check_4_equal(string: str, substring_length: int):
    for index in range(len(string)):
        substring = string[index : index + substring_length]
        substring_set = set(substring)
        if len(substring_set) == len(substring):
            return index + substring_length


print(check_4_equal(packet, 4))
print(check_4_equal(packet, 14))
