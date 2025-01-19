import pygame
from constants import *
from vertex import *

# create mst
# display mst
# place root at time_pos = (0,0)
# place other vertexes at positions:
#   time_distance from root
#       a straight line should be the fastest way from root->vertex
#       if you have to go root->a->b to go root->b then a should be on the line root->b
#   in a way which doesn't majorly rearrange the cartesian representation of the map

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()

    Vertex.containers = (drawable)

    vertex_factory = Vertex_Factory()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()