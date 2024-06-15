import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Cam
from light import Lt
from mesh import Mesh as Msh
from scene import Scene as Scn
from scene_renderer import Renderer as ScnRndr

import numpy as np

class RenderEngine:
    def __init__(self):
        self.scene = Scene()
        self.models = Model()

    def add_model(self, vertex_data, position=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
        self.models.add_model(vertex_data, position, rotation, scale)

    def create_scene_object(self, model_index, position=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0)):
        vertex_data = self.models.get_model_data(model_index)['vertex_data']
        scene_obj = SceneObject(vertex_data, position, rotation)
        self.scene.add_object(scene_obj)

    def render_scene(self):
        self.scene.render()

if __name__ == '__main__':
    app = RenderEngine()
    app.run()
