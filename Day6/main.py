from collections import defaultdict
from file_util import read_first_line_as_integers
from functools import reduce


def spend_days(lantern_fishes: dict[int, int], days: int) -> dict[int, int]:
    return reduce(spend_day, range(days), lantern_fishes)


def spend_day(lantern_fishes: dict[int, int], day: int) -> dict[int, int]:
    lantern_fishes_after_day = create_empty_lantern_fish_sea()
    for days_until_reproduction, lantern_fishes_in_day_cycle in lantern_fishes.items():
        days_until_reproduction -= 1
        lantern_fishes_after_day = reproduce(lantern_fishes_after_day, lantern_fishes_in_day_cycle) \
            if days_until_reproduction < 0 \
            else move_lantern_fishes_to_next_day(lantern_fishes_after_day, days_until_reproduction, lantern_fishes_in_day_cycle)
    return lantern_fishes_after_day


def reproduce(lantern_fishes_after_day: dict[int, int], lantern_fishes_which_reproduce: int, days_until_following_reproduction=6, days_until_first_reproduction=8) -> dict[int, int]:
    lantern_fishes_after_day[days_until_following_reproduction] += lantern_fishes_which_reproduce
    lantern_fishes_after_day[days_until_first_reproduction] += lantern_fishes_which_reproduce
    return lantern_fishes_after_day


def move_lantern_fishes_to_next_day(lantern_fishes_after_day: dict[int, int], days_until_reproduction: int, lantern_fishes_in_day_cycle: int) -> dict[int, int]:
    lantern_fishes_after_day[days_until_reproduction] += lantern_fishes_in_day_cycle
    return lantern_fishes_after_day


def add_fish_in_day_cycle(lantern_fishes: dict[int, int], days_until_reproduction: int) -> dict[int, int]:
    lantern_fishes[days_until_reproduction] += 1
    return lantern_fishes


def create_empty_lantern_fish_sea() -> dict[int, int]:
    return defaultdict(lambda: 0)


def initialize_lantern_fish_sea(file_entries: list[int]) -> dict[int, int]:
    return reduce(add_fish_in_day_cycle, file_entries, create_empty_lantern_fish_sea())


def simulate(file_entries: list[int], days_to_spend=80) -> dict[int, int]:
    lantern_fishes = initialize_lantern_fish_sea(file_entries)
    print(f"After {days_to_spend} days: {sum(spend_days(lantern_fishes, days_to_spend).values())}")
    return lantern_fishes


if __name__ == "__main__":
    file_entries = read_first_line_as_integers()
    simulate(file_entries)
    simulate(file_entries, 256)
