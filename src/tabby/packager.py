import os
import json

version = "3.0.0"
vm = "11.0.0"
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 OPR/118.0.0.0"
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
    ],
    "monitors":[],
    "extensions":[],
    "meta":{
        "semver":version,
        "vm": vm,
        "agent":agent
    }
}
sprites = []
menu_items = ["_mouse_", "_random_"] # here are all the "core" names for the inputs for menus
custom_menu_items = {"mouse position":"_mouse_", "random":"_random_"} # if you make an extension which adds new menu items for all things (like "go to" or "glide to"), you can add custom names for them here for ese of use.

def print_json_output_to_terminal(formated: bool = False):
    if formated:
        print(json.dumps(json_project, indent=2))
    else:
        print(json_project)

def package(path, version: int = version):
    json.dump(json_project, path)
    print(f'Successfully packaged project to "{path}"')