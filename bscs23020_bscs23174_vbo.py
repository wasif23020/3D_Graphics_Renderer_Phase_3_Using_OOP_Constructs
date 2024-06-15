import numpy as np
import pywavefront
class PlayerVBO(BaseVBO):
    def _init_(self, app):
        super()._init_(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/player/Tommy Vercetti.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
class VertexBufferManager:
    def __init__(self, context):
        self.context = context
        self.buffers = {}

    def add_vbo(self, name, obj_file_path, layout, attributes):
        self.buffers[name] = GenericVBO(self.context, obj_file_path, layout, attributes)

    def destroy_all(self):
        for buffer in self.buffers.values():
            buffer.destroy()


class GenericVBO:
    def __init__(self, context, obj_file_path, layout, attributes):
        self.context = context
        self.layout = layout
        self.attributes = attributes
        self.vbo = self.create_vbo(obj_file_path)

    def create_vbo(self, obj_file_path):
        vertex_data = self.load_vertex_data(obj_file_path)
        vbo = self.context.buffer(vertex_data)
        return vbo

    def load_vertex_data(self, obj_file_path):
        objs = pywavefront.Wavefront(obj_file_path, cache=True, parse=True)
        vertex_data = []
        for name, material in objs.materials.items():
            vertex_data.extend(material.vertices)
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

    def destroy(self):
        self.vbo.release()


    vbo_manager = VertexBufferManager(ctx)
    vbo_manager.add_vbo("cube", "path/to/cube.obj", "2f 3f 3f", ['in_texcoord_0', 'in_normal', 'in_position'])
    vbo_manager.add_vbo("cat", "path/to/cat.obj", "2f 3f 3f", ['in_texcoord_0', 'in_normal', 'in_position'])
    vbo_manager.add_vbo("player", "path/to/player.obj", "2f 3f 3f", ['in_texcoord_0', 'in_normal', 'in_position'])
    vbo_manager.add_vbo("skybox", "path/to/skybox.obj", "3f", ['in_position'])
    vbo_manager.add_vbo("advanced_skybox", "path/to/advanced_skybox.obj", "3f", ['in_position'])


    vbo_manager.destroy_all()
