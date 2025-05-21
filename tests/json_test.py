"""
init_sprites = ["stage"]

def new_sprite(name):
    init_sprites.append(name)
    print(f'added {name} to "init_sprites". its the {len(init_sprites)} place')


new_sprite("mike")
new_sprite("daniel")
new_sprite("angela")
new_sprite("bob")


import json
import string
import random

f = '{"targets":[{"isStage":true,"name":"Stage","variables":{"`jEk@4|i[#Fk?(8x)AV.-my variable":["my variable",0]},"lists":{},"broadcasts":{},"blocks":{"M2J2drf[sx9j{Bdd-KhJ":{"opcode":"looks_changeeffectby","next":null,"parent":null,"inputs":{"CHANGE":[1,[4,"200"]]},"fields":{"EFFECT":["COLOR",null]},"shadow":false,"topLevel":true,"x":354,"y":505}},"comments":{},"currentCostume":0,"costumes":[{"name":"backdrop1","bitmapResolution":1,"dataFormat":"svg","assetId":"d4a82b4479d895ae2192c053cc309ef2","md5ext":"d4a82b4479d895ae2192c053cc309ef2.svg","rotationCenterX":156,"rotationCenterY":73}],"sounds":[{"name":"pop","assetId":"83a9787d4cb6f3b7632b4ddfebf74367","dataFormat":"wav","format":"","rate":48000,"sampleCount":1123,"md5ext":"83a9787d4cb6f3b7632b4ddfebf74367.wav"}],"volume":100,"layerOrder":0,"tempo":60,"videoTransparency":50,"videoState":"on","textToSpeechLanguage":null},{"isStage":false,"name":"Sprite1","variables":{},"lists":{},"broadcasts":{},"blocks":{"9g:oz{4k6X[b$V:?endz":{"opcode":"event_whenflagclicked","next":"=o!bJ3{Z8|cDg-*uS(k[","parent":null,"inputs":{},"fields":{},"shadow":false,"topLevel":true,"x":529,"y":308},"=o!bJ3{Z8|cDg-*uS(k[":{"opcode":"control_repeat","next":null,"parent":"9g:oz{4k6X[b$V:?endz","inputs":{"TIMES":[1,[6,"10"]],"SUBSTACK":[2,"5-?x3qJ^V:05-O[LcVPx"]},"fields":{},"shadow":false,"topLevel":false},"5-?x3qJ^V:05-O[LcVPx":{"opcode":"motion_movesteps","next":"8,A[c%9D;KSg0LSf[A6z","parent":"=o!bJ3{Z8|cDg-*uS(k[","inputs":{"STEPS":[1,[4,"10"]]},"fields":{},"shadow":false,"topLevel":false},"8,A[c%9D;KSg0LSf[A6z":{"opcode":"motion_turnleft","next":null,"parent":"5-?x3qJ^V:05-O[LcVPx","inputs":{"DEGREES":[1,[4,"18"]]},"fields":{},"shadow":false,"topLevel":false},"=hk2#zL6qXxRx!c6;d6k":{"opcode":"motion_pointindirection","next":null,"parent":null,"inputs":{"DIRECTION":[1,[8,"21.4555555555"]]},"fields":{},"shadow":false,"topLevel":true,"x":317,"y":566},"Wki:A.rb4N6qC/eE_[K!":{"opcode":"looks_sayforsecs","next":null,"parent":null,"inputs":{"MESSAGE":[1,[10,"Hello!"]],"SECS":[1,[4,"2"]]},"fields":{},"shadow":false,"topLevel":true,"x":341,"y":1195}},"comments":{},"currentCostume":0,"costumes":[{"name":"costume1","bitmapResolution":1,"dataFormat":"svg","assetId":"bcf454acf82e4504149f7ffe07081dbc","md5ext":"bcf454acf82e4504149f7ffe07081dbc.svg","rotationCenterX":48,"rotationCenterY":50},{"name":"costume2","bitmapResolution":1,"dataFormat":"svg","assetId":"0fb9be3e8397c983338cb71dc84d0b25","md5ext":"0fb9be3e8397c983338cb71dc84d0b25.svg","rotationCenterX":46,"rotationCenterY":53}],"sounds":[{"name":"Meow","assetId":"83c36d806dc92327b9e7049a565c6bff","dataFormat":"wav","format":"","rate":48000,"sampleCount":40681,"md5ext":"83c36d806dc92327b9e7049a565c6bff.wav"}],"volume":100,"layerOrder":1,"visible":true,"x":12.225401826548728,"y":-108.83444126426387,"size":36.24,"direction":-8.544444444500016,"draggable":false,"rotationStyle":"left-right"}],"monitors":[],"extensions":[],"meta":{"semver":"3.0.0","vm":"11.0.0","agent":"Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}}'

jsonfile = json.loads(f)

class testclass:
    def __init__(self, name, position: (int, int)):
        self.name = name
        self.testjson = {"targets":[{"isStage": True, "name": "stage", "x": position[0], "y": position[1]}, {"isStage": False, "name": self.name}]}


test = testclass("sprite", (0, 43))
#print(test.testjson)

testjson = {"targets": [{"isStage": True, "name": "mark"}]}

testjson["targets"] += [{"isStage": False, "name": "david"}]
testjson["targets"] += [{"isStage": False, "name": "hally"}]

sprites = []
secont= ["yes", "no"]

sprites.append("name")
sprites.append("ello")

if "yes" in sprites + secont:
    print(sprites)


print("event_whenflagcliked"[:5])
print("motion_movesteps"[:5])


def Sprite(cls) -> None:
    cls()

class Blocks:
    def __init__(self):
        self.__self = self
        print(f'{type(self).__name__} is the name')

    @classmethod
    def move(cls, steps):
        print("moved 10 steps")

    @classmethod
    def start(cls, func):
        print("Started!")
        func(cls)

@Sprite
class Sprite5(Blocks):
    @Blocks.start
    def start(self):
        self.move(10)



def myfunc(inp: tuple[int, int]):
    print(f'{inp[0]} and {inp[1]}')


myfunc((34,10))

#print(json.dumps(testjson, indent=2))
print(string.printable)
print(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'))
print(''.join(random.choices(''.join(c for c in (string.digits + string.ascii_letters + string.punctuation) if c not in '\\`"'), k=20)))
#print(json.dumps(jsonfile, indent=4))
"""


class Sprite:
    def __init__(self):
        print(f'code output from "{type(self).__name__}"')

    @classmethod
    def start(cls, func):
