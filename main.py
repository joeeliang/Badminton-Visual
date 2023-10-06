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
    def __init__(self, type, quality, isMyShot, isOut, isFault, startCoord, endCoord):
        self.type = type
        self.isMyShot = isMyShot
        self.quality = quality #number value 1-5?
        self.isOut = isOut
        self.isFault = isFault
        self.startCoord = startCoord
        self.endCoord = endCoord

def generateMidGameShot(isMyShot, lastShotEndCoord):
    if isMyShot:
        endCoord = [random.randint(670, 1340),random.randint(0, 610)]
    else:
        endCoord = [random.randint(0, 670),random.randint(0, 610)]
    return Shot(shotTypes[random.randint(1,len(shotTypes)-1)], random.randint(0,5), isMyShot, False, False, lastShotEndCoord, endCoord)

def generateGame():
    game = Game("grace")
    for i in range(1):
        isMyShot = True
        x = Rally(isMyShot, True)
        game.addRally(x)
        #service
        x.addShot(Shot("serve", random.randint(0,5), isMyShot, False, False, [300,305], [random.randint(670, 1340),random.randint(0, 610)]))
        for s in range(random.randint(5,7)):
            lastShotCoord = x.shots[s].endCoord
            x.addShot(generateMidGameShot(isMyShot, lastShotCoord))
            isMyShot = not isMyShot
        endRally = random.choice(["out", "fault", "winner"])
        if endRally == "out":
            x.shots[len(x.shots)-1].isOut = True
        elif endRally == "fault":
            x.shots[len(x.shots)-1].isFault = True
        print("Rally added")
    return game

class GameEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

y = json.dumps(generateGame(), cls=GameEncoder, indent=4)

# The result is a JSON string
print(y)