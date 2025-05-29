from .packager import (
    json_project,
    sprites,
    motion_menu_items,
    custom_motion_menu_items
)
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
                json_project["targets"][self.__sprite_num]["blocks"][name]["x"] = x           # i.e. it has no parents so it needs x y coordinates
                json_project["targets"][self.__sprite_num]["blocks"][name]["y"] = y
            else:
                json_project["targets"][self.__sprite_num]["blocks"][self.__parent]["next"] = name
                self.__parent = name


        json_project["targets"][self.__sprite_num]["blocks"][name]["parent"] = parent

### ### ### ### Motion

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

    def go_to_thing(self, thing: str):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("motion_goto", inputs={"TO":[1, name2]}, name=name1)
        self.__add_block("motion_goto_menu", fields={"TO":[thing, None]}, name=name2, parent=name2)

    def go_to(self, placement:tuple[int, int] | str):
        if isinstance(placement, tuple) and len(placement) == 2 and all(isinstance(i, int) for i in placement):
            self.go_to_position(placement)

        elif isinstance(placement, str):
            if placement in motion_menu_items or sprites and placement != self.name:
                self.go_to_thing(placement)

            elif placement in custom_motion_menu_items:
                self.go_to_thing(custom_motion_menu_items[placement])

    def glide_to_position(self, seconds:float, position:tuple[int, int]):
        self.__add_block("motion_glidesecstoxy", inputs={"SECS":[1,[4,f'{seconds}']],"X":[1,[4,f'{position[0]}']],"Y":[1,[4,f'{position[1]}']]})

    def glide_to_thing(self, seconds:float, thing:str):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("motion_glideto", inputs={"SECS":[1,[4,f'{seconds}']],"TO": [1, name2]}, name=name1)
        self.__add_block("motion_glideto_menu", fields={"TO": [thing, None]}, name=name2, parent=name2)

    def glide_to(self, seconds:float, thing:tuple[int, int] | str):
        if isinstance(thing, tuple) and len(thing) == 2 and all(isinstance(i, int) for i in thing):
            self.glide_to_position(seconds, thing)

        elif isinstance(thing, str):
            if thing in motion_menu_items or sprites and thing != self.name:
                self.glide_to_thing(seconds, thing)

            elif thing in custom_motion_menu_items:
                self.glide_to_thing(seconds, custom_motion_menu_items[thing])

    def point_in_direction(self, direction):
        self.__add_block("motion_pointindirection", inputs={"DIRECTION":[1,[8, f'{direction}']]})

    def point_towards(self, thing:str):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("motion_pointtowards", inputs={"TOWARDS":[1, name2]}, name=name1)
        self.__add_block("motion_pointtowards_menu", fields={"TOWARDS":[thing, None]}, name=name2, parent=name2)

    def point(self, direction: int | str):
        if isinstance(direction, int):
            self.point_in_direction(direction)

        elif isinstance(direction, str):
            if direction in motion_menu_items or sprites and direction != self.name:
                self.point_towards(direction)

            elif direction in custom_motion_menu_items:
                self.go_to_thing(custom_motion_menu_items[direction])

    def change_x_by(self, amount:int):
        self.__add_block("motion_changexby", inputs={"DX":[1,[4,f'{amount}']]})

    def set_x_to(self, amount:int):
        self.__add_block("motion_setx", inputs={"X":[1,[4,f'{amount}']]})

    def change_y_by(self, amount:int):
        self.__add_block("motion_changeyby", inputs={"DY":[1,[4,f'{amount}']]})

    def set_y_to(self, amount:int):
        self.__add_block("motion_sety", inputs={"Y":[1,[4,f'{amount}']]})

    def if_on_edge_bounce(self):
        self.__add_block("motion_ifonedgebounce")

    def set_rotation_style(self, style:str):
        if style in ["left-right", "don't rotate", "all around"]:
            self.__add_block("motion_setrotationstyle", fields={"STYLE":[f'{style}', None]})

        elif style in "left right":
            self.__add_block("motion_setrotationstyle", fields={"STYLE":['left-right', None]})

        elif style in "dont rotate":
            self.__add_block("motion_setrotationstyle", fields={"STYLE":["don't rotate", None]})

### ### ### ### Looks

    def say_for_seconds(self, message:str, seconds:float):
        self.__add_block("looks_sayforsecs", inputs={"MESSAGE":[1,[10, message]], "SECS":[1,[4,f'{seconds}']]})

    def say(self, message:str):
        self.__add_block("looks_say", inputs={"MESSAGE":[1,[10,message]]})

    def think_for_seconds(self, message:str, seconds:float):
        self.__add_block("looks_thinkforsecs", inputs={"MESSAGE":[1,[10, message]], "SECS":[1,[4,f'{seconds}']]})

    def think(self, message: str):
        self.__add_block("looks_think", inputs={"MESSAGE": [1, [10, message]]})

    def switch_costume_to(self, costume): # "costume" should be "self.costumeName"
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("looks_switchcostumento", inputs={"COSTUME":[1, name2]}, name=name1)
        self.__add_block("looks_costume", fields={"COSTUME":[costume, None]}, name=name2, parent=name1)

    def next_costume(self):
        self.__add_block("looks_nextcostume")

    def switch_backdrop_to(self, backdrop): # "backdrop" should be "backdrop.backdropName" or other such as "backdrop.nextBackdrop"
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("looks_switchbackdropto", inputs={"BACKDROP":[1, name2]}, name=name1)
        self.__add_block("looks_backdrops", fields={"BACKDROP":[backdrop, None]}, parent=name1, name=name2)

    def next_backdrop(self):
        self.__add_block("looks_nextbackdrop")

    def change_size_by(self, amount:int):
        self.__add_block("looks_changesizeby", inputs={"CHANGE":[1,[4,f'{amount}']]})

    def set_size_to(self, value:int):
        self.__add_block("looks_setsizeto", inputs={"SIZE":[1,[4,f'{value}']]})

    def change_graphical_effect_by(self, effect, amount:int):
        self.__add_block("looks_changeeffectby", inputs={"CHANGE":[1,[4,f'{amount}']]}, fields={"EFFECT":[effect, None]})

    def set_graphical_effect_by(self, effect, value:int):
        self.__add_block("looks_seteffectto", inputs={"VALUE":[1,[4,f'{value}']]}, fields={"EFFECT":[effect, None]})

    def clear_graphical_effects(self):
        self.__add_block("looks_cleargraphiceffects")

    def show(self):
        self.__add_block("looks_show")

    def hide(self):
        self.__add_block("looks_hide")

    def go_to_layer(self, layer:str): #either "front" or "back"
        self.__add_block("looks_gotofrontback", fields={"FRONT_BACK":[str(layer).lower(), None]})

    def go_x_layers(self, direction:str, amount:int):
        self.__add_block("looks_goforwardbackwardlayers", inputs={"NUM":[1,[7, f'{amount}']]}, fields={"FORWARD_BACKWARD":[str(direction).lower(), None]})

### ### ### ### Sound

    def play_sound_until_done(self, sound):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("sound_playuntildone", inputs={"SOUND_MENU":[1,name2]}, name=name1)
        self.__add_block("sound_sounds_menu", fields={"SOUND_MENU":[sound, None]}, parent=name1, name=name2)

    def start_sound(self, sound):
        name1 = self.__random_name()
        name2 = self.__random_name()
        self.__add_block("sound_play", inputs={"SOUND_MENU":[1, name2]}, name=name1)
        self.__add_block("sound_sounds_menu", fields={"SOUND_MENU":[name1, None]}, name=name2, parent=name1)

    def stop_all_sounds(self):
        self.__add_block("sound_stopallsounds")

    def change_sound_effect_by(self, effect:str, amount:int):
        self.__add_block("sound_changeeffectby", inputs={"VALUE":[1,[4,f'{amount}']]}, fields={"EFFECT":[effect, None]})

    def set_sound_effect_to(self, effect:str, value:int):
        self.__add_block("sound_seteffectto", inputs={"VALUE":[1,[4,f'{value}']]}, fields={"EFFECT":[effect, None]})

    def clear_sound_effects(self):
        self.__add_block("sound_cleareffects")

    def change_volume_by(self, amount:int):
        self.__add_block("sound_changevolumeby", inputs={"VOLUME":[1,[4,f'{amount}']]})

    def set_volume_to(self, volume:int):
        self.__add_block("sound_setvolumeto", inputs={"VOLUME":[1,[4,f'{volume}']]})

### ### ### ### Events

    def when_flag_clicked(self, func):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whenflagclicked", name=_name)
        self.__parent = _name
        func()
        self.__parent = None

    def when_key_pressed(self, func, key:str):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whenkeypressed", name=_name, fields={"KEY_OPTION":[str(key).lower(), None]})
        self.__parent = _name
        func()
        self.__parent = None

    def when_this_sprite_clicked(self, func):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whenthisspriteclicked", name=_name)
        self.__parent = _name
        func()
        self.__parent = None

    def when_backdrop_switches_to(self, func, backdrop:str):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whenbackdropswitchesto", name=_name)
        self.__parent = _name
        func()
        self.__parent = None

    def when_greater_then(self, func, thing:str, value:int):
        if self.__parent:
            raise SyntaxError("Event blocks must be top-level blocks and cannot be nested inside other event blocks.")

        _name = self.__random_name()

        self.__add_block("event_whengreaterthan", inputs={"VALUE":[1,[4,f'{value}']]}, fields={"WHENGREATHERTHANMENU":[str(thing).upper()]}, name=_name)
        self.__parent = _name
        func()
        self.__parent = None

    # not all event blocks are programmed yet. but any help would be really appreciated