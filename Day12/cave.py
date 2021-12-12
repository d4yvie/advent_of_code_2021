from enum import Enum


class Cave:
    def __init__(self, name: str, large: bool):
        self.name = name
        self.connected_caves = []
        self.large = large

    def is_large(self) -> bool:
        return self.large

    def append_connected_caves(self, connected_caves: list[str]) -> None:
        self.connected_caves.extend(connected_caves)

    def is_start_cave(self) -> bool:
        return self.name == CaveMarker.START.value

    def is_end_cave(self) -> bool:
        return self.name == CaveMarker.END.value

    def __repr__(self):
        return f"{self.name} is connected to {','.join(self.connected_caves)}"


class CaveMarker(Enum):
    START = "start"
    END = "end"

