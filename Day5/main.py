from file_util import read_lines
from overlap_result import OverlapResult


def task1(lines: list[str]) -> OverlapResult:
    return OverlapResult(create_overlap_map(lines))


def task2(lines: list[str]) -> OverlapResult:
    return OverlapResult(create_overlap_map(lines, True))


def create_overlap_map(lines: list[str], include_diagonals=False) -> dict[tuple[float, float], int]:
    overlap_map = {}
    for line in lines:
        [(x1, y1), (x2, y2)] = line_to_coordinates(line)
        overlap_map = add_vertical_entries(y1, y2, x1, overlap_map) if x1 == x2 \
            else add_horizontal_entries(x1, x2, y1, overlap_map) if y1 == y2 \
            else add_diagonal_entries(x1, x2, y1, y2, overlap_map) if include_diagonals \
            else overlap_map
    return overlap_map


def line_to_coordinates(line: str) -> list[tuple[float, float]]:
    coordinates_of_line = line.split(' -> ')
    return list(map(create_coordinate_tuple, coordinates_of_line))


def add_vertical_entries(y1: int, y2: int, x1: int, result: dict[tuple[float, float], int]) -> dict[tuple[float, float], int]:
    for y in range((min(y1, y2)), (max(y1, y2)) + 1):
        result[(x1, y)] = result.get((x1, y), 0) + 1
    return result


def add_horizontal_entries(x1: int, x2: int, y1: int, result: dict[tuple[float, float], int]) -> dict[tuple[float, float], int]:
    for x in range((min(x1, x2)), (max(x1, x2)) + 1):
        result[(x, y1)] = result.get((x, y1), 0) + 1
    return result


def add_diagonal_entries(x1: int, x2: int, y1: int, y2: int, result: dict[tuple[float, float], int]) -> dict[tuple[float, float], int]:
    distance = abs(x1 - x2)
    dx = (x2 - x1) / distance
    dy = (y2 - y1) / distance
    for n in range(distance + 1):
        x = x1 + (dx * n)
        y = y1 + (dy * n)
        result[(x, y)] = result.get((x, y), 0) + 1
    return result


def create_coordinate_tuple(coordinate: str) -> tuple[int, int]:
    x, y = coordinate.split(',')
    return int(x), int(y)


if __name__ == "__main__":
    lines_read = read_lines()
    result_1 = task1(lines_read)
    print(f"Result one is: {result_1.overlaps}")
    result_2 = task2(lines_read)
    print(f"Result two is: {result_2.overlaps}")
