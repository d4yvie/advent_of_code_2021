from builtins import int
from file_util import read_line_seperated_data_sets
from print_aoc import print_task1, print_task2
import itertools
import re
import cProfile


Vector5 = tuple[int, int, int, int, int]
Vector3 = tuple[int, int, int]
Scanner = set[Vector3]


def convert(x: int, y: int, z: int, ori: Vector5) -> Vector3:
    xneg, xaxis, yneg, yaxis, zneg = ori
    out = [0] * 3
    axis = [0, 1, 2]
    out[axis.pop(xaxis)] = x * xneg
    out[axis.pop(yaxis)] = y * yneg
    out[axis.pop()] = z * zneg
    return tuple(out)


def convert_reverse(x: int, y: int, z: int, ori: Vector5) -> Vector3:
    xneg, xaxis, yneg, yaxis, zneg = ori
    ins = [x, y, z]
    axis = [0, 1, 2]
    x = ins[axis.pop(xaxis)] * xneg
    y = ins[axis.pop(yaxis)] * yneg
    z = ins[axis.pop()] * zneg
    return x, y, z


def match(scanner_one: Scanner, scanner_two: Scanner) -> tuple[set[tuple[int | int, int | int, int | int]], tuple[int | int, int | int, int | int]]:
    for ori in itertools.product((-1, 1), (0, 1, 2), (-1, 1), (0, 1), (-1, 1)):
        for x, y, z in scanner_one:
            for xx, yy, zz in scanner_two:
                match_count = 0
                for xxx, yyy, zzz in scanner_one:
                    if (x, y, z) == (xxx, yyy, zzz):
                        continue
                    dx = xxx - x
                    dy = yyy - y
                    dz = zzz - z
                    dxx, dyy, dzz = convert(dx, dy, dz, ori)
                    if (xx + dxx, yy + dyy, zz + dzz) in scanner_two:
                        match_count += 1
                if match_count >= 11:
                    x, y, z = convert(x, y, z, ori)
                    dx, dy, dz = x - xx, y - yy, z - zz
                    return (
                        set(
                            convert_reverse(x + dx, y + dy, z + dz, ori) for x, y, z in scanner_two
                        ),
                        convert_reverse(dx, dy, dz, ori),
                    )


def greatest_manhatten_distance(scanners_pos: Scanner) -> int:
    return max(manhattan_distance(x1, x2, y1, y2, z1, z2) for (x1, y1, z1), (x2, y2, z2) in itertools.combinations(scanners_pos, 2))


def manhattan_distance(x1: int, x2: int, y1: int, y2: int, z1: int, z2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def parse_scanners() -> list[Scanner]:
    scanner_data_sets = read_line_seperated_data_sets()
    return list(map(create_scanner, scanner_data_sets))


def create_scanner(scanner_data_set: str) -> Scanner:
    return set(map(parse_tuple, scanner_data_set.splitlines()[1:]))


# noinspection PyTypeChecker
def parse_tuple(line: str) -> Vector3:
    return tuple(map(int, re.findall(r"-?[0-9]+", line)))


def main():
    scanners = parse_scanners()
    todo = [0]
    matched = {0}
    beacons = set(scanners[0])
    scanners_pos = {(0, 0, 0)}
    while todo:
        new = []
        for scanner_one in todo:
            for i, scanner_two in enumerate(scanners):
                if i in matched:
                    continue
                res = match(scanners[scanner_one], scanner_two)
                if res is not None:
                    m, s = res
                    new.append(i)
                    matched.add(i)
                    scanners[i] = m
                    scanners_pos.add(s)
                    beacons |= m
        todo = new
    print_task1(19, len(beacons))
    print_task2(19, greatest_manhatten_distance(scanners_pos))


if __name__ == "__main__":
    cProfile.run('main()')
