class ShaderProgram:
    def __init__(self, context):
        self.context = context
        self.programs = {}

    def load_shader(self, name, vertex_shader_code, fragment_shader_code):
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

    def get_program(self, name):
        return self.programs.get(name, None)

    def cleanup(self):
        for program in self.programs.values():
            program.release()
        self.programs.clear()


