import numpy as np

class SceneObject:
    def __init__(self, vertex_data, position=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0)):
        self.vertex_data = vertex_data
        self.position = np.array(position, dtype=np.float32)
        self.rotation = np.array(rotation, dtype=np.float32)

    def set_position(self, x, y, z):
        self.position = np.array((x, y, z), dtype=np.float32)

    def set_rotation(self, x, y, z):
        self.rotation = np.array((x, y, z), dtype=np.float32)

    def get_model_matrix(self):
        translation_matrix = np.identity(4)
        translation_matrix[:3, 3] = self.position

        rotation_matrix = self._compute_rotation_matrix()

        return np.dot(translation_matrix, rotation_matrix)

    def _compute_rotation_matrix(self):
        rot_x = self.rotation[0]
        rot_y = self.rotation[1]
        rot_z = self.rotation[2]

        rot_x_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(rot_x), -np.sin(rot_x), 0],
            [0, np.sin(rot_x), np.cos(rot_x), 0],
            [0, 0, 0, 1]
        ])

        rot_y_matrix = np.array([
            [np.cos(rot_y), 0, np.sin(rot_y), 0],
            [0, 1, 0, 0],
            [-np.sin(rot_y), 0, np.cos(rot_y), 0],
            [0, 0, 0, 1]
        ])

        rot_z_matrix = np.array([
            [np.cos(rot_z), -np.sin(rot_z), 0, 0],
            [np.sin(rot_z), np.cos(rot_z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        return np.dot(rot_x_matrix, np.dot(rot_y_matrix, rot_z_matrix))

class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self):
        for obj in self.objects:
            model_matrix = obj.get_model_matrix()