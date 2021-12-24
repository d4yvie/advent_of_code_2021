from typing import Callable
from aoc_types import Vector2D
from file_util import read_lines
from print_aoc import finish_task1, finish_task2
from functools import reduce


Program = list[list[str]]
ModelNumber = list[int]
ModelNumberCreator = Callable[[ModelNumber, int, int, int], ModelNumber]
Stack = list[Vector2D]
StackParams = tuple[int, Program, Stack, ModelNumberCreator]


def add_digits_for_largest_model_number(largest_model_number: ModelNumber, i: int, j: int, n: int) -> ModelNumber:
    if n > 0:
        largest_model_number[i] = 9
        largest_model_number[j] = 9 - n
    else:
        largest_model_number[i] = 9 + n
        largest_model_number[j] = 9
    return largest_model_number


def add_digits_for_smallest_model_number(smallest_model_number: ModelNumber, i: int, j: int, n: int) -> ModelNumber:
    if n > 0:
        smallest_model_number[i] = 1 + n
        smallest_model_number[j] = 1
    else:
        smallest_model_number[i] = 1
        smallest_model_number[j] = 1 - n
    return smallest_model_number


def create_model_number(program: Program, creator: ModelNumberCreator, stack=[]) -> str:
    param_list = [(x, program, stack, creator) for x in range(14)]
    model_number = reduce(do_model_number_step, param_list, [0] * 14)
    return reduce(lambda a, b: f"{a}{b}", model_number, "")


def do_model_number_step(model_number: ModelNumber, params: StackParams) -> ModelNumber:
    i, program, stack, model_number_creator = params
    if program[18 * i + 4][-1] == "1":
        stack.append((i, int(program[18 * i + 15][-1])))
    else:
        j, n = stack.pop()
        n += int(program[18 * i + 5][-1])
        return model_number_creator(model_number, i, j, n)
    return model_number


if __name__ == '__main__':
    prog = [line.split() for line in read_lines()]
    finish_task1(24, create_model_number(prog, add_digits_for_largest_model_number), "91699394894995")
    finish_task2(24, create_model_number(prog, add_digits_for_smallest_model_number), "51147191161261")
