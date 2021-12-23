from dataclasses import dataclass
from aoc_types import VectorX

Rooms = tuple[VectorX, ...]


@dataclass(frozen=True)
class OrganizationState:
    energy: int
    rooms: tuple
    hallway: tuple = (None,) * 11

    def __lt__(self, other):
        return self.energy < other.energy

    @property
    def id(self) -> tuple[tuple, tuple]:
        return self.hallway, self.rooms

    @property
    def are_amphipods_organized(self):
        return all(hallway is None for hallway in self.hallway) and all(
            all(ambhipod == i for ambhipod in room) for i, room in enumerate(self.rooms)
        )
