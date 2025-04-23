class MotionBlocks:
    def move(self, steps: float):
        pass

    def turn(self, degrees: float): # clockwise
        pass

    def go_to(self, position):
        pass

    def glide_to(self, seconds: float, position):
        pass

    def point_in_direction(self, degrees: int): #degrees
        pass

    def point_towards(self, thing): # position
        pass

    def change_x_by(self, amount: int):
        pass

    def set_x_to(self, amount: int):
        pass

    def change_y_by(self, amount: int):
        pass

    def set_y_to(self, amount: int):
        pass

    def if_on_edge_bounce(self):
        pass

    def set_rotation_style(self, style):
        pass


class LooksBlocks:
    def say(self, text: str, seconds: float = None):
        pass

    def think(self, text: str, seconds: float = None):
        pass

    def switch_costume_to(self, costume):
        pass

    def next_costume(self):
        pass

    def switch_backdrop_to(self, backdrop: str, wait: bool = False):
        pass

    def next_backdrop(self):
        pass

    def change_size_by(self, amount: int):
        pass

    def set_size_to(self, amount: int):
        pass

    def change_effect_by(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        pass

    def set_effect_to(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(
                f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        pass

    def clear_graphic_effects(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass

    def go_to_layer(self, layer, amount: int = None):
        pass

class SoundBlocks:
    def play_sound(self, sound, until_done: bool = False):
        pass

    def stop_all_sounds(self):
        pass

    def change_effect_by(self, effect, amount: float):
        pass

    def set_effect_to(self, effect, amount: float):
        pass

    def clear_all_effects(self):
        pass
        
    def change_volume(self):
        pass

    def set_volume(self):
        pass

class EventBlocks:
    def when_green_flag_clicked(self, func):
        def wrapper():
            pass

    def when_key_pressed(self, func, key):
        def wrapper():
            pass

    def when_this_sprite_clicked(self, func):
        def wrapper():
            pass

    def when_backdrop_switches_to(self, func, backdrop):
        def wrapper():
            pass

    def when_x_is_bigger_then_y(self, func, first, second):
        def wrapper():
            pass

    def when_i_recive(self, func, message):
        def wrapper():
            pass

    def broudcast(self, message, wait: bool = False):
        pass

class ControlBlocks:
    #finnish when i know what to do
    pass
    

# Backdrop
class BackdropLooksBlocks:
    def switch_backdrop_to(self, backdrop: str, wait: bool = False):
        pass

    def next_backdrop(self):
        pass

    def change_effect_by(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        pass

    def set_effect_to(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(
                f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        pass

    def clear_graphic_effects(self):
        pass
