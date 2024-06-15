import numpy as np

class Shadow:
    def __init__(self, ctx):
        self.ctx = ctx

    def generate_shadow(self, vao):
        vertices = vao.vbo.read().reshape(-1, 3)

        light_direction = np.array([0, -1, 0], dtype='f4')
        shadow_vertices = []
        for vertex in vertices:
            shadow_vertex = vertex - light_direction * (vertex[1] / light_direction[1])
            shadow_vertices.extend(shadow_vertex)

        shadow_vbo = self.ctx.buffer(np.array(shadow_vertices, dtype='f4'))

        shadow_vao_content = [(shadow_vbo, '3f', 'in_position')]
        shadow_vao = self.ctx.vertex_array(vao.program, shadow_vao_content)

        return shadow_vao