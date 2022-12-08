from typing import List, Tuple

with open("input.txt", "r") as trees_file:
    trees = trees_file.read().splitlines()

rows = [[int(height) for height in row] for row in trees]
columns = [[int(row[column_index]) for row in trees] for column_index in range(len(trees[0]))]


def check_visibility(
    rows: List[List[int]], columns: List[List[int]], row_index: int, column_index: int
):
    tree_height = rows[row_index][column_index]
    trees_from_left = rows[row_index][0:column_index]
    trees_from_right = rows[row_index][column_index + 1 :]
    trees_from_top = columns[column_index][0:row_index]
    trees_from_bottom = columns[column_index][row_index + 1 :]
    visible_from_left = True
    visible_from_right = True
    visible_from_top = True
    visible_from_bottom = True
    if trees_from_left:
        visible_from_left = all([left_height < tree_height for left_height in trees_from_left])
    if trees_from_right:
        visible_from_right = all([right_height < tree_height for right_height in trees_from_right])
    if trees_from_top:
        visible_from_top = all([top_height < tree_height for top_height in trees_from_top])
    if trees_from_bottom:
        visible_from_bottom = all(
            [bottom_height < tree_height for bottom_height in trees_from_bottom]
        )
    return visible_from_left or visible_from_right or visible_from_top or visible_from_bottom


visibilities = []
for row_index, row_height in enumerate(rows):
    for column_index, column_height in enumerate(columns):
        visibilities.append(check_visibility(rows, columns, row_index, column_index))

print(sum(visibilities))


def count_trees_smaller(tree_height: int, sliced_trees: List[int]):
    trees_smaller = 0
    for sliced_tree_height in sliced_trees:
        if sliced_tree_height < tree_height:
            trees_smaller += 1
        else:
            return trees_smaller + 1
    return trees_smaller


def compute_scenic_score(
    rows: List[List[int]], columns: List[List[int]], row_index: int, column_index: int
):
    trees_from_left = 0
    trees_from_right = 0
    trees_from_top = 0
    trees_from_bottom = 0
    tree_height = rows[row_index][column_index]
    trees_from_left = rows[row_index][0:column_index]
    trees_from_right = rows[row_index][column_index + 1 :]
    trees_from_top = columns[column_index][0:row_index]
    trees_from_bottom = columns[column_index][row_index + 1 :]
    return (
        count_trees_smaller(tree_height, trees_from_left[::-1])
        * count_trees_smaller(tree_height, trees_from_right)
        * count_trees_smaller(tree_height, trees_from_top[::-1])
        * count_trees_smaller(tree_height, trees_from_bottom)
    )


scenic_scores = []
for row_index, row_height in enumerate(rows):
    for column_index, column_height in enumerate(columns):
        scenic_scores.append(compute_scenic_score(rows, columns, row_index, column_index))

print(max(scenic_scores))
