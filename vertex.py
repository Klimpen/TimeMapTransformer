import pygame
import random
from constants import*

class Vertex(pygame.sprite.Sprite):
    def __init__(self, x, y):

        if hasattr(self, "containers"):
            super().__init__(self.containers)

        self.position = pygame.Vector2(x, y)
        self.edges = [] # list of (vertex, distance_in_time)
        self.distance = None
        self.parent = None
        self.children = []
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2, width=2)
        for edge in self.edges:
            pygame.draw.line(screen,"green", self.position, edge[0].position, width=1)


class Vertex_Factory():

    def __init__(self):
        vertex_list = self.create_vertexes()

    def create_vertexes(self):
        vertex_list = []

        for i in range(VERTEX_NUM):
            x = random.random() * SCREEN_WIDTH
            y = random.random() * SCREEN_HEIGHT
            vertex_list.append(Vertex(x, y))
        
        for i in range(len(vertex_list)):
            edge_num = random.randint(1, VERTEX_MAX_EDGES)
            edges_to_make = edge_num - len(vertex_list[i].edges)

            for j in range(i+1, len(vertex_list)):

                ij_distance = vertex_list[i].position.distance_to(vertex_list[j].position)

                if  ij_distance < VERTEX_MAX_LINK_DISTANCE:
                    distance_factor = random.random()
                    vertex_list[i].edges.append((vertex_list[j], ij_distance * distance_factor))
                    vertex_list[j].edges.append((vertex_list[i], ij_distance * distance_factor))
                    edges_to_make -= 1

                if edges_to_make <= 0:
                    break
            
        return vertex_list