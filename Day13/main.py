from file_util import read_line_seperated_data_sets
from print_aoc import print_task1


def parse_dots(dots: str) -> set[tuple[int, int]]:
    return {tuple(map(int, line.split(","))) for line in dots.split("\n")}


def task1(dots: set[tuple[int, int]], folds: str) -> tuple[set[tuple[int, int]], int]:
    for index, line in enumerate(folds.split("\n")):
        coordinate, fold_number = line.split()[-1].split("=")
        fold_number = int(fold_number)
        for x, y in list(dots):
            dots.remove((x, y))
            if coordinate == "x" and x > fold_number:
                x = 2 * fold_number - x
            if coordinate == "y" and y > fold_number:
                y = 2 * fold_number - y
            dots.add((x, y))
        if index == 0:
            dots_first_fold = len(dots)
    return dots, dots_first_fold


def task2(dots: set[tuple[int, int]]) -> None:
    max_x, max_y = zip(*dots)
    for y in range(max(max_y) + 1):
        for x in range(max(max_x) + 1):
            print(" #"[(x, y) in dots], end="")
        print()


if __name__ == "__main__":
    dots, folds = read_line_seperated_data_sets()
    dots, points_first_fold = task1(parse_dots(dots), folds)
    print_task1(13, points_first_fold)
    print("The code is: ")
    task2(dots)
