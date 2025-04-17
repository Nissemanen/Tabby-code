from re import match
import pygame
import os
from PIL import Image

f = "."
_w = 480
_h = 360


def setDataFolder(folder: str):
    global f
    f = folder


def play(name: str):
    dataDir = os.path.join(f, "data")
    if not os.path.exists(dataDir):
        raise FileNotFoundError(f'Missing required "data" folder in "{os.path.join(f, "data")}". Please create it before running the game again.')

    _requiredList = ["backdrops", "sounds", "sprites"]
    _errors = []

    for folder in _requiredList:
        folder_path = os.path.join(dataDir, folder)
        if not os.path.isdir(folder_path):
            _errors.append(folder)


    if _errors:
        raise FileNotFoundError(f"Missing required folder(s): {', '.join(_errors)}")

    pygame.init()

    backdropsDir = os.path.join(dataDir, "backdrops")
    soundsDir = os.path.join(dataDir, "sounds")
    spritesDir = os.path.join(dataDir, "sprites")

    for folder in os.listdir(dataDir):
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
                                pass
                            else:
                                pygame.quit()
                                raise ValueError(f'"{image}" is a "{_tail}" type file, only ".png" and ".svg" type files are usable files')


                case "sounds":
                    for sound in os.listdir(os.path.join(dataDir, "sounds")):
                        _name, _tail = os.path.splitext(sound)
                        if _tail == ".wav":
                            pass
                        else:
                            raise ValueError(f'"{sound}" is a "{_tail}" type file, only ".wav" type files are usable files')

                case "sprites":
                    for sprite in os.listdir(os.path.join(dataDir, "sprites")):
                        pass

    screen = pygame.display.set_mode((_w, _h))
    clock = pygame.time.Clock()
    pygame.display.set_caption(name)
    pygame.display.set_icon(pygame.image.load("scratch_logo.png"))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


if __name__ == "__main__":
    play("scratch")

pygame.quit()
