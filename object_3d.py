import pygame as pg
from matrix_functions import *

class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertices = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])

        self.faces = np.array([(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 6, 7, 3), (1, 5, 6, 2), (4, 0, 3, 7)])


    def draw(self):
        self.screen_projection()
        

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, pg.Color('greenyellow'), polygon, 3)

        for vertex in vertices:
            if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex.astype(int), 6)


    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)


    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)


    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)


    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)


    def scale(self, ns):
        self.vertices = self.vertices @ scale(ns)