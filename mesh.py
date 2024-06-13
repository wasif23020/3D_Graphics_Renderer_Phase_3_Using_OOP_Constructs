from vao import VAO
from texture import TexLoader

class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.gl_ctx)
        self.tex = TexLoader(app)

    def destroy(self):
        self.vao.destroy()
        self.tex.destroy()
