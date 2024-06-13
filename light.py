import glm

class Lt:
    def __init__(self, pos=(50, 50, -10), clr=(1, 1, 1)):
        self.pos = glm.vec3(pos)
        self.clr = glm.vec3(clr)
        self.dir = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.06 * self.clr  # ambient
        self.Id = 0.8 * self.clr  # diffuse
        self.Is = 1.0 * self.clr  # specular
        # view matrix
        self.view = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.pos, self.dir, glm.vec3(0, 1, 0))
