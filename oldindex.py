from ctypes import string_at
import random
import csv
from time import sleep
import os

targetguide = open('targetguide.csv')
targetScore = []
targetTarget = []
targetMult = []
playerguide = open('playerlist.csv')
playerlist = []
playerskill = []

targetguide.readline()
playerguide.readline()

savePath = 'logs'

if not os.path.exists(savePath):
    os.makedirs(savePath)

for a, b, c in csv.reader(targetguide, delimiter=","):
    targetScore.append(int(a))
    targetTarget.append(int(b))
    targetMult.append(int(c))

for a, b in csv.reader(playerguide, delimiter=","):
    playerlist.append(a)
    playerskill.append(int(b))

scores = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]


singlegame = input("Single Game? y/n - ")
doublestart = input("Start on Doubles? y/n - ")
watch = input("Watch? y/n - ")

class Target:
    def __init__(self):
        self.target = score.target*score.mult
        if score.target == 50:
            self.target = 50
            self.left = 25
            self.right = 25
            self.high = 25
            self.rh = random.randint(1, 20)
            self.lh = random.randint(1, 20)
            self.low = random.randint(1, 20)
            self.rl = random.randint(1, 20)
            self.ll = random.randint(1, 20)
        elif score.target == 25:
            self.target = 25
            self.left = 50
            self.right = random.randint(1, 20)
            self.high = random.randint(1, 20)
            self.rh = random.randint(1, 20)
            self.lh = random.randint(1, 20)
            self.low = random.randint(1, 20)
            self.rl = random.randint(1, 20)
            self.ll = random.randint(1, 20)
        elif score.target == 5:
            self.right = 20*score.mult
            self.left = (scores[scores.index(score.target)-1])*score.mult
        else:
            self.right = (scores[scores.index(score.target)+1])*score.mult
            self.left = (scores[scores.index(score.target)-1])*score.mult
        if score.mult == 3:
            self.high = score.target
            self.low = score.target
            self.rh = self.right//score.mult
            self.lh = self.left//score.mult
            self.rl = self.right//score.mult
            self.ll = self.left//score.mult
        elif score.mult == 2:
            self.high = 0
            self.rh = 0
            self.lh = 0
            self.low = score.target
            self.rl = self.right//score.mult
            self.ll = self.left//score.mult
        elif score.target == 50 or score.target == 25:
            self.target = self.target
        else:
            self.high = score.target
            self.low = score.target
            self.rh = self.right
            self.rl = self.right
            self.lh = self.left
            self.ll = self.left

class Player:
    def __init__(self, name, playerskill):
        if playerskill == 0:
            self.skill = [0,30,44,56,66,71,79,83,92,101]
        if playerskill == 1:
            self.skill = [0,33,45,64,70,75,80,85,94,101]
        if playerskill == 2:
            self.skill = [0,35,48,68,73,77,83,88,94,101]
        if playerskill == 3:
            self.skill = [0,37,50,71,76,81,86,91,96,101]
        if playerskill == 4:
            self.skill = [0,39,52,73,77,84,89,94,97,101]
        if playerskill == 5:
            self.skill = [0,40,55,75,80,85,90,94,97,101]
        if playerskill == 6:
            self.skill = [0,41,58,77,80,85,89,94,97,101]
        if playerskill == 7:
            self.skill = [0,43,61,80,84,87,90,94,97,101]
        if playerskill == 8:
            self.skill = [0,45,63,82,86,89,92,95,97,101]
        if playerskill == 9:
            self.skill = [0,48,65,84,88,91,94,96,98,101]
        if playerskill == 10:
            self.skill = [0,51,71,91,93,95,97,98,99,101]
        self.name = name
        self.score = 501
        self.throw = 0
        self.set = 0
        self.leg = 0

def makeTarget():
    if score.atOche == 1:
        y = p1.score-score.visit
        x = targetScore.index(y)
        score.target = targetTarget[x]
        score.mult = targetMult[x]
    elif score.atOche == 2:
        y = p2.score-score.visit
        x = targetScore.index(y)
        score.target = targetTarget[x]
        score.mult = targetMult[x]
    if y == 501 and doublestart == "y":
        aim.target = 40
        aim.left = 0
        aim.right = 0
        aim.high = 0
        aim.rh = 0
        aim.lh = 0
        aim.low = 0
        aim.rl = 0
        aim.ll = 0
    else:
        aim.target = score.target*score.mult
        if score.target == 50:
            aim.target = 50
            aim.left = 25
            aim.right = 25
            aim.high = 25
            aim.rh = random.randint(1, 20)
            aim.lh = random.randint(1, 20)
            aim.low = random.randint(1, 20)
            aim.rl = random.randint(1, 20)
            aim.ll = random.randint(1, 20)
        elif score.target == 25:
            aim.target = 25
            aim.left = 50
            aim.right = random.randint(1, 20)
            aim.high = random.randint(1, 20)
            aim.rh = random.randint(1, 20)
            aim.lh = random.randint(1, 20)
            aim.low = random.randint(1, 20)
            aim.rl = random.randint(1, 20)
            aim.ll = random.randint(1, 20)
        elif score.target == 5:
            aim.right = 20*score.mult
            aim.left = (scores[scores.index(score.target)-1])*score.mult
        else:
            aim.right = (scores[scores.index(score.target)+1])*score.mult
            aim.left = (scores[scores.index(score.target)-1])*score.mult
        if score.mult == 3:
            aim.high = score.target
            aim.low = score.target
            aim.rh = aim.right//score.mult
            aim.lh = aim.left//score.mult
            aim.rl = aim.right//score.mult
            aim.ll = aim.left//score.mult
        elif score.mult == 2:
            aim.high = 0
            aim.rh = 0
            aim.lh = 0
            aim.low = score.target
            aim.rl = aim.right//score.mult
            aim.ll = aim.left//score.mult
        elif score.target == 50 or score.target == 25:
            aim.target = aim.target
        else:
            aim.high = score.target
            aim.low = score.target
            aim.rh = aim.right
            aim.rl = aim.right
            aim.lh = aim.left
            aim.ll = aim.left


if singlegame == "y":
    player1 = input("Player 1 name - ")
    player2 = input("Player 2 name - ")
    fileName = f"{player1} v {player2}.txt"
    fullName = os.path.join(savePath, fileName)
    print(fullName)
    f = open(fullName, "a")
elif singlegame == "n":
    playerlineup = open("playerlineup.txt", "r")
    players = playerlineup.read()
    playerlines = players.splitlines()
    playerlineup.close
    roundmatches = (len(playerlines)/2)
    gamesplayed = 0
    playerdata = 0
    player1 = playerlines[playerdata]
    player2 = playerlines[playerdata+1]
    fileName = f'{input("Name of file = ")}.txt'
    fullName = os.path.join(savePath, fileName)
    f = open(fullName, "a")
    results = []

if player1 in playerlist:
    player1skill = playerskill[playerlist.index(player1)]
else:
    player1skill = 0
if player2 in playerlist:
    player2skill = playerskill[playerlist.index(player2)]
else:
    player2skill = 0

p1 = Player(player1, player1skill)
p2 = Player(player2, player2skill)
f.write(f'{p1.name}, {player1skill}, {p2.name}, {player2skill}\n')

condition = input("legs or sets? - ")
win = int(input("How many to win? - "))
f.write(f'{win} {condition} to win.\n')

class Data:
    def __init__(self, starting):
        self.visit = starting
        self.throw = starting
        self.atOche = 1
        self.target = 20
        self.mult = 3

score = Data(0)

aim = Target()

def throwpoints():
    rating = random.randint(0,100)
    makeTarget()
    if score.atOche == 1:
        if rating in range(p1.skill[0], p1.skill[1]):
            score.throw = aim.target
        elif rating in range(p1.skill[1], p1.skill[2]):
            score.throw = aim.high
        elif rating in range(p1.skill[2], p1.skill[3]):
            score.throw = aim.low
        elif rating in range(p1.skill[3], p1.skill[4]):
            score.throw = aim.right
        elif rating in range(p1.skill[4], p1.skill[5]):
            score.throw = aim.left
        elif rating in range(p1.skill[5], p1.skill[6]):
            score.throw = aim.lh
        elif rating in range(p1.skill[6], p1.skill[7]):
            score.throw = aim.ll
        elif rating in range(p1.skill[7], p1.skill[8]):
            score.throw = aim.rh
        elif rating in range(p1.skill[8], p1.skill[9]):
            score.throw = aim.rl
        p1.throw += 1
        score.visit += score.throw
        f.write(f'{p1.name} scores {score.throw}, {p1.score-score.visit} remains.\n')
    elif score.atOche == 2:
        if rating in range(p2.skill[0], p2.skill[1]):
            score.throw = aim.target
        elif rating in range(p2.skill[1], p2.skill[2]):
            score.throw = aim.high
        elif rating in range(p2.skill[2], p2.skill[3]):
            score.throw = aim.low
        elif rating in range(p2.skill[3], p2.skill[4]):
            score.throw = aim.right
        elif rating in range(p2.skill[4], p2.skill[5]):
            score.throw = aim.left
        elif rating in range(p2.skill[5], p2.skill[6]):
            score.throw = aim.lh
        elif rating in range(p2.skill[6], p2.skill[7]):
            score.throw = aim.ll
        elif rating in range(p2.skill[7], p2.skill[8]):
            score.throw = aim.rh
        elif rating in range(p2.skill[8], p2.skill[9]):
            score.throw = aim.rl
        p2.throw += 1
        score.visit += score.throw
        f.write(f'{p2.name} scores {score.throw}, {p2.score-score.visit} remains.\n')

def legMatch():
    while p1.leg != win or p2.leg != win:
        throwpoints()
        if score.atOche == 1:
            if p1.score-score.visit == 1 or p1.score-score.visit < 0:
                f.write(f'{p1.name} throws for {score.visit}, Bust!\n')
                if watch == "y":
                    print(f'{p1.name} throws for {score.visit}, Bust!\n')
                score.atOche = 2
                score.visit = 0
                p1.throw = 0
            elif p1.score-score.visit == 0:
                f.write(f'{p1.name} throws for {score.visit}, they win the leg!\n')
                if watch == "y":
                    print(f'{p1.name} throws for {score.visit}, they win the leg!\n')
                score.visit = 0
                p1.throw = 0
                p1.leg += 1
                if ((p1.leg + p2.leg) % 2) == 0:
                    score.atOche = 1
                else: 
                    score.atOche = 2
                p1.score = 501
                p2.score = 501
                p1.throw = 0
                p2.throw = 0
                f.write(f"{p1.name} {p1.leg}, {p2.name} {p2.leg}\n\n")
                if watch == "y":
                    print(f"{p1.name} {p1.leg}, {p2.name} {p2.leg}\n\n")
                if p1.leg == win:
                    break
            elif p1.throw == 3:
                p1.score -= score.visit
                f.write(f'{p1.name} throws for {score.visit}, {p1.score} remains.\n')
                if watch == "y":
                    print (f'{p1.name} throws for {score.visit}, {p1.score} remains.\n')
                p1.throw = 0
                score.visit = 0
                score.atOche = 2
        elif score.atOche == 2:
            if p2.score-score.visit == 1 or p2.score-score.visit < 0:
                f.write(f'{p2.name} throws for {score.visit}, Bust!\n')
                if watch == "y":
                    print(f'{p2.name} throws for {score.visit}, Bust!\n')
                score.atOche = 1
                score.visit = 0
                p2.throw = 0
            elif p2.score-score.visit == 0:
                f.write(f'{p2.name} throws for {score.visit}, they win the leg!\n')
                if watch == "y":
                    print(f'{p2.name} throws for {score.visit}, they win the leg!\n')
                score.visit = 0
                p2.throw = 0
                p2.leg += 1
                if ((p1.leg + p2.leg) % 2) == 0:
                    score.atOche = 1
                else: 
                    score.atOche = 2
                p1.score = 501
                p2.score = 501
                p1.throw = 0
                p2.throw = 0
                f.write(f"{p1.name} {p1.leg}, {p2.name} {p2.leg}\n\n")
                if watch == "y":
                    print(f"{p1.name} {p1.leg}, {p2.name} {p2.leg}\n\n")
                if p2.leg == win:
                    break
            elif p2.throw == 3:
                p2.score -= score.visit
                f.write(f'{p2.name} throws for {score.visit}, {p2.score} remains.\n')
                if watch == "y":
                    print(f'{p2.name} throws for {score.visit}, {p2.score} remains.\n')
                p2.throw = 0
                score.visit = 0
                score.atOche = 1
        if watch == "y":
            sleep(0.25)
        else:
            sleep(0.05)
            
def setMatch():
    while p1.set != win or p2.set != win:
        throwpoints()
        if score.atOche == 1:
            if p1.score-score.visit == 1 or p1.score-score.visit < 0:
                f.write (f'{p1.name} throws for {score.visit}, Bust!\n')
                if watch == "y":
                    print(f'{p1.name} throws for {score.visit}, Bust!\n')
                score.atOche = 2
                score.visit = 0
                p1.throw = 0
            elif p1.score-score.visit == 0:
                f.write(f'{p1.name} throws for {score.visit}, they win the leg!\n')
                if watch == "y":
                    print(f'{p1.name} throws for {score.visit}, they win the leg!\n')
                score.visit = 0
                p1.throw = 0
                p1.leg += 1
                if p1.leg == 3:
                    p1.leg = 0
                    p2.leg = 0
                    p1.set += 1
                    f.write(f'{p1.name} wins the set!\n')
                    if watch == "y":
                        print(f'{p1.name} wins the set!\n')
                    if ((p1.set + p2.set) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                else:
                    if ((p1.leg + p2.leg) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                p1.score = 501
                p2.score = 501
                p1.throw = 0
                p2.throw = 0
                f.write(f"{p1.name} {p1.set}-{p1.leg}, {p2.name} {p2.set}-{p2.leg}\n\n")
                if watch == "y":
                    print(f"{p1.name} {p1.set}-{p1.leg}, {p2.name} {p2.set}-{p2.leg}\n\n")
                if p1.set == win:
                    break
            elif p1.throw == 3:
                p1.score -= score.visit
                f.write(f'{p1.name} throws for {score.visit}, {p1.score} remains.\n')
                if watch == "y":
                    print(f'{p1.name} throws for {score.visit}, {p1.score} remains.\n')
                p1.throw = 0
                score.visit = 0
                score.atOche = 2
        elif score.atOche == 2:
            if p2.score-score.visit == 1 or p2.score-score.visit < 0:
                f.write (f'{p2.name} throws for {score.visit}, Bust!\n')
                if watch == "y":
                    print(f'{p2.name} throws for {score.visit}, Bust!\n')
                score.atOche = 1
                score.visit = 0
                p2.throw = 0
            elif p2.score-score.visit == 0:
                f.write(f'{p2.name} throws for {score.visit}, they win the leg!\n')
                if watch == "y":
                    print(f'{p2.name} throws for {score.visit}, they win the leg!\n')
                score.visit = 0
                p2.throw = 0
                p2.leg += 1
                if p2.leg == 3:
                    p1.leg = 0
                    p2.leg = 0
                    p2.set += 1
                    f.write(f'{p2.name} wins the set!\n')
                    if watch == "y":
                        print(f'{p2.name} wins the set!\n')
                    if ((p1.set + p2.set) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                else:
                    if ((p1.leg + p2.leg) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                p1.score = 501
                p2.score = 501
                p1.throw = 0
                p2.throw = 0
                f.write(f"{p1.name} {p1.set}-{p1.leg}, {p2.name} {p2.set}-{p2.leg}\n\n")
                if watch == "y":
                    print(f"{p1.name} {p1.set}-{p1.leg}, {p2.name} {p2.set}-{p2.leg}\n\n")
                if p2.set == win:
                    break
            elif p2.throw == 3:
                p2.score -= score.visit
                f.write(f'{p2.name} throws for {score.visit}, {p2.score} remains.\n')
                if watch == "y":
                    print(f'{p2.name} throws for {score.visit}, {p2.score} remains.\n')
                p2.throw = 0
                score.visit = 0
                score.atOche = 1
        if watch == "y":
            sleep(0.25)
        else:
            sleep(0.05)

if singlegame == "y":
    if condition == "legs":
        legMatch()
    elif condition == "sets":
        setMatch()
elif singlegame == "n":
    while gamesplayed < roundmatches:
        if condition == "legs":
            legMatch()
            results.append(f"{p1.name} {p1.leg}, {p2.name} {p2.leg}\n")
        elif condition == "sets":
            setMatch()
            results.append(f"{p1.name} {p1.set}-{p1.leg}, {p2.name} {p2.set}-{p2.leg}\n")
        gamesplayed += 1
        playerdata += 2
        if gamesplayed == roundmatches:
            break
        player1 = playerlines[playerdata]
        player2 = playerlines[playerdata+1]
        if player1 in playerlist:
            player1skill = playerskill[playerlist.index(player1)]
        else:
            player1skill = 0
        if player2 in playerlist:
            player2skill = playerskill[playerlist.index(player2)]
        else:
            player2skill = 0    
        p1 = Player(player1, player1skill)
        p2 = Player(player2, player2skill)
        f.write(f'{p1.name}, {player1skill}, {p2.name}, {player2skill}\n')

if singlegame == "n":
    for element in results:
        f.write(element)
        print(element)
f.close()
        
print("done")

#wrap as an exe