from graphs import Vertex, Graph
from display import GraphSprite
from a_star import a_star
from random import randint
import pygame


BOARD_WIDTH_TILES = 25
BOARD_HIGHT_TILES = 25
MAX_SCREEN_SIZE = 800
TILE_SIZE_PIXELS = MAX_SCREEN_SIZE // max(BOARD_WIDTH_TILES, BOARD_HIGHT_TILES)
MAX_OBSTACLE_DENSITY = 0.9

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(
        (TILE_SIZE_PIXELS * BOARD_WIDTH_TILES, TILE_SIZE_PIXELS * BOARD_HIGHT_TILES)
    )
    clock = pygame.time.Clock()
    running = True
    my_graph = Graph(width=BOARD_WIDTH_TILES, height=BOARD_HIGHT_TILES, obstacles=set())
    graph_image = GraphSprite(graph=my_graph, total_size_pixels=MAX_SCREEN_SIZE)
    start = my_graph.random_vertex()
    end = my_graph.random_vertex()
    obstacles: set[Vertex] = set()
    for _ in range(
        randint(0, int(BOARD_HIGHT_TILES * BOARD_WIDTH_TILES * MAX_OBSTACLE_DENSITY))
    ):
        tile = my_graph.random_vertex()
        if tile != start and tile != end:
            obstacles.add(tile)
    my_graph.obstacles = obstacles

    path = a_star(starting_point=start, goal=end, graph=my_graph)

    graph_image.draw_grid()
    graph_image.draw_path(path=path)
    graph_image.draw_obstacles()
    group = pygame.sprite.Group(graph_image)
    group.draw(surface=screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
