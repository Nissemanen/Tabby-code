from tabby.blocks import _MotionBlocks

class Sprite(_MotionBlocks):
    def __init__(self, name: str, position: (int, int) = (0, 0), show: bool = True, size: int = 100, rotation: int = 90, rotation_style: str = "All_Around"):
        self.position = position
        self.size = size
        self.show = show
        self.rotation = rotation
        self.rotation_style = rotation_style

