from dataclasses import dataclass
from typing import Tuple
from random import randint
from math import sqrt


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
        if isinstance(value, tuple):
            return Vertex(x=self.x + value[0], y=self.y + value[1])
        elif isinstance(value, Vertex):
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


@dataclass()
class VertexOnPath:
    vertex: Vertex
    previous_vertex: "VertexOnPath | None"
    distance_from_start: float
    huerostic_cost_to_goal: float

    def total_heuristic_cost(self) -> int:
        return self.distance_from_start + self.huerostic_cost_to_goal

    def __eq__(self, value: "VertexOnPath") -> bool:
        return self.total_heuristic_cost() == value.total_heuristic_cost()

    def __gt__(
        self, value: "VertexOnPath"
    ) -> bool:  # TODO: Fun challenge: rewrite this function to be one line
        if self.total_heuristic_cost() > value.total_heuristic_cost():
            return True
        elif self == value:
            return self.huerostic_cost_to_goal > value.huerostic_cost_to_goal
        else:
            return False

    def __ge__(self, value: "VertexOnPath") -> bool:
        return self > value or self == value

    def trace_path(self) -> list[Vertex]:
        path = []
        path.append(self.vertex)
        if self.previous_vertex:
            path.extend(self.previous_vertex.trace_path())

        return path


class Graph:
    def __init__(self, width: int, height: int, obstacles: set[Vertex]) -> None:
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def is_tile_on_board(self, tile: Vertex) -> bool:
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def is_tile_not_blocked(self, tile: Vertex) -> bool:
        return tile not in self.obstacles

    def is_tile_valid(self, tile: Vertex) -> bool:
        return self.is_tile_not_blocked(tile) and self.is_tile_on_board(tile)

    def random_vertex(self) -> Vertex:
        vertex = Vertex(randint(0, self.width - 1), randint(0, self.height - 1))
        while not self.is_tile_valid(vertex):
            vertex = Vertex(randint(0, self.width - 1), randint(0, self.height - 1))
        return vertex


def distance(vertex1: Vertex, vertex2: Vertex) -> float:
    return sqrt((vertex1.x - vertex2.x) ** 2 + (vertex1.y - vertex2.y) ** 2)


def heuristic_distance(start: Vertex, end: Vertex) -> float:
    return abs(end.x - start.x) + abs(end.y - start.y) * sqrt(2)
