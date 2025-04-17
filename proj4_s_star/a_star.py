from graphs import Vertex, Graph, VertexData, heuristic_distance
from typing import Dict
import heapq


def a_star(starting_point: Vertex, goal: Vertex, graph: Graph) -> list[Vertex]:
    if not graph.is_tile_valid(starting_point) or not graph.is_tile_valid(goal):
        raise ValueError(
            "make sure the start and end points are on the graph and not blocked"
        )

    queue: heapq = [
        VertexData(
            vertex=starting_point,
            shortest_path_origin=None,
            path_length_from_start=float("inf"),
            huerostic_cost_to_goal=heuristic_distance(starting_point, goal),
        )
    ]
    heapq.heapify(queue)
    visited: Dict[Vertex, VertexData] = dict()

    while True:
        try:
            check_vertex: VertexData = heapq.heappop(queue)
        except AttributeError:
            return False

        if check_vertex.vertex == goal:
            path = []
            while check_vertex.vertex != starting_point:
                path.append(check_vertex.vertex)
                check_vertex = check_vertex.shortest_path_origin
            return path

        if (
            not (check_vertex.vertex in visited)
            or visited[check_vertex.vertex].path_length_from_start
            > check_vertex.path_length_from_start
        ):
            visited[check_vertex.vertex] = check_vertex

        adjacent_vertices = check_vertex.vertex.get_adjacent_vertices()
        for adjacent_vertex in adjacent_vertices:
            if adjacent_vertex not in visited and graph.is_tile_valid(adjacent_vertex):
                heapq.heappush(
                    queue,
                    VertexData(
                        vertex=adjacent_vertex,
                        shortest_path_origin=check_vertex,
                        path_length_from_start=check_vertex.path_length_from_start + 1,
                        huerostic_cost_to_goal=heuristic_distance(
                            adjacent_vertex, goal
                        ),
                    ),
                )

    # check_vertex =   # TODO: pleeeeeese rename this
    # tiles = {
    #     starting_point: VertexData(
    #         path_length_from_start=0,
    #         shortest_path_origin=starting_point,
    #         huerostic_cost_to_goal=heuristic_distance(starting_point, goal),
    #     )
    # }
    # check_vertex.put(starting_point)

    # while not check_vertex.empty():
    #     test_tile: Vertex = check_vertex.get()
    #     if test_tile == goal:
    #         return test_tile.trace_path()
