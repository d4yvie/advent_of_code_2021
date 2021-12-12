from datetime import datetime
from file_util import read_lines
from cave import Cave, CaveMarker
from copy import deepcopy
from print_aoc import print_task1, print_task2
from functools import reduce


def create_caves_with_connections(lines: list[str]) -> dict[str, Cave]:
    return add_connections(lines, create_caves(lines))


def create_caves(lines: list[str]) -> dict[str, Cave]:
    return reduce(create_cave, lines, {})


def create_cave(name_to_caves: dict[str, Cave], line) -> dict[str, Cave]:
    cave_a, cave_b = line_to_cave_markers(line)
    name_to_caves[cave_a] = Cave(cave_a, cave_a.isupper())
    name_to_caves[cave_b] = Cave(cave_b, cave_b.isupper())
    return name_to_caves


def line_to_cave_markers(line: str) -> list[str]:
    return line.strip().split("-")


def add_connections(lines: list[str], name_to_caves: dict[str, Cave]) -> dict[str, Cave]:
    return reduce(connect_caves, lines, name_to_caves)


def connect_caves(name_to_caves: dict[str, Cave], line) -> dict[str, Cave]:
    cave_a, cave_b = line_to_cave_markers(line)
    name_to_caves[cave_a].append_connected_caves([cave_b])
    name_to_caves[cave_b].append_connected_caves([cave_a])
    return name_to_caves


def get_all_possible_paths_to_end(recursion_params: tuple[str, dict[str, Cave], dict[str, int], list[str]]) -> set[tuple[str, ...]]:
    start_cave_marker, caves, already_traversed_nodes, current_path = recursion_params
    start_cave = caves[start_cave_marker]
    if not start_cave.is_large() and (already_traversed_nodes.get(start_cave_marker, 0) > 0):
        return set()
    already_traversed_nodes[start_cave_marker] = already_traversed_nodes.get(start_cave_marker, 0) + 1
    current_path.append(start_cave_marker)
    if start_cave.is_end_cave():
        return {tuple(current_path)}
    params = map(lambda connected_cave: to_recursion_params(connected_cave, caves, already_traversed_nodes.copy(), current_path.copy()), caves[start_cave_marker].connected_caves)
    paths = map(get_all_possible_paths_to_end, params)
    return set().union(*paths)


def to_recursion_params(connected_cave, caves, already_traversed_nodes: dict[str, int], current_path: list[str]) -> tuple[str, dict[str, Cave], dict[str, int], list[str]]:
    return connected_cave, caves, already_traversed_nodes, current_path


def task1(caves: dict[str, Cave]) -> int:
    return len(get_all_possible_paths_to_end(to_recursion_params(CaveMarker.START.value, caves, {}, [])))


def task2(caves: dict[str, Cave]) -> int:
    routes = set()
    for cave_to_dupe in caves:
        duped_cave_marker = to_dupe_cave(cave_to_dupe)
        if cave_to_dupe.islower() and is_not_start_or_end(cave_to_dupe):
            caves_replica = deepcopy(caves)
            caves_replica[duped_cave_marker] = Cave(duped_cave_marker, False)
            caves_replica[duped_cave_marker].connected_caves = caves_replica[cave_to_dupe].connected_caves
            for c in caves:
                if cave_to_dupe in caves[c].connected_caves:
                    caves_replica[c].append_connected_caves([duped_cave_marker])
            routes = routes.union(get_all_possible_paths_to_end(to_recursion_params(CaveMarker.START.value, caves_replica, {}, [])))
    new_routes = set(map(lambda route: tuple([x if x[-1] != "2" else x[:-1] for x in route]), routes))
    return len(new_routes)


def is_not_start_or_end(cave_marker: str) -> bool:
    return not (cave_marker == CaveMarker.START.value or cave_marker == CaveMarker.END.value)


def to_dupe_cave(cave_marker: str) -> str:
    return f"{cave_marker}2"


if __name__ == "__main__":
    lines = read_lines()
    caves = create_caves_with_connections(lines)
    print_task1(12, task1(caves))
    print_task2(12, task2(caves))
