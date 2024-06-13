import moderngl as gl

class ShaderProg:
    def __init__(self, context):
        self.ctx = context
        self.progs = {}
        self.progs['default'] = self.create_prog('default')
        self.progs['skybox'] = self.create_prog('skybox')
        self.progs['adv_skybox'] = self.create_prog('adv_skybox')
        self.progs['shadow'] = self.create_prog('shadow_map')

    def create_prog(self, name):
        with open(f'shaders/{name}.vert') as v_file:
            v_shader = v_file.read()

        with open(f'shaders/{name}.frag') as f_file:
            f_shader = f_file.read()

        prog = self.ctx.program(vertex_shader=v_shader, fragment_shader=f_shader)
        return prog

    def destroy(self):
        for prog in self.progs.values():
            prog.release()