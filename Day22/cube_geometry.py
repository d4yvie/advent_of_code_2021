from dataclasses import dataclass
import re


class CubeGeometry:
    pass


@dataclass(frozen=True)
class CubeGeometry:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    @staticmethod
    def from_line(line: str) -> CubeGeometry:
        return CubeGeometry(*map(int, re.findall(r"-?[0-9]+", line)))

    def intersect(self, other: CubeGeometry) -> CubeGeometry:
        c = CubeGeometry(
            max(self.x1, other.x1),
            min(self.x2, other.x2),
            max(self.y1, other.y1),
            min(self.y2, other.y2),
            max(self.z1, other.z1),
            min(self.z2, other.z2),
        )
        if c.x1 <= c.x2 and c.y1 <= c.y2 and c.z1 <= c.z2:
            return c

    def volume(self) -> int:
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)
