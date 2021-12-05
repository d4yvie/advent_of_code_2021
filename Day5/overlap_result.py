class OverlapResult:

    def __init__(self, overlap_map: dict[tuple[float, float], int]):
        self._overlap_map = overlap_map
        self._overlaps = overlap_map_to_overlaps(overlap_map)

    @property
    def overlaps(self) -> int:
        return self._overlaps

    @property
    def overlap_map(self) -> dict[tuple[float, float], int]:
        return self._overlap_map


def overlap_map_to_overlaps(overlap_map: dict[tuple[float, float], int], minimal_overlap=2) -> int:
    return len(list(filter(lambda val: val >= minimal_overlap, overlap_map.values())))
