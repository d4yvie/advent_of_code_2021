from print_aoc import print_task1, print_task2
from file_util import read_lines
from aoc_types import Vector2D


def dijkstra(map_dict: dict[Vector2D, int], end_coords: Vector2D) -> int:
    unvisited = set(map_dict.keys())
    node_dict = {(0, 0): 0}
    current_node = (0, 0)
    while node_dict:
        x, y = current_node
        risk = node_dict[current_node]
        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for next_to in adjacent:
            if next_to not in unvisited:
                continue
            current_risk = node_dict.get(next_to, None)
            new_risk = risk + map_dict[next_to]
            if not current_risk or new_risk < current_risk:
                node_dict[next_to] = new_risk
        unvisited.remove(current_node)
        del node_dict[current_node]
        lowest_risk = min(node_dict.values())
        for coords, risk in node_dict.items():
            if risk == lowest_risk:
                current_node = coords
                break
        if current_node == end_coords:
            return node_dict[end_coords]
    return node_dict[end_coords]


def create_map(lines: list[str]) -> tuple[dict[Vector2D, int], Vector2D]:
    map_dict = {}
    for y, row in enumerate(lines):
        for x, risk_level in enumerate(row):
            map_dict[(x, y)] = int(risk_level)
    end_coords = (len(lines) - 1, len(lines[0]) - 1)
    return map_dict, end_coords


def calc_risk(risk: int, i: int) -> int:
    new_risk = (risk + i) % 9
    return 9 if new_risk == 0 else new_risk


def extend_map(map_dict, result_map, result_coordinates, extension_func) -> tuple[dict[Vector2D, int], dict[Vector2D, int]]:
    for coordinates, risk in map_dict.items():
        x, y = coordinates
        for i in range(1, 5):
            extension_func(x, y, i, result_map, risk, result_coordinates)
    return result_map, result_map.copy()


def extend_x(x: int, y: int, i, result_map: dict[Vector2D, int], risk: int, end_coords: Vector2D):
    new_x = x + ((end_coords[0] + 1) * i)
    result_map[(new_x, y)] = calc_risk(risk, i)


def extend_y(x: int, y: int, i: int, result_map: dict[Vector2D, int], risk: int, end_coords: Vector2D):
    new_y = y + ((end_coords[1] + 1) * i)
    result_map[(x, new_y)] = calc_risk(risk, i)


def create_full_map(lines: list[str]) -> tuple[dict[Vector2D, int], Vector2D]:
    tmp_map, end_coords = create_map(lines)
    result_map, tmp_map = extend_map(tmp_map, tmp_map.copy(), end_coords, extend_x)
    result_map, tmp_map = extend_map(tmp_map, result_map, end_coords, extend_y)
    new_end_coords = ((end_coords[0] + 1) * 5 - 1, (end_coords[1] + 1) * 5 - 1)
    return result_map, new_end_coords


def task1(lines: list[str]) -> int:
    map_dict, end_coords = create_map(lines)
    return dijkstra(map_dict, end_coords)


def task2(lines: list[str]) -> int:
    map_dict, end_coords = create_full_map(lines)
    return dijkstra(map_dict, end_coords)


if __name__ == "__main__":
    lines = read_lines()
    print_task1(15, task1(lines))
    print_task2(15, task2(lines))
