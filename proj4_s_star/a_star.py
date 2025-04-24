from graphs import Vertex, Graph, VertexOnPath, distance, heuristic_distance
from queue import PriorityQueue


def a_star(starting_point: Vertex, goal: Vertex, graph: Graph) -> list[Vertex]:
    if not graph.is_tile_valid(starting_point) or not graph.is_tile_valid(goal):
        raise ValueError(
            "Make sure the start and end points are on the graph and not blocked."
        )

    start_vertex_data = VertexOnPath(
        vertex=starting_point,
        previous_vertex=None,
        distance_from_start=0,
        huerostic_cost_to_goal=heuristic_distance(starting_point, goal),
    )
    open_vertices = PriorityQueue()
    open_vertices.put(start_vertex_data)
    closed_vertices: set[Vertex] = set()

    while not open_vertices.empty():
        vertex_data: VertexOnPath = open_vertices.get()
        vertex: Vertex = vertex_data.vertex
        closed_vertices.add(vertex)

        if vertex == goal:
            break

        adjacent_vertices = vertex.get_adjacent_vertices()
        for adjacent_vertex in adjacent_vertices:
            if (adjacent_vertex not in closed_vertices) and graph.is_tile_valid(
                adjacent_vertex
            ):
                additional_distance = distance(vertex1=vertex, vertex2=adjacent_vertex)
                next_path = VertexOnPath(
                    vertex=adjacent_vertex,
                    previous_vertex=vertex_data,
                    distance_from_start=vertex_data.distance_from_start
                    + additional_distance,
                    huerostic_cost_to_goal=heuristic_distance(adjacent_vertex, goal),
                )
                open_vertices.put(next_path)

    if vertex == goal:
        return vertex_data.trace_path()
    else:
        return []
