class SceneRenderer:
    def __init__(self, context):
        self.context = context
        self.programs = {}
        self.vaos = {}

    def load_shader_program(self, name, vertex_shader_code, fragment_shader_code):
        program = self._create_program(vertex_shader_code, fragment_shader_code)
        self.programs[name] = program

    def _compile_shader(self, shader_type, source):
        shader = self.context.shader(shader_type, source)
        return shader

    def _create_program(self, vertex_shader_code, fragment_shader_code):
        vertex_shader = self._compile_shader(self.context.VERTEX_SHADER, vertex_shader_code)
        fragment_shader = self._compile_shader(self.context.FRAGMENT_SHADER, fragment_shader_code)

        program = self.context.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader,
        )
        return program

    def create_vao(self, name, program_name, buffers):
        program = self.programs.get(program_name)
        if not program:
            raise ValueError(f"Program '{program_name}' not found")

        buffer_descriptions = [(buffer, layout, *attribs) for buffer, layout, attribs in buffers]
        vao = self.context.vertex_array(program, buffer_descriptions, skip_errors=True)
        self.vaos[name] = vao

    def render(self, vao_name):
        vao = self.vaos.get(vao_name)
        if not vao:
            raise ValueError(f"VAO '{vao_name}' not found")

        vao.render()

    def cleanup(self):
        for program in self.programs.values():
            program.release()
        self.programs.clear()

        for vao in self.vaos.values():
            vao.release()
        self.vaos.clear()
