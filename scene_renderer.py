import moderngl as gl

class Renderer:
    def __init__(self, application):
        self.app = application
        self.ctx = application.gl_context
        self.mesh = application.mesh
        self.scene = application.scene
        self.depth_tex = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_tex)

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    def render_main(self):
        self.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()
        self.scene.skybox.render()

    def render_all(self):
        self.scene.update()
        self.render_shadow()
        self.render_main()

    def clean(self):
        self.depth_fbo.release()
