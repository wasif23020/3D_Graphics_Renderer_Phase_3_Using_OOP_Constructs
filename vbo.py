import numpy as npy
import moderngl as mgl
import pywavefront as pfw


class CustomVertexBufferObject:
    def __init__(self, context):
        self.vbos = {}
        self.vbos['my_cube'] = CustomCubeVBO(context)
        self.vbos['my_cat'] = CustomCatVBO(context)
        self.vbos['my_skybox'] = CustomSkyBoxVBO(context)
        self.vbos['my_advanced_skybox'] = CustomAdvancedSkyBoxVBO(context)

    def destroy(self):
        for vbo in self.vbos.values():
            vbo.destroy()


class CustomBaseVBO:
    def __init__(self, context):
        self.context = context
        self.vbo = self.create_custom_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_custom_vertex_data(self):
        raise NotImplementedError("Method 'get_custom_vertex_data' must be implemented in subclass.")

    def create_custom_vbo(self):
        vertex_data = self.get_custom_vertex_data()
        vbo = self.context.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class CustomCubeVBO(CustomBaseVBO):
    def __init__(self, context):
        super().__init__(context)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def generate_custom_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return npy.array(data, dtype='f4')

    def get_custom_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.generate_custom_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1), ]
        tex_coord_data = self.generate_custom_data(tex_coord_vertices, tex_coord_indices)

        normals = [(0, 0, 1) * 6,
                   (1, 0, 0) * 6,
                   (0, 0, -1) * 6,
                   (-1, 0, 0) * 6,
                   (0, 1, 0) * 6,
                   (0, -1, 0) * 6, ]
        normals = npy.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = npy.hstack([normals, vertex_data])
        vertex_data = npy.hstack([tex_coord_data, vertex_data])
        return vertex_data


class CustomCatVBO(CustomBaseVBO):
    def __init__(self, context):
        super().__init__(context)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_custom_vertex_data(self):
        objs = pfw.Wavefront('objects/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = npy.array(vertex_data, dtype='f4')
        return vertex_data


class CustomSkyBoxVBO(CustomBaseVBO):
    def __init__(self, context):
        super().__init__(context)
        self.format = '3f'
        self.attribs = ['in_position']

    @staticmethod
    def generate_custom_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return npy.array(data, dtype='f4')

    def get_custom_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.generate_custom_data(vertices, indices)
        vertex_data = npy.flip(vertex_data, 1).copy(order='C')
        return vertex_data


class CustomAdvancedSkyBoxVBO(CustomBaseVBO):
    def __init__(self, context):
        super().__init__(context)
        self.format = '3f'
        self.attribs = ['in_position']

    def get_custom_vertex_data(self):
        # in clip space
        z = 0.9999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = npy.array(vertices, dtype='f4')
        return vertex_data
