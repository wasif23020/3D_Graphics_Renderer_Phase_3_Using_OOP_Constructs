import numpy as np
import moderngl as mgl

class SkyTexture:
    def __init__(self, ctx, texture_data):
        self.ctx = ctx
        self.texture_data = texture_data
        self.texture = None

    def load_texture(self):
        self.texture = self.ctx.texture(self.texture_data.shape[:2], 3, self.texture_data.tobytes())

    def bind_texture(self):
        self.texture.use()

    def render_sky(self):
        prog = self.ctx.program(
            vertex_shader="""
            #version 330
            in vec2 in_vert;
            out vec2 tex_coord;
            void main() {
                tex_coord = in_vert * 0.5 + 0.5;
                gl_Position = vec4(in_vert, 0.0, 1.0);
            }
            """,
            fragment_shader="""
            #version 330
            in vec2 tex_coord;
            out vec4 fragColor;
            uniform sampler2D sky_texture;
            void main() {
                fragColor = texture(sky_texture, tex_coord);
            }
            """
        )

        vertices = np.array([-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0], dtype='f4')
        vbo = self.ctx.buffer(vertices)
        vao = self.ctx.simple_vertex_array(prog, vbo, 'in_vert')

        prog['sky_texture'] = 0
        vao.render(mgl.TRIANGLE_FAN)