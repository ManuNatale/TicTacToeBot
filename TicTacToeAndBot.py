import gameMatrix as gm
import bot
import random
import time

while(True):

    matrixValues = gm.initMatrix()
    firstTurn = True
    nbTurns = 0
    
    beginChoice = input('\n\nWho begin ?\n\n1. You (X)\n2. Bot (O)\n\n> ')
    
    if (beginChoice == '1'): 
    
        gm.showMatrix(matrixValues)
    
        while (True):
            nbTurns += 1
            
            while(True):
                try:
                    print('X turn')
                    xPlayer = int(input("> "))
                except ValueError:
                    print('Need an integer')
                    continue
                if(xPlayer > 9 or xPlayer < 1):
                    print('Integer beetween 1 and 9')
                    continue
                elif(matrixValues[xPlayer] != 'X' and matrixValues[xPlayer] != 'O'):
                    matrixValues[xPlayer] = 'X'
                    break
                else:
                    print('impossible')
                    continue
                    
            gm.showMatrix(matrixValues)
            if(gm.checkWin(matrixValues) == 'X'):
                print('X win\n')
                break
            elif(gm.checkWin(matrixValues) == 'O'):
                print('O win\n')
                break
                
            if(nbTurns == 5):
                print('Draw')
                break
                    
            print('O turn')
            time.sleep(0.5)    
            
            while(True):
                if(firstTurn == True):
                    rand = random.randint(1, 9)
                    if(matrixValues[rand] != 'X' and matrixValues[rand] != 'O'):
                        matrixValues[rand] = 'O'
                        firstTurn = False
                        break
                    else:
                        continue
                # run bot
                numPlayed = bot.botPlay(matrixValues)
                matrixValues[numPlayed] = 'O'
                break
                
            gm.showMatrix(matrixValues)
            if(gm.checkWin(matrixValues) == 'X'):
                print('X win\n')
                break
            elif(gm.checkWin(matrixValues) == 'O'):
                print('O win\n')
                break
            
    if (beginChoice == '2'): 
    
        gm.showMatrix(matrixValues)
    
        while (True):
            nbTurns += 1
            
            print('O turn')
            time.sleep(0.5)    
            
            while(True):
                if(firstTurn == True):
                    rand = random.randint(1, 9)
                    if(matrixValues[rand] != 'X' and matrixValues[rand] != 'O'):
                        matrixValues[rand] = 'O'
                        firstTurn = False
                        break
                    else:
                        continue
                # run bot
                numPlayed = bot.botPlay(matrixValues)
                matrixValues[numPlayed] = 'O'
                break
                
            gm.showMatrix(matrixValues)
            if(gm.checkWin(matrixValues) == 'X'):
                print('X win')
                break
            elif(gm.checkWin(matrixValues) == 'O'):
                print('O win')
                break
                
            if(nbTurns == 5):
                print('Draw')
                break
                
            while(True):
                try:
                    print('X turn')
                    xPlayer = int(input("> "))
                except ValueError:
                    print('Need an integer')
                    continue
                if(xPlayer > 9 or xPlayer < 1):
                    print('Integer beetween 1 and 9')
                    continue
                elif(matrixValues[xPlayer] != 'X' and matrixValues[xPlayer] != 'O'):
                    matrixValues[xPlayer] = 'X'
                    break
                else:
                    print('impossible')
                    continue
    
            gm.showMatrix(matrixValues)
            if(gm.checkWin(matrixValues) == 'X'):
                print('X win')
                break
            elif(gm.checkWin(matrixValues) == 'O'):
                print('O win')
                break


