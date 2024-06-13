import glm
import pygame as pg

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPD = 0.005
SENS = 0.04


class Cam:
    def __init__(self, app, pos=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.asp = app.win_dims[0] / app.win_dims[1]
        self.pos = glm.vec3(pos)
        self.up = glm.vec3(0, 1, 0)
        self.rt = glm.vec3(1, 0, 0)
        self.fwd = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        self.view = self.get_view()
        self.proj = self.get_proj()

    def get_view(self):
        return glm.lookAt(self.pos, self.pos + self.fwd, self.up)

    def get_proj(self):
        return glm.perspective(glm.radians(FOV), self.asp, NEAR, FAR)

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENS
        self.pitch -= rel_y * SENS
        self.pitch = max(-89, min(89, self.pitch))

    def update_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        self.fwd.x = glm.cos(yaw) * glm.cos(pitch)
        self.fwd.y = glm.sin(pitch)
        self.fwd.z = glm.sin(yaw) * glm.cos(pitch)
        self.fwd = glm.normalize(self.fwd)
        self.rt = glm.normalize(glm.cross(self.fwd, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.rt, self.fwd))

    def move(self):
        vel = SPD * self.app.frame_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: self.pos += self.fwd * vel
        if keys[pg.K_s]: self.pos -= self.fwd * vel
        if keys[pg.K_a]: self.pos -= self.rt * vel
        if keys[pg.K_d]: self.pos += self.rt * vel
        if keys[pg.K_q]: self.pos += self.up * vel
        if keys[pg.K_e]: self.pos -= self.up * vel

    def update(self):
        self.move()
        self.rotate()
        self.update_vectors()
        self.view = self.get_view()
