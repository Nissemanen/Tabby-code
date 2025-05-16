import os
import json

version = 3
initialized_sprites = []
json_project = {
    "targets":[
        {
            "isStage": True,
            "name": "Stage",
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [],
            "sounds": [],
            "volume": 100,
            "layerOrder": 0,
            "tempo": 60,
            "videoTransparency": 50,
            "videoState": "on",
            "textToSpeechLanguage": None
        }
    ]
}

def print_json_output_to_terminal(formated: bool = False):
    if formated:
        print(json.dumps(json_project, indent=2))
    else:
        print(json_project)

def package(path, version: int = version):
    json.dump(json_project, path)
    print(f'Successfully packaged project to "{path}"')