from file_util import read_line_seperated_data_sets


class BingoBoard:

    def __init__(self, board: list[list[int]]):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.matches = self.init_board()
        self._last_number = 0

    def mark_matches(self, num: int) -> None:
        self._last_number = num
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] == num:
                    self.matches[x][y] = True

    def won(self) -> bool:
        return (any(all(row) for row in self.matches) or
                any(all(col) for col in zip(*self.matches)))

    def calc_score(self) -> int:
        score = 0
        for x in range(self.width):
            for y in range(self.height):
                if not self.matches[x][y]:
                    score += int(self.board[x][y])
        return score

    def init_board(self) -> list[list[bool]]:
        return [[False] * self.width for _ in range(self.height)]

    @property
    def last_number(self) -> int:
        return self._last_number


def to_boards_str(board_matrices: list[str]) -> list[list[list[str]]]:
    return [[line.split() for line in board.split('\n')] for board in board_matrices]


def to_boards_num(boards_str: list[list[list[str]]]) -> list[list[list[int]]]:
    return [[[int(elt) for elt in line] for line in board] for board in boards_str]


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
    print(first.calc_score() * first.last_number)
    print(last.calc_score() * last.last_number)
