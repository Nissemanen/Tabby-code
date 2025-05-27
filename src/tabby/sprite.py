from .packager import json_project
from .packager import sprites
from .packager import menu_items
from .packager import custom_menu_items
import random
import string

# if you are a curious person, wanting to know how this works.
# then ive added some notes here and there to say what something 
# does if it looks to "cryptic".

class Sprite:
    def __init__(self, name:str):
        sprites.append(name)
        self.name = name
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
                self.__parent = name


        json_project["targets"][self.__sprite_num]["blocks"][name]["parent"] = parent


    def move(self, steps):
        self.__add_block("motion_movesteps", inputs={"STEPS":[1,[4,f'{steps}']]})

    def turn_right(self, degrees):
        self.__add_block("motion_turnright", inputs={"DEGREES":[1,[4,f'{degrees}']]})

    def turn_left(self, degrees):
        self.__add_block("motion_turnleft", inputs={"DEGREES":[1,[4,f'{degrees}']]})

    def turn(self, degrees:int):
        if degrees > -1:
            self.turn_right(degrees)
        else:
            self.turn_left(-degrees)

    def go_to_position(self, position:tuple[int, int]):
        self.__add_block("motion_gotoxy", inputs={"X":[1,[4,f'{position[0]}']], "Y":[1,[4,f'{position[1]}']]})

    def go_to_thing(self, item: str):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("motion_goto", inputs={"TO":[1, name2]}, name=name1)
        self.__add_block("motion_goto_menu", fields={"TO":[item, None]}, name=name2, parent=name2)

    def go_to(self, placement:tuple[int, int] | str):
        if isinstance(placement, (int, int)):
            self.go_to_position(placement)

        elif isinstance(placement, str):
            if placement in menu_items or sprites and placement != self.name:
                self.go_to_thing(placement)

            else:
                try:
                    if custom_menu_items[placement]:
                        self.go_to_thing(placement)

                except KeyError:
                    raise SyntaxError(f'{placement} is not a valid input.')



    
    def point_in_direction(self, direction):
        self.__add_block("motion_pointindirection", inputs={"DIRECTION":[1,[8, f'{direction}']]})

    def point_towards(self, item:str):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("motion_pointtowards", inputs={"TOWARDS":[1, name2]}, name=name1)
        self.__add_block("motion_pointtowards_menu", fields={"TOWARDS":[item, None]}, name=name2, parent=name2)

    def point(self, direction: int | str):
        if isinstance(direction, int):
            self.point_in_direction(direction)

        elif isinstance(direction, str):
            if direction in menu_items or sprites and direction != self.name:
                self.point_towards(direction)

            else:
                try:
                    if custom_menu_items[direction]:
                        self.point_towards(direction)

                except KeyError:
                    raise SyntaxError(f'{direction} is not a valid input.')

    def when_flag_clicked(self, func):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whenflagclicked", name=_name)
        self.__parent = _name
        func()
        self.__parent = None