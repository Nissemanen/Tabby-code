import json

f = '{"targets":[{"isStage":true,"name":"Stage","variables":{"`jEk@4|i[#Fk?(8x)AV.-my variable":["my variable",0]},"lists":{},"broadcasts":{},"blocks":{},"comments":{},"currentCostume":0,"costumes":[{"name":"backdrop1","dataFormat":"svg","assetId":"cd21514d0531fdffb22204e0ec5ed84a","md5ext":"cd21514d0531fdffb22204e0ec5ed84a.svg","rotationCenterX":240,"rotationCenterY":180}],"sounds":[{"name":"pop","assetId":"83a9787d4cb6f3b7632b4ddfebf74367","dataFormat":"wav","format":"","rate":48000,"sampleCount":1123,"md5ext":"83a9787d4cb6f3b7632b4ddfebf74367.wav"}],"volume":100,"layerOrder":0,"tempo":60,"videoTransparency":50,"videoState":"on","textToSpeechLanguage":null},{"isStage":false,"name":"Sprite1","variables":{},"lists":{},"broadcasts":{},"blocks":{"9g:oz{4k6X[b$V:?endz":{"opcode":"event_whenflagclicked","next":"=o!bJ3{Z8|cDg-*uS(k[","parent":null,"inputs":{},"fields":{},"shadow":false,"topLevel":true,"x":529,"y":308},"=o!bJ3{Z8|cDg-*uS(k[":{"opcode":"control_repeat","next":null,"parent":"9g:oz{4k6X[b$V:?endz","inputs":{"TIMES":[1,[6,"10"]],"SUBSTACK":[2,"5-?x3qJ^V:05-O[LcVPx"]},"fields":{},"shadow":false,"topLevel":false},"5-?x3qJ^V:05-O[LcVPx":{"opcode":"motion_movesteps","next":null,"parent":"=o!bJ3{Z8|cDg-*uS(k[","inputs":{"STEPS":[1,[4,"10"]]},"fields":{},"shadow":false,"topLevel":false}},"comments":{},"currentCostume":0,"costumes":[{"name":"costume1","bitmapResolution":1,"dataFormat":"svg","assetId":"bcf454acf82e4504149f7ffe07081dbc","md5ext":"bcf454acf82e4504149f7ffe07081dbc.svg","rotationCenterX":48,"rotationCenterY":50},{"name":"costume2","bitmapResolution":1,"dataFormat":"svg","assetId":"0fb9be3e8397c983338cb71dc84d0b25","md5ext":"0fb9be3e8397c983338cb71dc84d0b25.svg","rotationCenterX":46,"rotationCenterY":53}],"sounds":[{"name":"Meow","assetId":"83c36d806dc92327b9e7049a565c6bff","dataFormat":"wav","format":"","rate":48000,"sampleCount":40681,"md5ext":"83c36d806dc92327b9e7049a565c6bff.wav"}],"volume":100,"layerOrder":1,"visible":true,"x":0,"y":0,"size":100,"direction":90,"draggable":false,"rotationStyle":"all around"}],"monitors":[],"extensions":[],"meta":{"semver":"3.0.0","vm":"11.0.0","agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0"}}'

jsonfile = json.loads(f)

class testclass:
    def __init__(self, name, position: (int, int)):
        self.name = name
        self.testjson = {"targets":[{"isStage": True, "name": "stage", "x": position[0], "y": position[1]}, {"isStage": False, "name": self.name}]}


test = testclass("sprite", (0, 43))
print(test.testjson)

testjson = {"targets": [{"isStage": True, "name": "mark"}]}

testjson["targets"] += [{"isStage": False, "name": "david"}]
testjson["targets"] += [{"isStage": False, "name": "hally"}]

#print(json.dumps(testjson, indent=2))

print(json.dumps(jsonfile, indent=4))