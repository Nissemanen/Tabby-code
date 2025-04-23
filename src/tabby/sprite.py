from src.tabby.blocks import MotionBlocks
import os

__all__ = ["Sprite"]
_final_path = os.path.join(os.path.dirname(__file__), "package\\_final_product.json")

class Sprite(MotionBlocks, LooksBlocks, SoundBlocks, EventBlocks, ControlBlocks):
    position = (0, 0)
    size = 100
    show = True
    rotation = 90
    rotation_style = "All_Around"
    
    def __init__(self, name: str, position: (int, int) = (0, 0), show: bool = True, size: int = 100, rotation: int = 90, rotation_style: str = "All_Around"):
        self.position = position
        self.size = size
        self.show = show
        self.rotation = rotation
        self.rotation_style = rotation_style
        
        

    
