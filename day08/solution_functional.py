from functools import reduce
from typing import List, Tuple

with open("input.txt", "r") as trees_file:
    trees = trees_file.read().splitlines()

rows = list(map(lambda line: list(map(int, line)), trees))
columns = list(
    map(lambda column: list(map(lambda row: int(row[column]), rows)), range(len(trees[0])))
)


def get_visibility(rows, columns, row_index, column_index):
    tree_height = rows[row_index][column_index]
    trees_from_left = rows[row_index][0:column_index]
    trees_from_right = rows[row_index][column_index + 1 :]
    trees_from_top = columns[column_index][0:row_index]
    trees_from_bottom = columns[column_index][row_index + 1 :]

    visible_from_left = (
        all(map(lambda left_height: left_height < tree_height, trees_from_left))
        if trees_from_left
        else True
    )

    visible_from_right = (
        all(map(lambda right_height: right_height < tree_height, trees_from_right))
        if trees_from_left
        else True
    )
    visible_from_top = (
        all(map(lambda top_height: top_height < tree_height, trees_from_top))
        if trees_from_top
        else True
    )
    visible_from_bottom = (
        all(map(lambda bottom_height: bottom_height < tree_height, trees_from_bottom))
        if trees_from_bottom
        else True
    )
    return visible_from_left or visible_from_right or visible_from_top or visible_from_bottom


visible_trees = map(
    lambda row_index: map(
        lambda column_index: get_visibility(rows, columns, row_index, column_index),
        range(len(rows)),
    ),
    range(len(rows)),
)

result = reduce(
    lambda x, y: x + y, reduce(lambda row1, row2: list(row1) + list(row2), visible_trees, []), 0
)

print(result)


def count_smaller(tree_height: int, sliced_array: List[int]):
    bigger_filtered = list(filter(lambda height: height >= tree_height, sliced_array))
    if not bigger_filtered:
        return len(sliced_array)
    first_bigger_index = sliced_array.index(bigger_filtered[0]) if sliced_array else -1
    return len(sliced_array[: first_bigger_index + 1])


def compute_scenic_score(rows, columns, row_index, column_index):
    tree_height = rows[row_index][column_index]
    slices = [
        rows[row_index][0:column_index][::-1],
        rows[row_index][column_index + 1 :],
        columns[column_index][0:row_index][::-1],
        columns[column_index][row_index + 1 :],
    ]
    return reduce(lambda acc, slice: acc * count_smaller(tree_height, slice), slices, 1)


scenic_scores = map(
    lambda row_index: map(
        lambda columm_index: compute_scenic_score(rows, columns, row_index, columm_index),
        range(len(columns)),
    ),
    range(len(rows)),
)

print(max(reduce(lambda row1, row2: list(row1) + list(row2), scenic_scores, [])))
