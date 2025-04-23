class MotionBlocks:
    def move(self, steps: float):
        raise NotImplementedError("This method is not available.")

    def turn(self, degrees: float): # clockwise
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


class LooksBlocks:
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

    def change_effect_by(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        raise NotImplementedError("This method is not available.")

    def set_effect_to(self, effect, amount: float):
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

class SoundBlocks:
    def play_sound(self, sound, until_done: bool = False):
        raise NotImplementedError("This method is not available.")

    def stop_all_sounds(self):
        raise NotImplementedError("This method is not available.")

    def change_effect_by(self, effect, amount: float):
        raise NotImplementedError("This method is not available.")

    def set_effect_to(self, effect, amount: float):
        raise NotImplementedError("This method is not available.")

    def clear_all_effects(self):
        raise NotImplementedError("This method is not available.")
        
    def change_volume(self):
        raise NotImplementedError("This method is not available.")

    def set_volume(self):
        raise NotImplementedError("This method is not available.")

class EventBlocks:
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

class ControlBlocks:
    #finnish when i know what to do
    raise NotImplementedError("This method is not available.")
    

# Backdrop
class BackdropLooksBlocks:
    def switch_backdrop_to(self, backdrop: str, wait: bool = False):
        raise NotImplementedError("This method is not available.")

    def next_backdrop(self):
        raise NotImplementedError("This method is not available.")

    def change_effect_by(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        raise NotImplementedError("This method is not available.")

    def set_effect_to(self, effect, amount: float):
        if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
            raise ValueError(
                f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
        raise NotImplementedError("This method is not available.")

    def clear_graphic_effects(self):
        raise NotImplementedError("This method is not available.")
