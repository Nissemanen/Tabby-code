from .packager import json_project
from .packager import sprites
import random
import string

# if you are a curious person, wanting to know how this works.
# then ive added some notes here and there to say what something 
# does if it looks to "cryptic".

class Sprite:
    def __init__(self, name:str):
        sprites.append(name)
        self.__sprite_num = len(sprites)
        self.__parent = None
        
        json_project["targets"] += [{
            "isStage": False,
            "name": name,
            "variables": [],
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [],
            "sounds": [],
            "volume": 100,
            "layerOrder": len(sprites),
            "visible": True,
            "x": 0,
            "y": 0,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "all around"
        }]
    
    @staticmethod #it basically means that this function does not need to know the "self".
    def __random_name():
        return ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'), k=20))
    
    def __add_block(self, opcode, parent=None, child=None, name=None, inputs=None, fields=None, shadow=None):
        if fields is None:
            fields = {}
        if inputs is None:
            inputs = {}
        if not name:
            name = self.__random_name()
        
        if not parent:
            parent = self.__parent
            if not parent:
                topLevel = True
                x = 0
                y = 0

        json_project["targets"][self.__sprite_num]["blocks"][name] = { # this adds the sprite to the final JSON code
            "opcode": opcode,
            "next": None,
            "parent": parent,
            "inputs": inputs,
            "fields": fields,
            "shadow": shadow,
            "topLevel": False
        }
    
    def when_flag_clicked(self):
        pass