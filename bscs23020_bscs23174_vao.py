class VertexArrayManager:
    def __init__(self, context):
        self.context = context
        self.vaos = {}

    def add_vao(self, name, program, buffers, attributes):
        self.vaos[name] = self._create_vao(program, buffers, attributes)

    def _create_vao(self, program, buffers, attributes):
        buffer_descriptions = [(buffer, layout, *attribs) for buffer, layout, attribs in buffers]
        vao = self.context.vertex_array(program, buffer_descriptions, skip_errors=True)
        return vao

    def get_vao(self, name):
        return self.vaos.get(name, None)

    def cleanup(self):
        for vao in self.vaos.values():
            vao.release()
        self.vaos.clear()

 self.vaos['player'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['player'])