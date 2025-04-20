from a_star import a_star
from graphs import Vertex, Graph, VertexData, Obstacle, heuristic_distance

start = Vertex(4, 2)
end = Vertex(0, 0)
O = Obstacle
obstacles = [
    O(1, 0),
    O(1, 1),
    O(1, 2),
    O(1, 3),
]
my_graph = Graph(width=5, height=5, blocks=obstacles)

if __name__ == "main":
    path = a_star(starting_point=start, goal=end, graph=my_graph)
    if path:
        for v in path:
            print(v)
    else:
        print("No path found")
