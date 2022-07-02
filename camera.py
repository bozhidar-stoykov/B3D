import pygame as pg
from matrix_functions import *

class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * self.render.HEIGHT / self.render.WIDTH
        self.near_plane = 0.1
        self.far_plane = 100
        self.moving_speed = 0.02
        self.rotating_speed = 0.01


    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * self.moving_speed
        if keys[pg.K_s]:
            self.position -= self.forward * self.moving_speed
        if keys[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if keys[pg.K_d]:
            self.position += self.right * self.moving_speed
        if keys[pg.K_q]:
            self.position -= self.up * self.moving_speed
        if keys[pg.K_e]:
            self.position += self.up * self.moving_speed


    def translate_matrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x,- y, -z, 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        ux, uy, uz, w = self.up
        fx, fy, fz, w = self.forward
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    
    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
