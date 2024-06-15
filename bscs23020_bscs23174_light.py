import numpy as np

class Light:
    def __init__(self, position=(0.0, 0.0, 0.0), direction=(0.0, 0.0, -1.0), color=(1.0, 1.0, 1.0), intensity=1.0):
        self.position = np.array(position, dtype=np.float32)
        self.direction = np.array(direction, dtype=np.float32)
        self.color = np.array(color, dtype=np.float32)
        self.intensity = intensity

    def set_position(self, x, y, z):
        self.position = np.array((x, y, z), dtype=np.float32)

    def set_direction(self, x, y, z):
        self.direction = np.array((x, y, z), dtype=np.float32)
        self.direction = self.direction / np.linalg.norm(self.direction)  # Normalize the direction vector

    def set_color(self, r, g, b):
        self.color = np.array((r, g, b), dtype=np.float32)

    def set_intensity(self, intensity):
        self.intensity = intensity

    def get_light_data(self):
        return {
            'position': self.position,
            'direction': self.direction,
            'color': self.color,
            'intensity': self.intensity
        }

    def apply_to_shader(self, shader, uniform_name):
        shader[uniform_name + ".position"].write(self.position.tobytes())
        shader[uniform_name + ".direction"].write(self.direction.tobytes())
        shader[uniform_name + ".color"].write(self.color.tobytes())
        shader[uniform_name + ".intensity"].write(np.array([self.intensity], dtype=np.float32).tobytes())
