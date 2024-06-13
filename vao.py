from vbo import CustomVertexBufferObject
from shader_program import ShaderProg


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = CustomVertexBufferObject(ctx)
        self.program = ShaderProg(ctx)
        self.vaos = {}

        self.vaos['box'] = self.create_vao(self.program.progs['def'], self.vbo.vbos['box'])
        self.vaos['shadow_box'] = self.create_vao(self.program.progs['shadow'], self.vbo.vbos['box'])
        self.vaos['cat'] = self.create_vao(self.program.progs['def'], self.vbo.vbos['cat'])
        self.vaos['shadow_cat'] = self.create_vao(self.program.progs['shadow'], self.vbo.vbos['cat'])
        self.vaos['sky'] = self.create_vao(self.program.progs['sky'], self.vbo.vbos['sky'])
        self.vaos['advanced_sky'] = self.create_vao(self.program.progs['adv_sky'], self.vbo.vbos['adv_sky'])

    def create_vao(self, prog, vbo):
        vao = self.ctx.vertex_array(prog, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
