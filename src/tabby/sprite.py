from src.tabby.blocks import *
from src.tabby import json_project
import os

__all__ = ["Sprite"]

class Sprite(MotionBlocks, LooksBlocks, SoundBlocks, EventBlocks, ControlBlocks):

    position = (0, 0)
    size = 100
    show = True
    rotation = 90
    rotation_style = "All_Around"
    
    def __init__(self, name: str,current_costume: int = 0, volume: int = 100, visible: bool = True, position: (int, int) = (0, 0), size: int = 100, direction: int = 90, draggable: bool = False, rotation_style: str = "all around"):
        _temp = 1
        for target in json_project["targets"]:
            if not target["isStage"]:
                if target["layerOrder"] > _temp:
                    _temp = target["layerOrder"]

        self.json = [{
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