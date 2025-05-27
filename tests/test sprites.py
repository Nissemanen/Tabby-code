from src import tabby

mySprite = tabby.Sprite("mySprite")
sprite2 = tabby.Sprite("sprite2")

@mySprite.when_flag_clicked
def when_green_flag():
    mySprite.move(5)
    mySprite.turn_right(-90)
    mySprite.point(35)
    mySprite.go_to(1)



tabby.packager.print_json_output_to_terminal(True)