class _MotionBlocks:
    def move(self, steps: float):
        pass

    def turn(self, degrees: float): # clockwise
        pass

    def go_to(self, position: (int, int)):
        pass

    def glide_to(self, seconds: float, position: (int, int)):
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


class _LooksBlocks:
    def switch_backdrop_to(self, backdrop: str):
        pass

    def switch_backdrop_to_and_wait(self, backdrop: str):
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


# Backdrop
class _BackdropLooksBlocks:
    def switch_backdrop_to(self, backdrop: str):
        pass

    def switch_backdrop_to_and_wait(self, backdrop: str):
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