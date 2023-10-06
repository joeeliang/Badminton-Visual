import json
import random

shotTypes = ["serve", "clear", "lift", "drop", "net", "smash", "drive"]

class Game:
    def __init__(self, opp, me = "Joe"):
        self.opp = opp
        self.me = me
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
    def __init__(self, type, quality, isMyShot, isOut = False, isFault = False):
        self.type = type
        self.isMyShot = isMyShot
        self.quality = quality #number value 1-5?
        self.isOut = isOut
        self.isFault = isFault

def generateGame():
    game = Game("grace")
    for i in range(10):
        isMyShot = True
        x = Rally(isMyShot, True)
        isMyShot = not isMyShot
        game.addRally(x)
        for s in range(random.randint(3,7)):
            x.addShot(Shot(shotTypes[random.randint(1,len(shotTypes)-1)], random.randint(0,5), isMyShot))
            isMyShot = not isMyShot
        endRally = random.choice(["out", "fault", "winner"])
        if endRally == "out":
            x.addShot(Shot(shotTypes[random.randint(1,len(shotTypes)-1)], random.randint(0,5), isMyShot, isOut=True))
        elif endRally == "fault":
            x.addShot(Shot(shotTypes[random.randint(1,len(shotTypes)-1)], random.randint(0,5), isMyShot, isFault=True))
        else:
            x.addShot(Shot(shotTypes[random.randint(1,len(shotTypes)-1)], random.randint(0,5), isMyShot))

        print("Rally added")
    return game
        

class GameEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

y = json.dumps(generateGame(), cls=GameEncoder, indent=4)

# The result is a JSON string
print(y)