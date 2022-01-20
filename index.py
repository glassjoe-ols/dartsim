import tkinter as tk
import os
from ctypes import string_at
import random
import csv
from time import sleep
import pyperclip
import sys

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

window = tk.Tk()
secondWindow = tk.Toplevel(window)
thirdWindow = tk.Toplevel(secondWindow)
watchWindow = tk.Toplevel(secondWindow)
thirdWindow.geometry("400x400")
secondWindow.withdraw()
thirdWindow.withdraw()
watchWindow.withdraw()

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

class rules():
    def __init__(self):
        self.format = "legs"
        self.doubles = "n"
        self.watch = "n"
        self.win = 6
        self.title = "darts"
        self.roundmatches = 0
        self.gamesplayed = 0
        self.f = ""
        self.results = []
        self.playerdata = 0
        self.playerlines = []
        self.player1 = ""
        self.player2 = ""
        self.player1skill = 0
        self.player2skill = 0
        self.p1 = Player("", 0)
        self.p2 = Player("", 0)
        self.p1name = []
        self.p2name = []
        self.labelnumbers = []
        self.p1score = []
        self.p2score = []
        self.p1scorelabels = []
        self.p2scorelabels = []
        self.p1namelabels = []
        self.p2namelabels = []
        self.logvar = ""



class newData():
    def __init__(self):
        self.filedata = ""

ruleset = rules()

#p1 = Player("", 0)
#p2 = Player("", 0)

def makeTarget():
    if score.atOche == 1:
        y = ruleset.p1.score-score.visit
        x = targetScore.index(y)
        score.target = targetTarget[x]
        score.mult = targetMult[x]
    elif score.atOche == 2:
        y = ruleset.p2.score-score.visit
        x = targetScore.index(y)
        score.target = targetTarget[x]
        score.mult = targetMult[x]
    if y == 501 and ruleset.doubles == "y":
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


nameVar = tk.StringVar()
formatVar = tk.StringVar()
doublesVar = tk.StringVar()
gameNumVar = tk.StringVar()
watchVar = tk.StringVar()
winVar = tk.IntVar(value=6)
playersVar = tk.StringVar()
playerlineup = "playerlineup.txt"
p1scores = "p1scores.txt"
p2scores = "p2scores.txt"
#logvar = tk.StringVar()
p1scorevar = tk.IntVar(value=501)
p2scorevar = tk.IntVar(value=501)
logvar = tk.StringVar()
p1namevar = tk.StringVar()
p2namevar = tk.StringVar()
p1legsvar = tk.IntVar(value=0)
p2legsvar = tk.IntVar(value=0)
p1setsvar = tk.IntVar(value=0)
p2setsvar = tk.IntVar(value=0)
    
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
        
scrollingCanvas = tk.Canvas(thirdWindow, borderwidth=0)
scrollingFrame = tk.Frame(thirdWindow)
vsb = tk.Scrollbar(thirdWindow, orient="vertical", command=scrollingCanvas.yview)
scrollingCanvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
scrollingCanvas.pack(side="left", fill="both", expand="true")
scrollingCanvas.create_window((4,4), window=scrollingFrame, anchor="nw")
scrollingFrame.bind("<Configure>", lambda event, canvas=scrollingCanvas: onFrameConfigure(scrollingCanvas))

def gamesetup1():
    print("gs1start")
    playerlineup = open("playerlineup.txt", "r")
    players = playerlineup.read()
    ruleset.playerlines = players.splitlines()
    playerlineup.close
    ruleset.roundmatches = (len(ruleset.playerlines)/2)
    ruleset.gamesplayed = 0
    ruleset.player1 = ruleset.playerlines[ruleset.playerdata]
    ruleset.player2 = ruleset.playerlines[ruleset.playerdata+1]
    ruleset.p1name.append(ruleset.playerlines[ruleset.playerdata])
    ruleset.p2name.append(ruleset.playerlines[ruleset.playerdata+1])
    ruleset.p1score.append(0)
    ruleset.p2score.append(0)
    fileName = f'{ruleset.title}.txt'
    fullName = os.path.join(savePath, fileName)
    ruleset.f = open(fullName, "a")
    if ruleset.player1 in playerlist:
        ruleset.player1skill = playerskill[playerlist.index(ruleset.player1)]
    else:
        ruleset.player1skill = 0
    if ruleset.player2 in playerlist:
        ruleset.player2skill = playerskill[playerlist.index(ruleset.player2)]
    else:
        ruleset.player2skill = 0
    ruleset.p1 = Player(ruleset.player1, ruleset.player1skill)
    #print(p1.name)    
    ruleset.p2 = Player(ruleset.player2, ruleset.player2skill)
    #print(p2.name)
    ruleset.f.write(f'{ruleset.p1.name}, {ruleset.player1skill}, {ruleset.p2.name}, {ruleset.player2skill}\n')
    ruleset.f.write(f'{ruleset.win} {ruleset.format} to win.\n')
    copyp1Button = tk.Button(scrollingFrame, text = "Copy", command=lambda: copyButton(1))
    copyp2Button = tk.Button(scrollingFrame, text = "Copy", command=lambda: copyButton(2))
    crashButton = tk.Button(scrollingFrame, text = "Restart Program", command=lambda:restartButton())
    copyp1Button.grid(row=0, column=1)
    copyp2Button.grid(row=0, column=2)
    crashButton.grid(row=0, column=3)
    thirdWindow.grab_set()
    thirdWindow.update()
    thirdWindow.lift()
    if ruleset.watch == "y":
        watchWindowInit()

def gamesetup2():
    print("gs2start")
    while ruleset.gamesplayed < ruleset.roundmatches:
        if ruleset.format == "legs":
            legMatch()
            ruleset.results.append(f"{ruleset.p1.name} {ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.leg}\n")
            ruleset.p1score[ruleset.gamesplayed] = ruleset.p1.leg
            ruleset.p2score[ruleset.gamesplayed] = ruleset.p2.leg
        elif ruleset.format == "sets":
            setMatch()
            ruleset.results.append(f"{ruleset.p1.name} {ruleset.p1.set}-{ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.set}-{ruleset.p2.leg}\n")
            ruleset.p1score[ruleset.gamesplayed] = ruleset.p1.set
            ruleset.p2score[ruleset.gamesplayed] = ruleset.p2.set
        createFinalLabel(ruleset.gamesplayed)
        vsb.pack(side="right", fill="y")
        scrollingCanvas.pack(side="left", fill="both", expand="true")
        scrollingCanvas.create_window((4,4), window=scrollingFrame, anchor="nw")
        scrollingFrame.bind("<Configure>", lambda event, canvas=scrollingCanvas: onFrameConfigure(scrollingCanvas))
        ruleset.gamesplayed += 1
        ruleset.playerdata += 2
        if ruleset.gamesplayed == ruleset.roundmatches:
            for element in ruleset.results:
                ruleset.f.write(element)
                #print(element)
            break
        player1 = ruleset.playerlines[ruleset.playerdata]
        player2 = ruleset.playerlines[ruleset.playerdata+1]
        ruleset.p1name.append(ruleset.playerlines[ruleset.playerdata])
        ruleset.p2name.append(ruleset.playerlines[ruleset.playerdata+1])
        ruleset.p1score.append(0)
        ruleset.p2score.append(0)
        if player1 in playerlist:
            player1skill = playerskill[playerlist.index(player1)]
        else:
            player1skill = 0
        if player2 in playerlist:
            player2skill = playerskill[playerlist.index(player2)]
        else:
            player2skill = 0    
        ruleset.p1 = Player(player1, player1skill)
        ruleset.p2 = Player(player2, player2skill)
        ruleset.f.write(f'{ruleset.p1.name}, {player1skill}, {ruleset.p2.name}, {player2skill}\n')
        thirdWindow.update()


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
        if rating in range(ruleset.p1.skill[0], ruleset.p1.skill[1]):
            score.throw = aim.target
        elif rating in range(ruleset.p1.skill[1], ruleset.p1.skill[2]):
            score.throw = aim.high
        elif rating in range(ruleset.p1.skill[2], ruleset.p1.skill[3]):
            score.throw = aim.low
        elif rating in range(ruleset.p1.skill[3], ruleset.p1.skill[4]):
            score.throw = aim.right
        elif rating in range(ruleset.p1.skill[4], ruleset.p1.skill[5]):
            score.throw = aim.left
        elif rating in range(ruleset.p1.skill[5], ruleset.p1.skill[6]):
            score.throw = aim.lh
        elif rating in range(ruleset.p1.skill[6], ruleset.p1.skill[7]):
            score.throw = aim.ll
        elif rating in range(ruleset.p1.skill[7], ruleset.p1.skill[8]):
            score.throw = aim.rh
        elif rating in range(ruleset.p1.skill[8], ruleset.p1.skill[9]):
            score.throw = aim.rl
        ruleset.p1.throw += 1
        score.visit += score.throw
        ruleset.f.write(f'{ruleset.p1.name} scores {score.throw}, {ruleset.p1.score-score.visit} remains.\n')
    elif score.atOche == 2:
        if rating in range(ruleset.p2.skill[0], ruleset.p2.skill[1]):
            score.throw = aim.target
        elif rating in range(ruleset.p2.skill[1], ruleset.p2.skill[2]):
            score.throw = aim.high
        elif rating in range(ruleset.p2.skill[2], ruleset.p2.skill[3]):
            score.throw = aim.low
        elif rating in range(ruleset.p2.skill[3], ruleset.p2.skill[4]):
            score.throw = aim.right
        elif rating in range(ruleset.p2.skill[4], ruleset.p2.skill[5]):
            score.throw = aim.left
        elif rating in range(ruleset.p2.skill[5], ruleset.p2.skill[6]):
            score.throw = aim.lh
        elif rating in range(ruleset.p2.skill[6], ruleset.p2.skill[7]):
            score.throw = aim.ll
        elif rating in range(ruleset.p2.skill[7], ruleset.p2.skill[8]):
            score.throw = aim.rh
        elif rating in range(ruleset.p2.skill[8], ruleset.p2.skill[9]):
            score.throw = aim.rl
        ruleset.p2.throw += 1
        score.visit += score.throw
        ruleset.f.write(f'{ruleset.p2.name} scores {score.throw}, {ruleset.p2.score-score.visit} remains.\n')

def legMatch():
    while ruleset.p1.leg != ruleset.win or ruleset.p2.leg != ruleset.win:
        throwpoints()
        if score.atOche == 1:
            if ruleset.p1.score-score.visit == 1 or ruleset.p1.score-score.visit < 0:
                ruleset.f.write(f'{ruleset.p1.name} throws for {score.visit}, Bust!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p1.name} throws for {score.visit}, Bust!\n')
                    logvar.set(f'{ruleset.p1.name} throws for {score.visit}, Bust!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.atOche = 2
                score.visit = 0
                ruleset.p1.throw = 0
            elif ruleset.p1.score-score.visit == 0:
                ruleset.f.write(f'{ruleset.p1.name} throws for {score.visit}, they win the leg!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p1.name} throws for {score.visit}, they win the leg!\n')
                    logvar.set(f'{ruleset.p1.name} throws for {score.visit}, they win the leg!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.visit = 0
                ruleset.p1.throw = 0
                ruleset.p1.leg += 1
                if ((ruleset.p1.leg + ruleset.p2.leg) % 2) == 0:
                    score.atOche = 1
                else: 
                    score.atOche = 2
                ruleset.p1.score = 501
                ruleset.p2.score = 501
                ruleset.p1.throw = 0
                ruleset.p2.throw = 0
                ruleset.f.write(f"{ruleset.p1.name} {ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.leg}\n\n")
                if ruleset.watch == "y":
                    #print(f"{ruleset.p1.name} {ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.leg}\n\n")
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                if ruleset.p1.leg == ruleset.win:
                    break
            elif ruleset.p1.throw == 3:
                ruleset.p1.score -= score.visit
                ruleset.f.write(f'{ruleset.p1.name} throws for {score.visit}, {ruleset.p1.score} remains.\n')
                if ruleset.watch == "y":
                    #print (f'{ruleset.p1.name} throws for {score.visit}, {ruleset.p1.score} remains.\n')
                    logvar.set(f'{ruleset.p1.name} throws for {score.visit}, {ruleset.p1.score} remains.')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                ruleset.p1.throw = 0
                score.visit = 0
                score.atOche = 2
        elif score.atOche == 2:
            if ruleset.p2.score-score.visit == 1 or ruleset.p2.score-score.visit < 0:
                ruleset.f.write(f'{ruleset.p2.name} throws for {score.visit}, Bust!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p2.name} throws for {score.visit}, Bust!\n')
                    logvar.set(f'{ruleset.p2.name} throws for {score.visit}, Bust!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.atOche = 1
                score.visit = 0
                ruleset.p2.throw = 0
            elif ruleset.p2.score-score.visit == 0:
                ruleset.f.write(f'{ruleset.p2.name} throws for {score.visit}, they win the leg!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p2.name} throws for {score.visit}, they win the leg!\n')
                    logvar.set(f'{ruleset.p2.name} throws for {score.visit}, they win the leg!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.visit = 0
                ruleset.p2.throw = 0
                ruleset.p2.leg += 1
                if ((ruleset.p1.leg + ruleset.p2.leg) % 2) == 0:
                    score.atOche = 1
                else: 
                    score.atOche = 2
                ruleset.p1.score = 501
                ruleset.p2.score = 501
                ruleset.p1.throw = 0
                ruleset.p2.throw = 0
                ruleset.f.write(f"{ruleset.p1.name} {ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.leg}\n\n")
                if ruleset.watch == "y":
                    #print(f"{ruleset.p1.name} {ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.leg}\n\n")
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                if ruleset.p2.leg == ruleset.win:
                    break
            elif ruleset.p2.throw == 3:
                ruleset.p2.score -= score.visit
                ruleset.f.write(f'{ruleset.p2.name} throws for {score.visit}, {ruleset.p2.score} remains.\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p2.name} throws for {score.visit}, {ruleset.p2.score} remains.\n')
                    logvar.set(f'{ruleset.p2.name} throws for {score.visit}, {ruleset.p2.score} remains.')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                ruleset.p2.throw = 0
                score.visit = 0
                score.atOche = 1
        if ruleset.watch == "y":
            sleep(0.25)
            
def setMatch():
    while ruleset.p1.set != ruleset.win or ruleset.p2.set != ruleset.win:
        throwpoints()
        if score.atOche == 1:
            if ruleset.p1.score-score.visit == 1 or ruleset.p1.score-score.visit < 0:
                ruleset.f.write (f'{ruleset.p1.name} throws for {score.visit}, Bust!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p1.name} throws for {score.visit}, Bust!\n')
                    logvar.set(f'{ruleset.p1.name} throws for {score.visit}, Bust!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.atOche = 2
                score.visit = 0
                ruleset.p1.throw = 0
            elif ruleset.p1.score-score.visit == 0:
                ruleset.f.write(f'{ruleset.p1.name} throws for {score.visit}, they win the leg!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p1.name} throws for {score.visit}, they win the leg!\n')
                    logvar.set(f'{ruleset.p1.name} throws for {score.visit}, they win the leg!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.visit = 0
                ruleset.p1.throw = 0
                ruleset.p1.leg += 1
                if ruleset.p1.leg == 3:
                    ruleset.p1.leg = 0
                    ruleset.p2.leg = 0
                    ruleset.p1.set += 1
                    ruleset.f.write(f'{ruleset.p1.name} wins the set!\n')
                    if ruleset.watch == "y":
                        #print(f'{ruleset.p1.name} wins the set!\n')
                        logvar.set(f'{ruleset.p1.name} wins the set!')
                        p1scorevar.set(ruleset.p1.score)
                        p2scorevar.set(ruleset.p2.score)
                        p1namevar.set(ruleset.p1.name)
                        p2namevar.set(ruleset.p2.name)
                        p1legsvar.set(ruleset.p1.leg)
                        p2legsvar.set(ruleset.p2.leg)
                        p1setsvar.set(ruleset.p1.set)
                        p2setsvar.set(ruleset.p2.set)
                        watchWindow.update()
                    if ((ruleset.p1.set + ruleset.p2.set) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                else:
                    if ((ruleset.p1.leg + ruleset.p2.leg) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                ruleset.p1.score = 501
                ruleset.p2.score = 501
                ruleset.p1.throw = 0
                ruleset.p2.throw = 0
                ruleset.f.write(f"{ruleset.p1.name} {ruleset.p1.set}-{ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.set}-{ruleset.p2.leg}\n\n")
                if ruleset.watch == "y":
                    #print(f"{ruleset.p1.name} {ruleset.p1.set}-{ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.set}-{ruleset.p2.leg}\n\n")
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                if ruleset.p1.set == ruleset.win:
                    break
            elif ruleset.p1.throw == 3:
                ruleset.p1.score -= score.visit
                ruleset.f.write(f'{ruleset.p1.name} throws for {score.visit}, {ruleset.p1.score} remains.\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p1.name} throws for {score.visit}, {ruleset.p1.score} remains.\n')
                    logvar.set(f'{ruleset.p1.name} throws for {score.visit}, {ruleset.p1.score} remains.')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                ruleset.p1.throw = 0
                score.visit = 0
                score.atOche = 2
        elif score.atOche == 2:
            if ruleset.p2.score-score.visit == 1 or ruleset.p2.score-score.visit < 0:
                ruleset.f.write (f'{ruleset.p2.name} throws for {score.visit}, Bust!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p2.name} throws for {score.visit}, Bust!\n')
                    logvar.set(f'{ruleset.p2.name} throws for {score.visit}, Bust!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.atOche = 1
                score.visit = 0
                ruleset.p2.throw = 0
            elif ruleset.p2.score-score.visit == 0:
                ruleset.f.write(f'{ruleset.p2.name} throws for {score.visit}, they win the leg!\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p2.name} throws for {score.visit}, they win the leg!\n')
                    logvar.set(f'{ruleset.p2.name} throws for {score.visit}, they win the leg!')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                score.visit = 0
                ruleset.p2.throw = 0
                ruleset.p2.leg += 1
                if ruleset.p2.leg == 3:
                    ruleset.p1.leg = 0
                    ruleset.p2.leg = 0
                    ruleset.p2.set += 1
                    ruleset.f.write(f'{ruleset.p2.name} wins the set!\n')
                    if ruleset.watch == "y":
                        #print(f'{ruleset.p2.name} wins the set!\n')
                        logvar.set(f'{ruleset.p2.name} wins the set!')
                        p1scorevar.set(ruleset.p1.score)
                        p2scorevar.set(ruleset.p2.score)
                        p1namevar.set(ruleset.p1.name)
                        p2namevar.set(ruleset.p2.name)
                        p1legsvar.set(ruleset.p1.leg)
                        p2legsvar.set(ruleset.p2.leg)
                        p1setsvar.set(ruleset.p1.set)
                        p2setsvar.set(ruleset.p2.set)
                        watchWindow.update()
                    if ((ruleset.p1.set + ruleset.p2.set) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                else:
                    if ((ruleset.p1.leg + ruleset.p2.leg) % 2) == 0:
                        score.atOche = 1
                    else: 
                        score.atOche = 2
                ruleset.p1.score = 501
                ruleset.p2.score = 501
                ruleset.p1.throw = 0
                ruleset.p2.throw = 0
                ruleset.f.write(f"{ruleset.p1.name} {ruleset.p1.set}-{ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.set}-{ruleset.p2.leg}\n\n")
                if ruleset.watch == "y":
                    #print(f"{ruleset.p1.name} {ruleset.p1.set}-{ruleset.p1.leg}, {ruleset.p2.name} {ruleset.p2.set}-{ruleset.p2.leg}\n\n")
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                if ruleset.p2.set == ruleset.win:
                    break
            elif ruleset.p2.throw == 3:
                ruleset.p2.score -= score.visit
                ruleset.f.write(f'{ruleset.p2.name} throws for {score.visit}, {ruleset.p2.score} remains.\n')
                if ruleset.watch == "y":
                    #print(f'{ruleset.p2.name} throws for {score.visit}, {ruleset.p2.score} remains.\n')
                    logvar.set(f'{ruleset.p2.name} throws for {score.visit}, {ruleset.p2.score} remains.')
                    p1scorevar.set(ruleset.p1.score)
                    p2scorevar.set(ruleset.p2.score)
                    p1namevar.set(ruleset.p1.name)
                    p2namevar.set(ruleset.p2.name)
                    p1legsvar.set(ruleset.p1.leg)
                    p2legsvar.set(ruleset.p2.leg)
                    p1setsvar.set(ruleset.p1.set)
                    p2setsvar.set(ruleset.p2.set)
                    watchWindow.update()
                ruleset.p2.throw = 0
                score.visit = 0
                score.atOche = 1
        if ruleset.watch == "y":
            sleep(0.25)

def copyButton(playerside):
    if playerside == 1:
        scores = open(p1scores, "w")
        scores.truncate(0)
        for i in range(len(ruleset.p1score)):
            scores.write(f'{ruleset.p1score[i]}\n')
        scores.close()
        scores = open(p1scores, "r")
        dataCrunch = scores.read()
        scores.close()
        pyperclip.copy(dataCrunch)
    if playerside == 2:
        scores = open(p2scores, "w")
        scores.truncate(0)
        for i in range(len(ruleset.p2score)):
            scores.write(f'{ruleset.p2score[i]}\n')
        scores.close()
        scores = open(p2scores, "r")
        dataCrunch = scores.read()
        scores.close()
        pyperclip.copy(dataCrunch)

def createFinalLabel(x):
    p1label = tk.Label(scrollingFrame, text=ruleset.p1name[x])
    p2label = tk.Label(scrollingFrame, text=ruleset.p2name[x])
    p1scoreLabel = tk.Label(scrollingFrame, text=ruleset.p1score[x])
    p2scoreLabel = tk.Label(scrollingFrame, text=ruleset.p2score[x])
    p1label.grid(row=x+1, column=0)
    p2label.grid(row=x+1, column=3)
    p1scoreLabel.grid(row=x+1, column=1)
    p2scoreLabel.grid(row=x+1, column=2)
    ruleset.p1namelabels.append(p1label)
    ruleset.p2namelabels.append(p2label)
    ruleset.p1scorelabels.append(p1scoreLabel)
    ruleset.p2scorelabels.append(p2scoreLabel)

def watchWindowInit():
    p1scoreWatch = tk.Label(textvariable=p1scorevar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 50))
    p2scoreWatch = tk.Label(textvariable=p2scorevar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 50))
    logfileWatch = tk.Label(textvariable=logvar, borderwidth=2, relief="ridge", width=50)
    p1nameWatch = tk.Label(textvariable=p1namevar, borderwidth=2, relief="ridge", font=("Arial", 20), width=30)
    p2nameWatch = tk.Label(textvariable=p2namevar, borderwidth=2, relief="ridge", font=("Arial", 20), width=30)
    p1legWatch = tk.Label(text="Legs", borderwidth=2, relief="ridge", font=("Arial", 20))
    p2legWatch = tk.Label(text="Legs", borderwidth=2, relief="ridge", font=("Arial", 20))
    p1setWatch = tk.Label(text="Sets", borderwidth=2, relief="ridge", font=("Arial", 20))
    p2setWatch = tk.Label(text="Sets", borderwidth=2, relief="ridge", font=("Arial", 20))
    p1legsScoreWatch = tk.Label(textvariable=p1legsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
    p2legsScoreWatch = tk.Label(textvariable=p2legsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
    p1setsScoreWatch = tk.Label(textvariable=p1setsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
    p2setsScoreWatch = tk.Label(textvariable=p2setsvar, background="black", foreground="white", borderwidth=2, relief="raised", font=("Arial", 20), width=2)
    watchWindow.columnconfigure(0, weight=1)
    watchWindow.columnconfigure(5, weight=1)
    watchWindow.rowconfigure(0, weight=1)
    p1scoreWatch.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="news")
    p2scoreWatch.grid(row=1, column=4, columnspan=2, rowspan=2, sticky="news")
    logfileWatch.grid(row=1, column=2, columnspan=2, sticky="news")
    p1nameWatch.grid(row=3, column=0, columnspan=2, sticky="news")
    p2nameWatch.grid(row=3, column=4, columnspan=2, sticky="news")
    p1legWatch.grid(row=4, column=0, sticky="news")
    p1setWatch.grid(row=5, column=0, sticky="news")
    p2legWatch.grid(row=4, column=5, sticky="news")
    p2setWatch.grid(row=5, column=5, sticky="news")
    p1legsScoreWatch.grid(row=4, column=1, sticky="news")
    p1setsScoreWatch.grid(row=5, column=1, sticky="news")
    p2legsScoreWatch.grid(row=4, column=4, sticky="news")
    p2setsScoreWatch.grid(row=5, column=4, sticky="news")
    watchWindow.lift()
    watchWindow.grab_set

def restartButton():
    os.execl(sys.executable, sys.executable, *sys.argv)

def submitSecond():
    thirdWindow.deiconify()
    if ruleset.watch == "y":
        watchWindow.deiconify()
    gamesetup1()
    #scrollingFrame.pack(side="top", fill="both",expand="True")
    gamesetup2()

def submit():
    name=nameVar.get()
    win=winVar.get()
    ##nameVar.set("")
    ruleset.title = name
    ruleset.win = win
    print(f'{ruleset.format}, {ruleset.win}, {ruleset.doubles}, {ruleset.watch}, {ruleset.title}')
    playersLabel = tk.Label(secondWindow, text="Insert Player List")
    playersEntry = tk.Text(secondWindow)
    def writeLineup():
        lineup = open(playerlineup, "r+")
        lineup.truncate(0)
        lineup.write(playersEntry.get("1.0", "end-1c"))
        lineup.close()
        submitSecond()
    nameLabel2 = tk.Label(secondWindow, text="Name")
    nameEntry2 = tk.Label(secondWindow, textvariable=nameVar)
    winLabel2 = tk.Label(secondWindow, text="To Win:")
    winEntry2 = tk.Label(secondWindow, textvariable=winVar)
    formatLabel2 = tk.Label(secondWindow, text="Format")
    formatEntry2 = tk.Label(secondWindow, textvariable=formatVar)
    doublesLabel2 = tk.Label(secondWindow, text="Double Start")
    doublesEntry2 = tk.Label(secondWindow, textvariable=doublesVar)
    watchLabel2 = tk.Label(secondWindow, text="Watch")
    watchEntry2 = tk.Label(secondWindow, textvariable=watchVar)
    submitButton = tk.Button(secondWindow, text="Submit", command=lambda:writeLineup())
    playersLabel.grid(column=1)
    playersEntry.grid(row=1, column=1, rowspan=13)
    nameLabel2.grid(row=1, column=0)
    nameEntry2.grid(row=2, column=0)
    winLabel2.grid(row=3, column=0)
    winEntry2.grid(row=4, column=0)
    formatLabel2.grid(row=5, column=0)
    formatEntry2.grid(row=6, column=0)
    doublesLabel2.grid(row=7, column=0)
    doublesEntry2.grid(row=8, column=0)
    watchLabel2.grid(row=11, column=0)
    watchEntry2.grid(row=12, column=0)
    submitButton.grid(row=13, column=0)
    secondWindow.deiconify()
    secondWindow.grab_set()
    secondWindow.lift()
    
    
    


def toggleButton(dataType):
    if dataType == "format":
        if ruleset.format == "legs":
            ruleset.format = "sets"
            formatVar.set(ruleset.format)
            #print(ruleset.format)
        else:
            ruleset.format = "legs"
            formatVar.set(ruleset.format)
            #print(ruleset.format)
    if dataType == "doubles":
        if ruleset.doubles == "n":
            ruleset.doubles = "y"
            doublesVar.set(ruleset.doubles)
            #print(ruleset.doubles)
        else:
            ruleset.doubles = "n"
            doublesVar.set(ruleset.doubles)
            #print(ruleset.doubles)
    if dataType == "watch":
        if ruleset.watch == "n":
            ruleset.watch = "y"
            watchVar.set(ruleset.watch)
            #print(ruleset.watch)
        else:
            ruleset.watch = "n"
            watchVar.set(ruleset.watch)
            #print(ruleset.watch)

button = tk.Button(window, text="Submit Data", command = submit)
formatButton = tk.Button(window, textvariable=formatVar, command= lambda: toggleButton("format"))
formatVar.set(ruleset.format)
doublesButton = tk.Button(window, textvariable=doublesVar, command= lambda: toggleButton("doubles"))
doublesVar.set(ruleset.doubles)
watchButton = tk.Button(window, textvariable=watchVar, command= lambda: toggleButton("watch"))
watchVar.set(ruleset.watch)



nameLabel = tk.Label(window, text="Name")
nameEntry = tk.Entry(window, textvariable=nameVar)
winLabel = tk.Label(window, text="To Win:")
winEntry = tk.Entry(window, textvariable=winVar)
formatLabel = tk.Label(window, text="Format")
doublesLabel = tk.Label(window, text="Double Start")
watchLabel = tk.Label(window, text="Watch")


nameLabel.grid(row = 0, column = 0, columnspan=2)
nameEntry.grid(row = 1, column = 0, columnspan=2)
winLabel.grid(row = 2, column = 0)
winEntry.grid(row=3, column=0)
formatLabel.grid(row=2, column=1)
formatButton.grid(row=3, column=1)
doublesLabel.grid(row=4, column=0)
doublesButton.grid(row=5, column=0)
watchLabel.grid(row=4, column=1)
watchButton.grid(row=5, column=1)
button.grid(row=7, column=1)

window.mainloop()

ruleset.f.close()
print("done")