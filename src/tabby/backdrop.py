import json
import os
from src.tabby import json_project

__all__ = [
    "switch_backdrop_to", "next_backdrop", "change_graphic_effect_by", "clear_all_graphic_effects", "play_sound",
    "stop_all_sounds", "change_sound_effect_by", "set_sound_effect_to", "clear_all_sound_effects", "change_volume",
    "set_volume", "when_green_flag_clicked", "when_key_pressed", "when_this_sprite_clicked", "when_backdrop_switches_to",
    "when_x_is_bigger_then_y", "when_i_receive", "broadcast"
]

_data = json_project["targets"][0]

#Looks blocks
backdrop_number = _data["currentCostume"]

def switch_backdrop_to(backdrop: str, wait: bool = False):
    raise NotImplementedError("This method is not available.")

def next_backdrop():
    raise NotImplementedError("This method is not available.")
    
def change_graphic_effect_by(effect, amount: float):
    if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
        raise ValueError(f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
    raise NotImplementedError("This method is not available.")

def set_graphic_effect_to(effect, amount: float):
    if effect not in ["color", "fisheye", "whirl", "pixelate", "mosaic", "brightness", "ghost"]:
        raise ValueError(
            f'Invalid value for "effect". Expected "color", "fisheye", "whirl", "pixelate", "mosaic", "brightness" or "ghost"')
    raise NotImplementedError("This method is not available.")

def clear_all_graphic_effects():
    raise NotImplementedError("This method is not available.")

#Sound blocks
volume = None

def play_sound(sound, until_done: bool = False):
        raise NotImplementedError("This method is not available.")

def stop_all_sounds():
    raise NotImplementedError("This method is not available.")

def change_sound_effect_by(effect, amount: float):
    raise NotImplementedError("This method is not available.")

def set_sound_effect_to(effect, amount: float):
    raise NotImplementedError("This method is not available.")

def clear_all_sound_effects():
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

def when_i_receive(func, message):
    def wrapper():
        raise NotImplementedError("This method is not available.")

def broadcast(message, wait: bool = False):
    raise NotImplementedError("This method is not available.")


if __name__ == "__main__":
    pass
