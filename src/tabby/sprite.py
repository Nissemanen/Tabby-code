from src.tabby.blocks import *
from src.tabby import json_project
import os
import random
import string

__all__ = ["Sprite"]

class Sprite():
    def __init__(self, name: str,current_costume: int = 0, volume: int = 100, visible: bool = True, position: (int, int) = (0, 0), size: int = 100, direction: int = 90, draggable: bool = False, rotation_style: str = "all around"):
        _temp = 1
        for target in json_project["targets"]:
            if not target["isStage"]:
                if target["layerOrder"] > _temp:
                    _temp = target["layerOrder"]

        self.sprite_num = len(json_project["targets"])

        json_project["targets"] += [{
            "isStage": False,
            "name": name,
            "variables": [],
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": current_costume,
            "costumes": [],
            "sounds": [],
            "volume": volume,
            "layerOrder": _temp,
            "visible": visible,
            "x": position[0],
            "y": position[1],
            "size": size,
            "direction": direction,
            "draggable": draggable,
            "rotationStyle": rotation_style
        }]
    
    #Motion Blocks
    def move(self, steps: float):
        json_project["targets"][self.sprite_num]["blocks"][''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"')] = {

        }


    def turn(self, degrees: float):

        if degrees < 0:
            raise NotImplementedError("This method is not available.")

        else:
            raise NotImplementedError("This method is not available.")

    def go_to(self, position):
        raise NotImplementedError("This method is not available.")

    def glide_to(self, seconds: float, position):
        raise NotImplementedError("This method is not available.")

    def point_in_direction(self, degrees: int): #degrees
        raise NotImplementedError("This method is not available.")

    def point_towards(self, thing): # position
        raise NotImplementedError("This method is not available.")

    def change_x_by(self, amount: int):
        raise NotImplementedError("This method is not available.")

    def set_x_to(self, amount: int):
        raise NotImplementedError("This method is not available.")

    def change_y_by(self, amount: int):
        raise NotImplementedError("This method is not available.")

    def set_y_to(self, amount: int):
        raise NotImplementedError("This method is not available.")

    def if_on_edge_bounce(self):
        raise NotImplementedError("This method is not available.")

    def set_rotation_style(self, style):
        raise NotImplementedError("This method is not available.")