import random

rating = random.randint(0,100)
player1 = "Chisnall"
p1score = 501
player2 = "van Gerwen"
p2score = 501
player = 1
throw = 0
throw1 = 0
throw2 = 0
throw3 = 0

for i in range(6):
    throw += 1
    if player == 1:
        p1score = p1score-rating
        print(rating)
        if throw == 1:
            throw1 = rating
        elif throw == 2:
            throw2 = rating
        else:
            throw3 = rating
    else: 
        p2score = p2score-rating
        print(rating)
        if throw == 1:
            throw1 = rating
        elif throw == 2:
            throw2 = rating
        else:
            throw3 = rating
    rating = random.randint(0,100)
    if throw == 3:
        throw = 0
        if player == 1:
            player += 1
            print (f'{player1} throws for {throw1}-{throw2}-{throw3}, score is {p1score}')
        else:
            player = 1
            print (f'{player2} throws for {throw1}-{throw2}-{throw3}, score is {p2score}')
        #break




