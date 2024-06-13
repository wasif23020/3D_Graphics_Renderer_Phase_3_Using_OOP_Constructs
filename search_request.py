import requests
import json

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
GITHUB_API_URL = 'https://api.github.com/search/code'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def search_github_code(query):
    params = {
        'q': query,
        'per_page': 10  # Adjust this number based on how many results you want to fetch
    }
    response = requests.get(GITHUB_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Example queries
queries = [
    "import pygame as pg",
    "import moderngl as mgl",
    "import sys",
    "from model import *",
    "from camera import Cam",
    "from light import Lt",
    "from mesh import Mesh as Msh",
    "from scene import Scene as Scn",
    "from scene_renderer import Renderer as ScnRndr",
    "class RndrEng:",
    "def __init__(self, win_size=(1600, 900))",
    "pg.init()",
    "self.win_size = win_size",
    "pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)",
    "pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)",
    "pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)",
    "pg.display.set_mode(self.win_size, flags=pg.OPENGL | pg.DOUBLEBUF)",
    "pg.event.set_grab(True)",
    "pg.mouse.set_visible(False)",
    "self.gl_ctx = mgl.create_context()",
    "self.gl_ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)",
    "self.clock = pg.time.Clock()",
    "self.curr_time = 0",
    "self.frame_time = 0",
    "self.lt = Lt()",
    "self.cam = Cam(self)",
    "self.mesh = Msh(self)",
    "self.light = self.lt",
    "self.scn = Scn(self)",
    "self.rndr = ScnRndr(self)",
    "def handle_evnts(self):",
    "for e in pg.event.get():"
]

for query in queries:
    results = search_github_code(query)
    if results:
        print(f"Results for query: {query}")
        for item in results.get('items', []):
            print(f"Repository: {item['repository']['full_name']}")
            print(f"File: {item['path']}")
            print(f"URL: {item['html_url']}")
            print("-" * 40)
    else:
        print(f"No results found for query: {query}")
