from graphs import Vertex, Graph, Vertex
from typing import Tuple, List
import pygame


class GraphSprite(pygame.sprite.Sprite):
    def __init__(self, graph: Graph, total_size_pixels: int = 500):
        super().__init__()
        self.graph = graph
        self.tile_size = total_size_pixels // max(self.graph.width, self.graph.height)
        self.width_pixels = self.tile_size * self.graph.width
        self.height_pixels = self.tile_size * self.graph.height
        self.image = pygame.Surface([self.width_pixels, self.height_pixels])
        self.rect = self.image.get_rect()

    def draw_grid(
        self, bg_color="lightcyan", grid_color="darkslategray4", line_width=3
    ) -> None:
        self.image.fill(bg_color)
        for x in range(self.graph.width):
            x_pos = self.tile_size * x
            pygame.draw.line(
                surface=self.image,
                color=grid_color,
                start_pos=(x_pos, 0),
                end_pos=(x_pos, self.height_pixels),
                width=line_width,
            )
        for y in range(self.graph.height):
            y_pos = self.tile_size * y
            pygame.draw.line(
                surface=self.image,
                color=grid_color,
                start_pos=(0, y_pos),
                end_pos=(self.width_pixels, y_pos),
                width=line_width,
            )

    def get_tile_center(self, tile: Vertex) -> Tuple[int, int]:
        half_tile = self.tile_size // 2
        x = tile.x * self.tile_size + half_tile
        y = tile.y * self.tile_size + half_tile
        return (x, y)

    def draw_obstacles(self, color="darkslategrey") -> None:
        for obstacle in self.graph.obstacles:
            center = self.get_tile_center(obstacle)
            radius = 0.45 * self.tile_size
            pygame.draw.circle(
                surface=self.image, color=color, center=center, radius=radius
            )

    def draw_path(
        self, path: List[Vertex], line_color="mediumorchid4", line_width=5
    ) -> None:
        for i in range(len(path) - 1):
            start = self.get_tile_center(path[i])
            end = self.get_tile_center(path[i + 1])

            pygame.draw.line(
                surface=self.image,
                color=line_color,
                start_pos=start,
                end_pos=end,
                width=line_width,
            )
