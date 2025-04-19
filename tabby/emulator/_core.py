import pygame
import os
from PIL import Image

#Variables
__all__ = ["run"]

assetsDir = os.path.join(os.path.dirname(__file__), "assets")
_w = 480
_h = 360
backdrops = {}
sounds = {}
sprites = {}


def run(name: str=None):
    if not os.path.exists(assetsDir):
        raise FileNotFoundError(f'Missing required "assets" folder in "{assetsDir}". Please create it before running the game again.')

    _requiredList = ["backdrops", "sounds", "sprites"]
    _errors = []

    for directory in _requiredList:
        directory_path = os.path.join(assetsDir, directory)
        if not os.path.isdir(directory_path):
            _errors.append(directory)


    if _errors:
        raise FileNotFoundError(f"Missing required folder(s): {', '.join(_errors)}")

    pygame.init()

    backdropsDir = os.path.join(assetsDir, "backdrops")
    soundsDir = os.path.join(assetsDir, "sounds")
    spritesDir = os.path.join(assetsDir, "sprites")

    for folder in os.listdir(assetsDir):
        if folder in _requiredList:
            match folder:
                case "backdrops":
                    if not os.listdir(backdropsDir):
                        _temp = Image.new("RGB", (_w, _h), color="White")
                        _temp.save(os.path.join(backdropsDir, "backdrop1.png"))
                        _temp.close()
                        print(f'Caution: "backdrops" directory doesnt have any images. Created a blank image in "{backdropsDir}"')

                    else:
                        for image in os.listdir(backdropsDir):
                            _name, _tail = os.path.splitext(image)
                            if _tail == ".svg" or _tail == ".png":
                                if Image.open(os.path.join(backdropsDir, image)).size == (480, 360):
                                    backdrops[_name] = pygame.image.load(os.path.join(backdropsDir, image))
                                    print(f'Info: image "{image}" was successfully loaded as a backdrop.')
                                else:
                                    print(f'Caution: image "{image}" was not successfully loaded as a backdrop due to it being the right ratio! only images with 480 w, 360 h aspect ratio are acceptable backdrops.')
                            else:
                                pygame.quit()
                                raise ValueError(f'"{image}" is a "{_tail}" type file, only ".png" and ".svg" type files are usable files')


                case "sounds":
                    for sound in os.listdir(os.path.join(assetsDir, "sounds")):
                        _name, _tail = os.path.splitext(sound)
                        if _tail == ".wav":
                            pass
                        else:
                            pygame.quit()
                            raise ValueError(f'"{sound}" is a "{_tail}" type file, only ".wav" type files are usable files')

                case "sprites":
                    for sprite in os.listdir(os.path.join(assetsDir, "sprites")):
                        _name, _tail = os.path.splitext(sprite)
                        if _tail == ".svg" or _tail == ".png":
                            if Image.open(os.path.join(backdropsDir, sprite)).size == (480, 360):
                                backdrops[_name] = pygame.image.load(os.path.join(backdropsDir, sprite))
                                print(f'Info: image "{sprite}" was successfully loaded as a sprite.')
                            else:
                                print(
                                    f'Caution: image "{sprite}" was not successfully loaded as a sprite due to it being the right ratio! only images with 480 w, 360 h aspect ratio are acceptable backdrops.')
                        else:
                            pygame.quit()
                            raise ValueError(
                                f'"{sprite}" is a "{_tail}" type file, only ".png" and ".svg" type files are usable files')

    screen = pygame.display.set_mode((_w, _h))
    clock = pygame.time.Clock()
    if name:
        pygame.display.set_caption(name)
    else:
        pygame.display.set_caption("scratch")
    pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(__file__), "scratch_logo.png")))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()



if __name__ == "__main__":
    run()
    pygame.quit()