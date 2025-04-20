from dataclasses import dataclass
from typing import Tuple

EXPAND_DIRECTIONS = (
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
)


@dataclass(frozen=True, order=True)
class Vertex:
    x: int
    y: int

    def __add__(self, value: Tuple[int, int] | "Vertex") -> "Vertex":
        if type(value) == tuple:
            return Vertex(x=self.x + value[0], y=self.y + value[1])
        elif type(value) == Vertex:
            return Vertex(self.x + value.x, self.y + value.y)

    def __eq__(self, value: "Vertex") -> bool:
        return self.x == value.x and self.y == value.y

    def __str__(self) -> str:
        return f"v({self.x}, {self.y})"

    def get_adjacent_vertices(self) -> list["Vertex"]:
        adjacent_vertices = []
        for direction in EXPAND_DIRECTIONS:
            adjacent_vertices.append(self + direction)
        return adjacent_vertices


class Obstacle(Vertex): ...


@dataclass()
class VertexData:  # TODO: rename
    vertex: Vertex
    previous_vertex: "VertexData"
    distance_from_start: int
    huerostic_cost_to_goal: int

    def total_heuristic_cost(self) -> int:
        return self.distance_from_start + self.huerostic_cost_to_goal

    def __eq__(self, value: "VertexData") -> bool:
        return self.total_heuristic_cost() == value.total_heuristic_cost()

    def __gt__(self, value: "VertexData") -> bool:
        if self.total_heuristic_cost() > value.total_heuristic_cost():
            return True
        elif self == value:
            return self.huerostic_cost_to_goal > value.huerostic_cost_to_goal
        else:
            return False


class Graph:
    def __init__(self, width, height, obstacles: set[Obstacle]) -> None:
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def is_tile_on_board(self, tile: Vertex) -> bool:
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def is_tile_not_blocked(self, tile: Vertex) -> bool:
        return tile not in self.obstacles

    def is_tile_valid(self, tile: Vertex) -> bool:
        return self.is_tile_not_blocked(tile) and self.is_tile_on_board(tile)


def heuristic_distance(start: Vertex, end: Vertex) -> int:
    return abs(end.x - start.x) + abs(end.y - start.y)
