import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Cam
from light import Lt
from mesh import Mesh as Msh
from scene import Scene as Scn
from scene_renderer import Renderer as ScnRndr

class RndrEng:
    def __init__(self, win_size=(1600, 900)):
        # Init Pygame
        pg.init()
        # Window config
        self.win_size = win_size
        # GL context setup
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Create GL context
        pg.display.set_mode(self.win_size, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # Create ModernGL context
        self.gl_ctx = mgl.create_context()
        self.gl_ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # Clock for time tracking
        self.clock = pg.time.Clock()
        self.curr_time = 0
        self.frame_time = 0
        # Init components
        self.lt = Lt()
        self.cam = Cam(self)
        self.mesh = Msh(self)
        self.light = self.lt  # Assign light attribute
        self.scn = Scn(self)
        self.rndr = ScnRndr(self)

    def handle_evnts(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.rndr.clean()
                pg.quit()
                sys.exit()

    def draw(self):
        # Clear screen
        self.gl_ctx.clear(color=(0.08, 0.16, 0.18))
        # Render scene
        self.rndr.render_all()
        # Update display
        pg.display.flip()

    def upd_time(self):
        self.curr_time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.upd_time()
            self.handle_evnts()
            self.cam.update()
            self.draw()
            self.frame_time = self.clock.tick(60)

if __name__ == '__main__':
    app = RndrEng()
    app.run()
