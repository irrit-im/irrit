from a_star import a_star
from graphs import Vertex, Graph, VertexData, Obstacle, heuristic_distance

v1 = Vertex(x=0, y=0)
v2 = Vertex(50, 50)
vd1 = VertexData(v1, v2, 1, 1)
my_graph = Graph(5, 5, [])
path = a_star(Vertex(2, 2), Vertex(0, 0), my_graph)
print(path)
