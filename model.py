import moderngl as mg
import numpy as npy
import glm as gl

class Model:
    def __init__(self, app, vao_name, tex, pos=(0, 0, 0), rot=(0, 0, 0), scl=(1, 1, 1)):
        self.app = app
        self.vao = app.mesh.vao.vaos[vao_name]
        self.tex = tex
        self.pos = pos
        self.rot = gl.vec3([gl.radians(a) for a in rot])
        self.scl = scl
        self.mdl_mtx = self.get_mdl_mtx()
        self.cam = app.cam
        self.prg = self.vao.program

    def get_mdl_mtx(self):
        m = gl.mat4()
        m = gl.translate(m, self.pos)
        m = gl.rotate(m, self.rot.z, gl.vec3(0, 0, 1))
        m = gl.rotate(m, self.rot.y, gl.vec3(0, 1, 0))
        m = gl.rotate(m, self.rot.x, gl.vec3(1, 0, 0))
        m = gl.scale(m, self.scl)
        return m

    def upd(self):
        pass

    def draw(self):
        self.upd()
        self.vao.render()

class ExtModel(Model):
    def __init__(self, app, vao_name, tex, pos, rot, scl):
        super().__init__(app, vao_name, tex, pos, rot, scl)
        self.init()

    def upd(self):
        self.tex.use(location=0)
        self.prg['camPos'].write(self.cam.pos)
        self.prg['m_view'].write(self.cam.m_view)
        self.prg['m_mdl'].write(self.mdl_mtx)

    def upd_shadow(self):
        self.shadow_prg['m_mdl'].write(self.mdl_mtx)

    def draw_shadow(self):
        self.upd_shadow()
        self.shadow_vao.render()

    def init(self):
        self.prg['m_view_light'].write(self.app.light.m_view_light)
        self.prg['u_res'].write(gl.vec2(self.app.win_dim))
        self.depth_tex = self.app.mesh.tex.texs['depth_tex']
        self.prg['shadowMap'] = 1
        self.depth_tex.use(location=1)
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_prg = self.shadow_vao.program
        self.shadow_prg['m_proj'].write(self.cam.m_proj)
        self.shadow_prg['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_prg['m_mdl'].write(self.mdl_mtx)
        self.tex = self.app.mesh.tex.texs[self.tex]
        self.prg['u_tex_0'] = 0
        self.tex.use(location=0)
        self.prg['m_proj'].write(self.cam.m_proj)
        self.prg['m_view'].write(self.cam.m_view)
        self.prg['m_mdl'].write(self.mdl_mtx)
        self.prg['light.pos'].write(self.app.light.pos)
        self.prg['light.Ia'].write(self.app.light.Ia)
        self.prg['light.Id'].write(self.app.light.Id)
        self.prg['light.Is'].write(self.app.light.Is)

class Cube(ExtModel):
    def __init__(self, app, vao='cube', tex=0, pos=(0, 0, 0), rot=(0, 0, 0), scl=(1, 1, 1)):
        super().__init__(app, vao, tex, pos, rot, scl)

class MovCube(Cube):
    def upd(self):
        self.mdl_mtx = self.get_mdl_mtx()
        super().upd()

class Cat(ExtModel):
    def __init__(self, app, vao='cat', tex='cat', pos=(0, 0, 0), rot=(-90, 0, 0), scl=(1, 1, 1)):
        super().__init__(app, vao, tex, pos, rot, scl)

class SkyBox(Model):
    def __init__(self, app, vao='skybox', tex='skybox', pos=(0, 0, 0), rot=(0, 0, 0), scl=(1, 1, 1)):
        super().__init__(app, vao, tex, pos, rot, scl)
        self.init()

    def upd(self):
        self.prg['m_view'].write(gl.mat4(gl.mat3(self.cam.m_view)))

    def init(self):
        self.tex = self.app.mesh.tex.texs[self.tex]
        self.prg['u_tex_skybox'] = 0
        self.tex.use(location=0)
        self.prg['m_proj'].write(self.cam.m_proj)
        self.prg['m_view'].write(gl.mat4(gl.mat3(self.cam.m_view)))

class AdvSkyBox(Model):
    def __init__(self, app, vao='adv_skybox', tex='skybox', pos=(0, 0, 0), rot=(0, 0, 0), scl=(1, 1, 1)):
        super().__init__(app, vao, tex, pos, rot, scl)
        self.init()

    def upd(self):
        m_view = gl.mat4(gl.mat3(self.cam.m_view))
        self.prg['m_invProjView'].write(gl.inverse(self.cam.m_proj * m_view))

    def init(self):
        self.tex = self.app.mesh.tex.texs[self.tex]
        self.prg['u_tex_skybox'] = 0
        self.tex.use(location=0)
