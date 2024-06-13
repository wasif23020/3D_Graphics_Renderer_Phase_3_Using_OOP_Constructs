from model import *
import glm as gl

class Scene:
    def __init__(self, application):
        self.app = application
        self.entities = []
        self.init_entities()
        self.skybox = SkyBox(application)

    def add(self, entity):
        self.entities.append(entity)

    def init_entities(self):
        app = self.app
        add = self.add

        grid_size, step = 20, 2
        for x in range(-grid_size, grid_size, step):
            for z in range(-grid_size, grid_size, step):
                add(Cube(app, pos=(x, -step, z)))

        for i in range(9):
            add(Cube(app, pos=(15, i * step, -9 + i), tex=2))
            add(Cube(app, pos=(15, i * step, 5 - i), tex=2))

        add(Cat(app, pos=(0, -1, -10)))

        self.moving = MovCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex=1)
        add(self.moving)

    def update(self):
        self.moving.update().xyz = self.app.time
