from src import tabby

mySprite = tabby.Sprite("mySprite")

@mySprite.when_flag_clicked
def wgfc1():
    mySprite.move(5)



tabby.packager.print_json_output_to_terminal(True)