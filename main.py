import pygame as pg
from camera import *
from object_3d import *
from projection import *

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.HEIGHT, self.WIDTH = (1600, 900)
        self.H_WIDTH = self.WIDTH // 2
        self.H_HEIGHT = self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()


    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.obj = Object3D(self)
        self.obj.translate([0.8, 1.7, 0.1])
        self.obj.rotate_y(math.radians(30))


    def draw(self):
        self.screen.fill(pg.Color('gray27'))
        self.obj.draw()


    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            pg.display.set_caption('FPS: ' + format(float(self.clock.get_fps()),".2f"))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()