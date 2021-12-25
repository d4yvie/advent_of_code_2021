from aoc_types import Vector2D
from file_util import read_lines
from print_aoc import finish_task1
from functools import reduce
from itertools import count
from cucumber_token import CucumberToken


CucumberList = set[Vector2D]
StepParams = tuple[int, int, int, CucumberList]


def get_cucumber_coordinates_by_type(lines: list[str], cucumber_type: CucumberToken, vertical_length: int, horizontal_length: int) -> CucumberList:
    return {(i, j) for i in range(vertical_length) for j in range(horizontal_length) if lines[i][j] == cucumber_type.value}


def attempt_to_move_cucumbers_once(right_moving: CucumberList, down_moving: CucumberList, vertical_length: int, horizontal_length: int) -> tuple[CucumberList, CucumberList]:
    to_check = right_moving | down_moving
    right_moving_after_step = reduce(attempt_to_move_right, create_reduce_params(right_moving, horizontal_length, to_check), set())
    to_check = right_moving_after_step | down_moving
    down_moving_after_step = reduce(attempt_to_move_down, create_reduce_params(down_moving, vertical_length, to_check), set())
    return right_moving_after_step, down_moving_after_step


def attempt_to_move_right(right_moving: CucumberList, params: StepParams) -> CucumberList:
    x, y, length, to_check = params
    new_loc = (x, (y + 1) % length)
    return add_if_not_in_list(right_moving, to_check, (x, y), new_loc)


def attempt_to_move_down(down_moving: CucumberList, params: StepParams) -> CucumberList:
    x, y, length, to_check = params
    new_loc = ((x + 1) % length, y)
    return add_if_not_in_list(down_moving, to_check, (x, y), new_loc)


def add_if_not_in_list(cucumber_list: CucumberList, to_check: CucumberList, location_before_step: Vector2D, location_after_step: Vector2D) -> CucumberList:
    cucumber_list.add(location_before_step if location_after_step in to_check else location_after_step)
    return cucumber_list


def create_reduce_params(cucumber_coordinates: set[Vector2D], length: int, to_check: CucumberList) -> list[StepParams]:
    return [(cucumber_coordinate[0], cucumber_coordinate[1], length, to_check) for cucumber_coordinate in cucumber_coordinates]


def count_steps_until_not_moving(rights: CucumberList, downs: CucumberList, vertical_length: int, horizontal_length: int) -> int:
    for c in count(1):
        new_rights, new_downs = attempt_to_move_cucumbers_once(rights, downs, vertical_length, horizontal_length)
        if rights == new_rights and downs == new_downs:
            return c
        rights = new_rights
        downs = new_downs


if __name__ == '__main__':
    lines = read_lines()
    vertical_length = len(lines)
    horizontal_length = len(lines[0])
    right_moving_cucumbers = get_cucumber_coordinates_by_type(lines, CucumberToken.RIGHT, vertical_length, horizontal_length)
    down_moving_cucumbers = get_cucumber_coordinates_by_type(lines, CucumberToken.DOWN, vertical_length, horizontal_length)
    finish_task1(25, count_steps_until_not_moving(right_moving_cucumbers, down_moving_cucumbers, vertical_length, horizontal_length), 571)
