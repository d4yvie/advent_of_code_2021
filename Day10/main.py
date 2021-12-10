from file_util import read_lines
from functools import reduce
import re


CLOSING_CHARACTERS = [')', ']', '}', '>']
CLOSING_TO_RATING = {')': 3, ']': 57, '}': 1197, '>': 25137}
OPENING_TO_CLOSING = {'(': ')', '[': ']', '{': '}', '<': '>'}


# first I thought of this stack solution but a regex like I used in task2 might be shorter
def task1(lines: list[str]) -> int:
    score = 0
    for line in lines:
        opening_character_stack = []
        for character in line:
            if is_closing(character):
                last_opening = opening_character_stack.pop()
                if not is_fitting_closing(last_opening, character):
                    score += CLOSING_TO_RATING[character]
                    break
            else:
                opening_character_stack.append(character)
    return score


def is_closing(character: str) -> bool:
    return character in CLOSING_CHARACTERS


def is_fitting_closing(opening_char: str, closing_char: str):
    return OPENING_TO_CLOSING[opening_char] == closing_char


def task2(lines: list[str]) -> int:
    scores_of_lines = []
    for line in lines:
        while len(rest_of_line := remove_open_closing_pairs(line)) < len(line):
            line = rest_of_line
        if len(line) and len(re.sub(r"\(|\[|\{|\<", "", line)) < 1:
            scores_of_lines += [reduce(add_to_score_of_line, line[::-1], 0)]
    return sorted(scores_of_lines)[len(scores_of_lines) // 2]


def remove_open_closing_pairs(line: str) -> str:
    return re.sub(r"\(\)|\[\]|\{\}|\<\>", "", line)


def add_to_score_of_line(score: int, character: str) -> int:
    return score * 5 + " ([{<".index(character)


if __name__ == "__main__":
    lines = read_lines()
    print(f"Answer task1: {task1(lines)}")
    print(f"Answer task2: {task2(lines)}")
