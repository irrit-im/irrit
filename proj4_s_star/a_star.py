from graphs import Vertex, Graph, VertexData, heuristic_distance
from queue import PriorityQueue


def a_star(starting_point: Vertex, goal: Vertex, graph: Graph) -> list[Vertex]:
    if not graph.is_tile_valid(starting_point) or not graph.is_tile_valid(goal):
        raise ValueError(
            "Make sure the start and end points are on the graph and not blocked."
        )

    start_vertex_data = VertexData(
        vertex=starting_point,
        previous_vertex=None,
        distance_from_start=0,
        huerostic_cost_to_goal=heuristic_distance(starting_point, goal),
    )
    open_vertices = PriorityQueue()
    open_vertices.put(start_vertex_data)
    closed_vertices: set[Vertex] = set()

    while not open_vertices.empty():
        vertex_data: VertexData = open_vertices.get()  # really needs renaming...
        vertex: Vertex = vertex_data.vertex
        closed_vertices.add(vertex)

        if vertex == goal:
            break

        adjacent_vertices = vertex.get_adjacent_vertices()
        for adjacent_vertex in adjacent_vertices:
            if (adjacent_vertex not in closed_vertices) and graph.is_tile_valid(
                adjacent_vertex
            ):
                next_path = VertexData(
                    vertex=adjacent_vertex,
                    previous_vertex=vertex_data,
                    distance_from_start=vertex_data.distance_from_start + 1,
                    huerostic_cost_to_goal=heuristic_distance(adjacent_vertex, goal),
                )
                open_vertices.put(next_path)

    # trace down the path:
    if vertex == goal:
        path = []
        while vertex_data.vertex != starting_point:
            path.append(vertex_data.vertex)
            vertex_data = vertex_data.previous_vertex
        path.reverse()
        return path
    else:
        return []
