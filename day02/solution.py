with open('input.txt', 'r') as input_file:
    strategy_guide = input_file.read().splitlines()

WIN_POINTS = 6
DRAW_POINTS = 3
LOSE_POINTS = 0

own_to_opponent = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}
selection_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def rock_paper_scissors(opponent: str, own: str):
    own_converted = own_to_opponent[own]
    if opponent == own_converted:
        return DRAW_POINTS + selection_points[own]
    if opponent == 'A' and own_converted == 'B' or opponent == 'B' and own_converted == 'C' or opponent == 'C' and own_converted == 'A':
        return WIN_POINTS + selection_points[own]
    return LOSE_POINTS + selection_points[own]

print(sum([rock_paper_scissors(match[0], match[2]) for match in strategy_guide]))

result_points = {
    'X': LOSE_POINTS,
    'Y': DRAW_POINTS,
    'Z': WIN_POINTS
}

def get_points_2(opponent: str, result: str):
    if (result == 'Z' and opponent == 'C' or result == 'X' and opponent == 'B' or result == 'Y' and opponent == 'A'):
        return result_points[result] + 1
    if (result == 'Z' and opponent == 'A' or result == 'X' and opponent == 'C' or result == 'Y' and opponent == 'B'):
        return result_points[result] + 2
    if (result == 'Z' and opponent == 'B' or result == 'X' and opponent == 'A' or result == 'Y' and opponent == 'C'):
        return result_points[result] + 3

print(sum([get_points_2(match[0], match[2]) for match in strategy_guide]))

