from src import tabby

mySprite = tabby.Sprite("mySprite")

@mySprite.when_flag_clicked
def when_green_flag():
    mySprite.move(5)
    mySprite.turn_right(-90)
    mySprite.point(50)
    mySprite.point()



tabby.packager.print_json_output_to_terminal(True)