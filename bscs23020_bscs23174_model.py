import numpy as np

class Model:
    def __init__(self):
        self.models = []

    def add_model(self, vertex_data, position=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
        model_data = {
            'vertex_data': vertex_data,
            'position': np.array(position, dtype=np.float32),
            'rotation': np.array(rotation, dtype=np.float32),
            'scale': np.array(scale, dtype=np.float32)
        }
        self.models.append(model_data)

    def set_model_position(self, model_index, x, y, z):
        self.models[model_index]['position'] = np.array((x, y, z), dtype=np.float32)

    def set_model_rotation(self, model_index, x, y, z):
        self.models[model_index]['rotation'] = np.array((x, y, z), dtype=np.float32)

    def set_model_scale(self, model_index, x_scale, y_scale, z_scale):
        self.models[model_index]['scale'] = np.array((x_scale, y_scale, z_scale), dtype=np.float32)

    def get_model_data(self, model_index):
        return self.models[model_index]

    def get_model_count(self):
        return len(self.models)