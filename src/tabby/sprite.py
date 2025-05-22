from .packager import json_project
from .packager import sprites
from .packager import print_json_output_to_terminal
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


        json_project["targets"][self.__sprite_num]["blocks"][name] = {  # this adds the sprite to the final JSON code
            "opcode": opcode,
            "next": child,
            "parent": None,
            "inputs": inputs,
            "fields": fields,
            "shadow": shadow,
            "topLevel": False
        }


        if not parent:
            parent = self.__parent
            if not parent:
                x = 0
                y = 0
                json_project["targets"][self.__sprite_num]["blocks"][name]["topLevel"] = True # this goes in the newly made block and makes it top level
                json_project["targets"][self.__sprite_num]["blocks"][name]["x"] = x           # i.e, it has no parents so it needs x y coordinates
                json_project["targets"][self.__sprite_num]["blocks"][name]["y"] = y
            else:
                json_project["targets"][self.__sprite_num]["blocks"][self.__parent]["next"] = name


        json_project["targets"][self.__sprite_num]["blocks"][name]["parent"] = parent


    def move(self, steps):
        self.__add_block("motion_movesteps", inputs={"STEPS":[1,[4,f'{steps}']]})
    
    def when_flag_clicked(self, func):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whenflagclicked")
        self.__parent = _name
        print_json_output_to_terminal(True)
        func()
        self.__parent = None