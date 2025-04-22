from graphs import Vertex, Graph, Obstacle
from display import GraphSprite
from a_star import a_star
from random import randint
import pygame


BOARD_WIDTH_TILES = 25
BOARD_HIGHT_TILES = 25
MAX_SCREEN_SIZE = 800
TILE_SIZE_PIXELS = MAX_SCREEN_SIZE // max(BOARD_WIDTH_TILES, BOARD_HIGHT_TILES)


start = Vertex.random_vertex(BOARD_WIDTH_TILES, BOARD_HIGHT_TILES)
end = Vertex.random_vertex(BOARD_WIDTH_TILES, BOARD_HIGHT_TILES)

obstacles: set[Obstacle] = set()
for _ in range(randint(0, int(BOARD_HIGHT_TILES * BOARD_WIDTH_TILES * 0.8))):
    tile = Vertex.random_vertex(BOARD_WIDTH_TILES, BOARD_HIGHT_TILES)
    if tile != start and tile != end:
        obstacles.add(tile)

my_graph = Graph(width=BOARD_WIDTH_TILES, height=BOARD_HIGHT_TILES, obstacles=obstacles)
my_graph_image = GraphSprite(graph=my_graph, total_size_pixels=MAX_SCREEN_SIZE)
path = a_star(starting_point=start, goal=end, graph=my_graph)

pygame.init()
screen = pygame.display.set_mode(
    (TILE_SIZE_PIXELS * BOARD_WIDTH_TILES, TILE_SIZE_PIXELS * BOARD_HIGHT_TILES)
)

clock = pygame.time.Clock()
running = True
my_graph_image.draw_grid()
my_graph_image.draw_path(path=path)
my_graph_image.draw_obstacles()
group = pygame.sprite.Group(my_graph_image)
group.draw(surface=screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(10)


pygame.quit()
