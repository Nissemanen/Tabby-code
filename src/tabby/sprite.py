from src.tabby.packager import json_project
from src.tabby.packager import initialized_sprites as in_sp
import random
import string

__all__ = ["Sprite"]

_random_safe_characters = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'), k=20))

class Sprite:
    def __init__(self, name: str,current_costume: int = 0, volume: int = 100, visible: bool = True, position: tuple[int, int] = (0, 0), size: int = 100, direction: int = 90, draggable: bool = False, rotation_style: str = "all around"):

        _temp = 1
        for target in json_project["targets"]:

            if not target["isStage"]:
                if target["layerOrder"] >= _temp:
                    _temp = target["layerOrder"] + 1

        self.__sprite_num = len(json_project["targets"])

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

        in_sp.append(f'{name}')
    
    def __add_block(self, opcode, nextC=None, parent=None, inputs:dict=None, fields:dict=None, shadow=False, topLevel=True, x=0, y=0, name=None):
        if not name:
            name = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'), k=20))
        if topLevel:
            json_project["targets"][self.sprite_num]["blocks"][name] = {
                "opcode":opcode,
                "next":nextC,
                "parent":parent,
                "inputs":inputs,
                "fields":fields,
                "shadow":shadow,
                "topLevel":True,
                "x":x,
                "y":y
            }
        else:
            json_project["targets"][self.sprite_num]["blocks"][name] = {
                "opcode":opcode,
                "next":nextC,
                "parent":parent,
                "inputs":inputs,
                "fields":fields,
                "shadow":shadow,
                "topLevel":False

            }

        return name

    #Motion Blocks
    def move(self, steps: int):
        """
        Moves the sprite forward the number of steps in the direction the sprite is facing.

        :param steps:
        :type steps: int
        :return:
        """
        self.__add_block("motion_movesteps",inputs={"STEPS":[1,[4,f"{steps}"]]})

    def turn(self, degrees: int):
        """
        Turns the sprite the specified amount. Positive for clockwise, negative for counterclockwise

        :param degrees:
        :type degrees: int
        :return:
        """
        if degrees >= 0:
            self.__add_block("motion_turnright",inputs={"DEGREES":[1,[4,f"{degrees}"]]})
        else:
            self.__add_block("motion_turnleft",inputs={"DEGREES":[1,[4,f"{-degrees}"]]})

    def go_to(self, position: tuple[int, int] | str):
        """
        Moves the sprite to the coordinates, "mouse_pointer", "random" or another sprite.

        :param position:
        :return:
        """

        if isinstance(position, tuple):
            self.__add_block("motion_gotoxy",inputs={"X":[1,[4,f'{position[0]}']],"Y":[1,[4,f'{position[1]}']]})
        elif position in ["mouse_pointer", "random"] + in_sp:
            _name1 = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'), k=20))
            _name2 = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'), k=20))

            self.__add_block("motion_goto", inputs={"TO":[1, _name2]}, name=_name1)

            if position == "mouse_pointer":
                self.__add_block("motion_goto_menu", fields={"TO":["_mouse_", None]}, parent=_name1, name=_name2)
            elif position == "random":
                self.__add_block("motion_goto_menu", fields={"TO":["_random_", None]}, parent=_name1, name=_name2)
            else:
                self.__add_block("motion_goto_menu", fields={"TO":[f'{position}', None]}, parent=_name1, name=_name2)
        else:
            raise SyntaxError(f'incorrect input for "position". expected type tuple or str, got {type(position)}')

    def glide_to(self, seconds: float, position):
        """
        Glides the sprite to the coordinates, "mouse_pointer", "random" or another sprite, taking as long as the specified amount of time

        :param seconds:
        :param position:
        :return:
        """
        if isinstance(position, tuple):
            self.__add_block("motion_glidesecstoxy", inputs={"SECS":[1,[4,f"{seconds}"]],"X":[1,(4,f"{position[0]}")],"Y":[1,[4,f"{position[1]}"]]})
        elif position in ["mouse_pointer", "random"] + in_sp:
            _name1 = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'),k=20))
            _name2 = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'),k=20))

            self.__add_block("motion_glideto", inputs={"SECS":[1,[4,f"{seconds}"]],"TO": [1, _name2]}, name=_name1)

            if position == "mouse_pointer":
                self.__add_block("motion_glideto_menu", fields={"TO": ["_mouse_", None]}, parent=_name1, name=_name2)
            elif position == "random":
                self.__add_block("motion_glideto_menu", fields={"TO": ["_random_", None]}, parent=_name1, name=_name2)
            else:
                self.__add_block("motion_glideto_menu", fields={"TO": [position, None]}, parent=_name1, name=_name2)
        else:
            raise SyntaxError(f'incorrect input for "position". expected type tuple or str, got {type(position)}')


    def point_in_direction(self, degrees: int): #degrees
        """
        Points the sprite in the direction.

        :param degrees:
        :return:
        """
        self.__add_block("motion_pointindirection", inputs={"DIRECTION":[1,[4,f"{degrees}"]]})
        pass

    def point_towards(self, thing:str): # position
        """
        Points the sprite towards the mouse_pointer or another sprite.

        :param thing:
        :return:
        """
        if thing == "mouse_pointer" or thing in in_sp:
            _name1 = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'),k=20))
            _name2 = ''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'),k=20))

            self.__add_block("motion_pointtowards", inputs={"TOWARDS":[1, _name2]}, name=_name1)
            if thing == "mouse_pointer":
                self.__add_block("motion_pointtowards_menu", fields={"TOWARDS":["_mouse_", None]}, name=_name2, parent=_name1)

            else:
                self.__add_block("motion_pointtowards_menu", fields={"TOWARDS":[thing, None]}, name=_name2, parent=_name1)

        else:
            raise SyntaxError(f'incorrect input for "thing". expected "mouse_pointer" or a sprite\'s name, got "{thing}"')

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

    # Looks
    def say(self, text: str, seconds: float = None):
        raise NotImplementedError("This method is not available.")

    def think(self, text: str, seconds: float = None):
        raise NotImplementedError("This method is not available.")

    def switch_costume_to(self, costume):
        raise NotImplementedError("This method is not available.")

    def next_costume(self):
        raise NotImplementedError("This method is not available.")

    def switch_backdrop_to(self, backdrop: str, wait: bool = False):
        raise NotImplementedError("This method is not available.")

    def next_backdrop(self):
        raise NotImplementedError("This method is not available.")

    def change_size_by(self, amount: int):
        raise NotImplementedError("This method is not available.")

    def set_size_to(self, amount: int):
        raise NotImplementedError("This method is not available.")

    def change_graphic_effect_by(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        raise NotImplementedError("This method is not available.")

    def set_graphic_effect_to(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(
                f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        raise NotImplementedError("This method is not available.")

    def clear_graphic_effects(self):
        raise NotImplementedError("This method is not available.")

    def show(self):
        raise NotImplementedError("This method is not available.")

    def hide(self):
        raise NotImplementedError("This method is not available.")

    def go_to_layer(self, layer, amount: int = None):
        raise NotImplementedError("This method is not available.")

    # Sound
    def play_sound(self, sound, until_done: bool = False):
        raise NotImplementedError("This method is not available.")

    def stop_all_sounds(self):
        raise NotImplementedError("This method is not available.")

    def change_sound_effect_by(self, effect, amount: float):
        raise NotImplementedError("This method is not available.")

    def set_sound_effect_to(self, effect, amount: float):
        raise NotImplementedError("This method is not available.")

    def clear_all_sound_effects(self):
        raise NotImplementedError("This method is not available.")

    def change_volume(self):
        raise NotImplementedError("This method is not available.")

    def set_volume(self):
        raise NotImplementedError("This method is not available.")

    # Events
    def when_green_flag_clicked(self, func):
        def wrapper():
            raise NotImplementedError("This method is not available.")

    def when_key_pressed(self, func, key):
        def wrapper():
            raise NotImplementedError("This method is not available.")

    def when_this_sprite_clicked(self, func):
        def wrapper():
            raise NotImplementedError("This method is not available.")

    def when_backdrop_switches_to(self, func, backdrop):
        def wrapper():
            raise NotImplementedError("This method is not available.")

    def when_x_is_bigger_then_y(self, func, first, second):
        def wrapper():
            raise NotImplementedError("This method is not available.")

    def when_i_recive(self, func, message):
        def wrapper():
            raise NotImplementedError("This method is not available.")

    def broudcast(self, message, wait: bool = False):
        raise NotImplementedError("This method is not available.")