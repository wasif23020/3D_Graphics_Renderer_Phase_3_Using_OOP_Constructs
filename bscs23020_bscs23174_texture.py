from PIL import Image
import numpy as np

class TextureLoader:
    def __init__(self, context):
        self.context = context
        self.textures = {}

    def load_texture(self, name, filepath):
        image = self._load_image(filepath)
        texture = self._create_texture(image)
        self.textures[name] = texture

    def _load_image(self, filepath):
        image = Image.open(filepath)
        image = image.convert("RGBA")
        image_data = np.array(image).astype('f4')
        return image_data

    def _create_texture(self, image_data):
        texture = self.context.texture(
            image_data.shape[:2],
            components=4,
            data=image_data.tobytes()
        )
        texture.use()
        return texture

    def get_texture(self, name):
        return self.textures.get(name, None)

    def cleanup(self):
        for texture in self.textures.values():
            texture.release()
        self.textures.clear()