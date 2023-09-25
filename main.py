import json

class Game:
    def __init__(self, opp, me = "Joe"):
        self.opp = opp
        self.score = [0,0]
        self.rallies = []

    def addRally(self, rally):
        self.rallies.append(rally)
        if rally.winnerIsMe:
            self.score[0] += 1
        else:
            self.score[1] += 1

class Rally:
    def __init__(self, serverIsMe, winnerIsMe):
        self.serverIsMe = serverIsMe
        self.winnerIsMe = winnerIsMe
        self.shots = []

    def addShot(self, shot):
        self.shots.append(shot)

class Shot:
    def __init__(self, type, quality, isOut = False, isFault = False):
        self.type = type
        self.quality = quality #number value 1-5?
        self.isOut = isOut
        self.isFault = isFault

game1 = Game("grace")
for i in range(10):
    x = Rally(True, True)
    game1.addRally(x)
    for s in range(4):
        x.addShot(Shot("Slice", 4))
    
class GameEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
        

y = json.dumps(game1, cls=GameEncoder, indent=4)

# The result is a JSON string
print(y)