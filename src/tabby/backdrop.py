import json
import os

__all__ = ["switch_backdrop_to", "next_backdrop", "change_graphic_effect_by", "set_effect_to", "clear_graphic_effects", "play_sound", "stop_all_sounds", "change_sound_effect_by", "", "", "", ""]

with open(os.path.join(os.path.dirname(__file__), "packager\\_final_produt.json"), "r") as f_p_dir:
    
    pass

#Looks blocks
def switch_backdrop_to(backdrop: str, wait: bool = False):
    raise NotImplementedError("This method is not available.")

def next_backdrop():
    raise NotImplementedError("This method is not available.")
    
def change_graphic_effect_by(effect, amount: float):
    if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
        raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
    raise NotImplementedError("This method is not available.")

def set_effect_to(effect, amount: float):
    if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
        raise ValueError(
            f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
    raise NotImplementedError("This method is not available.")

def clear_graphic_effects():
    raise NotImplementedError("This method is not available.")

#Sound blocks
volume = 100

def play_sound(sound, until_done: bool = False):
        raise NotImplementedError("This method is not available.")

def stop_all_sounds():
    raise NotImplementedError("This method is not available.")

def change_sound_effect_by(effect, amount: float):
    raise NotImplementedError("This method is not available.")

def set_effect_to(effect, amount: float):
    raise NotImplementedError("This method is not available.")

def clear_all_effects():
    raise NotImplementedError("This method is not available.")
    
def change_volume():
    raise NotImplementedError("This method is not available.")

def set_volume():
    raise NotImplementedError("This method is not available.")

#Event blocks
def when_green_flag_clicked(func):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def when_key_pressed(func, key):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def when_this_sprite_clicked(func):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def when_backdrop_switches_to(func, backdrop):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def when_x_is_bigger_then_y(func, first, second):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def when_i_recive(func, message):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def broudcast(message, wait: bool = False):
    raise NotImplementedError("This method is not available.")
    


'''
class Backdrop():
    def __new__(cls):
        if cls._ is None:
            cls._ = super().__new__(cls)
        return cls._
    
    def __init__():
        pass



def start():
    for target in get_final_product()["targets"]:
        if target["isStage"]:
            raise TypeError(f'tried to make a backdrop when one is already made')
        else:
            raise Exception
'''


if __name__ == "__main__":
    pass
