with open('input.txt', 'r') as pairs_file:
    pairs = pairs_file.read().splitlines()

def get_halves_section(section: str):
    first, last = section.split('-')
    return int(first), int(last)

def process_into_tuples(pair: str):
    section1, section2 = pair.split(',')
    section1_first, section1_second = get_halves_section(section1)
    section2_first, section2_second = get_halves_section(section2)
    return [(section1_first, section1_second), (section2_first, section2_second)]

whole_overlaps = 0
for pair in map(process_into_tuples, pairs):
    section1_first, section1_second, section2_first, section2_second = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
    if (section1_first <= section2_first and section1_second >= section2_second) or (section2_first <= section1_first and section2_second >= section1_second):
        whole_overlaps += 1
print(whole_overlaps)

any_overlaps = 0
for pair in map(process_into_tuples, pairs):
    section1_first, section1_second, section2_first, section2_second = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
    if (section1_first <= section2_first and section1_second >= section2_first) or (section2_first <= section1_first and section2_second >= section1_first):
        any_overlaps += 1
print(any_overlaps)
