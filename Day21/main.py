from file_util import read_lines
from functools import lru_cache
from print_aoc import print_task1, print_task2


Point2D = tuple[int, int]


def determinate_player_index(throws: int) -> int:
    return (throws // 3) % 2


def task1(positions: list[int, int]) -> int:
    scores = [0, 0]
    throws = 0
    while True:
        player = determinate_player_index(throws)
        for _ in range(3):
            throw = throws % 100 + 1
            positions[player] = (positions[player] + throw - 1) % 10 + 1
            throws += 1
        scores[player] += positions[player]
        if scores[player] >= 1000:
            return scores[1 - player] * throws


@lru_cache(maxsize=None)
def task2(scores: Point2D, positions: Point2D, turn: int) -> Point2D:
    if scores[0] >= 21:
        return 1, 0
    if scores[1] >= 21:
        return 0, 1
    wins1, wins2 = 0, 0
    for i in range(3):
        player = determinate_player_index(turn)
        recursive_pos = (positions[player] + i) % 10 + 1
        score = scores[player] + (turn % 3 == 2 and recursive_pos)
        recursive_win1, recursive_win1 = task2(
            (scores[0], score) if player == 1 else (score, scores[1]),
            (positions[0], recursive_pos) if player == 1 else (recursive_pos, positions[1]),
            (turn + 1) % 6,
        )
        wins1 += recursive_win1
        wins2 += recursive_win1
    return wins1, wins2


if __name__ == '__main__':
    positions = [int(line.split()[-1]) for line in read_lines()]
    print_task1(21, task1(positions))
    print_task2(21, max(task2((0, 0), tuple(positions), 0)))
