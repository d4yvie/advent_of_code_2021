from print_aoc import print_task1, print_task2
from file_util import read_all
from organization_state import OrganizationState, Rooms
import heapq


def insert(tpl, i: int, new: tuple[int, ...] | int | None) -> tuple:
    return tpl[:i] + (new,) + tpl[i + 1:]


def solve(rooms: Rooms, EXIT=(2, 4, 6, 8)) -> int:
    ROOM_SIZE = len(rooms[0])
    states_to_check = [OrganizationState(0, rooms)]
    visited_states = set()
    while states_to_check:
        state = heapq.heappop(states_to_check)
        if state.are_amphipods_organized:
            return state.energy
        if state.id in visited_states:
            continue
        visited_states.add(state.id)
        visit_rooms(state, visited_states, states_to_check, ROOM_SIZE, EXIT)
        visit_hallways(state, visited_states, states_to_check, ROOM_SIZE, EXIT)


def visit_rooms(state: OrganizationState, visited_states: set[tuple[tuple, tuple]], states_to_check: list[OrganizationState], ROOM_SIZE: int, EXIT: tuple):
    for room_index, room in enumerate(state.rooms):
        if room and not all(a == room_index for a in room):
            a = room[-1]
            for to, d in ((-1, -1), (11, 1)):
                for hi in range(EXIT[room_index] + d, to, d):
                    if hi in EXIT:
                        continue
                    if state.hallway[hi] is not None:
                        break
                    possible_state = OrganizationState(
                        state.energy
                        + (ROOM_SIZE - len(room) + 1 + abs(EXIT[room_index] - hi))
                        * (10 ** a),
                        insert(state.rooms, room_index, room[:-1]),
                        insert(state.hallway, hi, a),
                    )
                    add_possible_state(visited_states, states_to_check, possible_state)


def visit_hallways(state: OrganizationState, visited_states: set[tuple[tuple, tuple]], states_to_check: list[OrganizationState], ROOM_SIZE: int, EXIT: tuple):
    for i, a in enumerate(state.hallway):
        if a is None \
                or (i < EXIT[a] and any(u is not None for u in state.hallway[i + 1: EXIT[a]])) \
                or (i > EXIT[a] and any(u is not None for u in state.hallway[EXIT[a] + 1: i])) \
                or (any(u != a for u in state.rooms[a])):
            continue
        possible_state = OrganizationState(
            state.energy
            + (ROOM_SIZE - len(state.rooms[a]) + abs(EXIT[a] - i)) * (10 ** a),
            insert(state.rooms, a, (state.rooms[a] + (a,))),
            insert(state.hallway, i, None),
        )
        add_possible_state(visited_states, states_to_check, possible_state)


def add_possible_state(visited_states: set[tuple[tuple, tuple]], states_to_check: list[OrganizationState], possible_state: OrganizationState):
    if possible_state.id not in visited_states:
        heapq.heappush(states_to_check, possible_state)


def parse_task1_rooms() -> Rooms:
    lines = read_all().splitlines()
    return tuple(
        (ord(lines[3][2 * i + 3]) - ord("A"), ord(lines[2][2 * i + 3]) - ord("A"),)
        for i in range(4)
    )


def create_task2_rooms(rooms: Rooms) -> Rooms:
    AMBER, BRONZE, COPPER, DESERT = range(4)
    return (
        (rooms[0][0], DESERT, DESERT, rooms[0][1]),
        (rooms[1][0], BRONZE, COPPER, rooms[1][1]),
        (rooms[2][0], AMBER, BRONZE, rooms[2][1]),
        (rooms[3][0], COPPER, AMBER, rooms[3][1]),
    )


if __name__ == '__main__':
    rooms = parse_task1_rooms()
    result = solve(rooms)
    assert result == 13066
    print_task1(23, result)
    rooms = create_task2_rooms(rooms)
    result = solve(rooms)
    assert result == 47328
    print_task2(23, solve(rooms))
