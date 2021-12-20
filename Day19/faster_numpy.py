from collections import defaultdict
from itertools import combinations, permutations, product
from file_util import read_line_seperated_data_sets
from functools import reduce
from print_aoc import print_task1, print_task2
import re
import numpy as np
import cProfile

Vector3 = tuple[int, int, int]


def create_rotations() -> list[np.array]:
    return reduce(create_rotation, permutations((0, 1, 2), 3), [])


def create_rotation(rotations, permutation) -> list[np.array]:
    rotations.extend([a for signs in product((-1, 1), repeat=3) if np.linalg.det(a := np.diag(signs)[:, permutation]) > 0])
    return rotations


def parse_scanners() -> list[np.array]:
    data_sets = read_line_seperated_data_sets()
    return list(map(parse_scanner, data_sets))


def parse_scanner(data_set: str) -> np.array:
    data_of_one_scanner = data_set.split("\n")[1:]
    return np.array([list(map(int, re.findall("-?\d+", lines))) for lines in data_of_one_scanner])


def overlaps(i: int, j: int, scanners: list[np.array], rotations: list[np.array]) -> tuple[Vector3, np.array]:
    for rotation in rotations:
        count = defaultdict(int)
        for beacon1 in scanners[i]:
            for beacon2 in scanners[j]:
                position = tuple(beacon1 - beacon2 @ rotation)
                count[position] += 1
                if count[position] == 12:
                    return position, position + scanners[j] @ rotation


def to_beacons(scanners: list[np.array]) -> set[Vector3]:
    return set(tuple(beacon) for scanner in scanners for beacon in scanner)


def calc_greatest_manhattan_distance(positions: list[Vector3]) -> int:
    return max(
        sum(abs(x1 - x2) for x1, x2 in zip(s1, s2))
        for s1, s2 in combinations(positions, 2)
    )


def main():
    scanners = parse_scanners()
    rotations = create_rotations()
    stack = [0]
    done = set()
    positions = [(0, 0, 0)]
    while stack:
        i = stack.pop()
        done.add(i)
        for j in set(range(len(scanners))) - done:
            if overlap := overlaps(i, j, scanners, rotations):
                position, translated = overlap
                positions.append(position)
                scanners[j] = translated
                stack.append(j)
    print_task1(19, len(to_beacons(scanners)))
    print_task2(19, calc_greatest_manhattan_distance(positions))


if __name__ == "__main__":
    cProfile.run('main()')
