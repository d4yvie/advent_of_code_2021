from file_util import read_first_line_as_integers
from functools import reduce
import statistics


def task1(crab_positions: list[int]) -> int:
    median = statistics.median(crab_positions)
    return int(sum(map(lambda x: abs(x - median), crab_positions)))


def task2(crab_positions: list[int]) -> int:
    crab_positions_count = count_crab_positions(crab_positions)
    lowest_position = min(crab_positions_count.keys())
    highest_position = max(crab_positions_count.keys())
    costs_list = create_costs_list(lowest_position, highest_position)
    total_fuel = init_fuel(lowest_position, highest_position)
    for crab_position in range(lowest_position, highest_position + 1):
        for k in crab_positions_count.keys():
            crabs_in_position = crab_positions_count[k]
            total_fuel[crab_position] += costs_list[abs(crab_position - k)] * crabs_in_position
    return int(min(total_fuel.values()))


def create_costs_list(lowest_position: int, highest_position: int) -> list[int]:
    costs_for_distances = [0, 1]
    while len(costs_for_distances) <= (highest_position - lowest_position):
        costs_for_distances.append(costs_for_distances[-1] + len(costs_for_distances))
    return costs_for_distances


def count_crab_positions(crab_positions: list[int]) -> dict[int, int]:
    crab_positions_count = {}
    for position in crab_positions:
        if position in crab_positions_count:
            crab_positions_count[position] += 1
        else:
            crab_positions_count[position] = 1
    return crab_positions_count


def init_fuel(lowest_position: int, highest_position: int) -> dict[int, int]:
    return reduce(init_position, range(lowest_position, highest_position + 1), {})


def init_position(total_fuel, position: int) -> dict[int, int]:
    total_fuel[position] = 0
    return total_fuel


if __name__ == "__main__":
    crab_positions = read_first_line_as_integers()
    print(f"Fuel amount task1: {task1(crab_positions)}")
    print(f"Fuel amount task2: {task2(crab_positions)}")
