from print_aoc import print_task1, print_task2
from file_util import read_lines
from cube_geometry import CubeGeometry
from collections import Counter

# Is on and geometrical Data for calculations
Cube = tuple[bool, CubeGeometry]


def parse_reboot_steps() -> list[Cube]:
    return [
        (line.split()[0] == "on", CubeGeometry.from_line(line))
        for line in read_lines()
    ]


def determine_cubes_on_after_reboot(reboot_steps: list[Cube], procedure_region=None) -> int:
    cubes_counter = Counter()
    for cube_is_on, cube_geometry in reboot_steps:
        if procedure_region and (cube_geometry := cube_geometry.intersect(procedure_region)) is None:
            continue
        new_counter = Counter()
        for cube_geometry_counter, count in cubes_counter.items():
            if intersection_cube := cube_geometry.intersect(cube_geometry_counter):
                new_counter[intersection_cube] -= count
        cubes_counter.update(new_counter)
        if cube_is_on:
            cubes_counter[cube_geometry] += 1
    return sum(cube_geometry.volume() * count for cube_geometry, count in cubes_counter.items())


if __name__ == '__main__':
    reboot_steps_parsed = parse_reboot_steps()
    print_task1(22, determine_cubes_on_after_reboot(reboot_steps_parsed, CubeGeometry(-50, 50, -50, 50, -50, 50)))
    print_task2(22, determine_cubes_on_after_reboot(reboot_steps_parsed))
