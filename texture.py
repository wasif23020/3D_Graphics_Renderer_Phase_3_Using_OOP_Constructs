import pygame as pyg
import moderngl as mgl

class TexLoader:
    def __init__(self, app):
        self.app = app
        self.ctx = app.gl_context
        self.tex = {}
        self.tex[0] = self.load('textures/img.png')
        self.tex[1] = self.load('textures/img_1.png')
        self.tex[2] = self.load('textures/img_2.png')
        self.tex['cat'] = self.load('objects/cat/20430_cat_diff_v1.jpg')
        self.tex['skybox'] = self.load_cube('textures/skybox1/', 'png')
        self.tex['depth'] = self.depth()

    def depth(self):
        d = self.ctx.depth_texture(self.app.window_dimensions)
        d.repeat_x = False
        d.repeat_y = False
        return d

    def load_cube(self, dir, ext='png'):
        faces = ['right', 'left', 'top', 'bottom', 'front', 'back'][::-1]
        textures = []

        for f in faces:
            path = f'{dir}{f}.{ext}'
            surface = pyg.image.load(path).convert()
            if f in ['right', 'left', 'front', 'back']:
                surface = pyg.transform.flip(surface, True, False)
            else:
                surface = pyg.transform.flip(surface, False, True)
            textures.append(surface)

        size = textures[0].get_size()
        cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            data = pyg.image.tostring(textures[i], 'RGB')
            cube.write(face=i, data=data)

        return cube

    def load(self, path):
        surf = pyg.image.load(path).convert()
        surf = pyg.transform.flip(surf, False, True)
        tex = self.ctx.texture(size=surf.get_size(), components=3, data=pg.image.tostring(surf, 'RGB'))
        tex.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        tex.build_mipmaps()
        tex.anisotropy = 32.0
        return tex

    def destroy(self):
        for t in self.tex.values():
            t.release()
