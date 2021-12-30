from file_util import read_line_seperated_data_sets
from print_aoc import finish_task1, finish_task2
import itertools


class BingoBoard:

    def __init__(self, board: list[list[int]]):
        self._board = board
        self._width = len(self._board[0])
        self._height = len(self._board)
        self._matches = self.init_board()
        self._last_number = 0

    def mark_matches(self, num: int) -> None:
        self._last_number = num
        matches_generator = ((x, y) for x, y in self.board_iterator() if self._board[x][y] == num)
        for x, y in matches_generator:
            self._matches[x][y] = True

    def won(self) -> bool:
        return (any(all(row) for row in self._matches) or
                any(all(col) for col in zip(*self._matches)))

    def calc_score(self) -> int:
        return sum((self._board[x][y] for x, y in self.board_iterator() if not self._matches[x][y]))

    def board_iterator(self):
        return itertools.product(range(self._width), range(self._height))

    def init_board(self) -> list[list[bool]]:
        return [[False] * self._width for _ in range(self._height)]

    @property
    def last_number(self) -> int:
        return self._last_number


def to_boards_str(board_matrices: list[str]) -> list[list[list[str]]]:
    return [[line.split() for line in board.split('\n')] for board in board_matrices]


def to_boards_num(boards_str: list[list[list[str]]]) -> list[list[list[int]]]:
    return [[[int(num) for num in line] for line in board] for board in boards_str]


def to_bingo_boards(boards_num: list[[list[int]]]) -> list[BingoBoard]:
    return [BingoBoard(board) for board in boards_num]


def split_nums(numbers_line: str) -> list[int]:
    return [int(num) for num in numbers_line.split(',')]


if __name__ == "__main__":
    numbers_line, *boards = read_line_seperated_data_sets()
    numbers = split_nums(numbers_line)
    bingo_boards = to_bingo_boards(to_boards_num(to_boards_str(boards)))
    winning_boards = []
    for number in numbers:
        for i in range(len(bingo_boards) - 1, -1, -1):
            bingo_boards[i].mark_matches(number)
            if bingo_boards[i].won():
                winning_boards.append(bingo_boards[i])
                bingo_boards.pop(i)
    first = winning_boards[0]
    last = winning_boards[-1]
    finish_task1(4, first.calc_score() * first.last_number, 38594)
    finish_task2(4, last.calc_score() * last.last_number, 21184)
