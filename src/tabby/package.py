import os
import json
from src.tabby import json_project

def package(path, version: int = 3):
    json.dump(json_project, path)
    print(f'Successfully packaged project to "{path}"')