import time
import random

def botPlay(matrixValues):
    
    # memory possible win / winPatterns
    memPatterns = [0, 0, 0, 0, 0, 0, 0, 0]
    memPatternsEnnemy = [0, 0, 0, 0, 0, 0, 0, 0]
    
    # Winning pattern
    winPatterns = [
                  [matrixValues[7], matrixValues[8], matrixValues[9]], # Pattern 0
                  [matrixValues[4], matrixValues[5], matrixValues[6]], # Pattern 1
                  [matrixValues[1], matrixValues[2], matrixValues[3]], # Pattern 2
                  [matrixValues[7], matrixValues[4], matrixValues[1]], # Pattern 3
                  [matrixValues[8], matrixValues[5], matrixValues[2]], # Pattern 4
                  [matrixValues[9], matrixValues[6], matrixValues[3]], # Pattern 5
                  [matrixValues[7], matrixValues[5], matrixValues[3]], # Pattern 6
                  [matrixValues[9], matrixValues[5], matrixValues[1]]  # Pattern 7
                    ]
    print(winPatterns)
    
    for i in range(0, len(winPatterns)):
        for m in range(0, len(winPatterns[i])):
            if(winPatterns[i][m] == 'X'):
                memPatterns[i] -= 2
        for j in range(0, len(winPatterns[i])):
            if(winPatterns[i][j] == 'O'):
                memPatterns[i] += 1
        ###################################################
        # Same but reversed
        for m in range(0, len(winPatterns[i])):
            if(winPatterns[i][m] == 'X'):
                memPatterns[i] -= 2
        for j in range(len(winPatterns[i])-1, -1, -1):
            if(winPatterns[i][j] == 'O'):
                memPatterns[i] += 1
        highestNum = -10
        highestNumIndex = 0
        for p in range(0, len(memPatterns)):
            if(memPatterns[p] > highestNum and memPatterns[p] >= 0):
                highestNum = memPatterns[p]
                highestNumIndex = p
        print(f'highest = {highestNum}, highestIndex = {highestNumIndex}')
        print(f'memPatterns {memPatterns}')
        
    if(highestNum == 4):
        for k in range(0, 3):
            if(winPatterns[highestNumIndex][k] != 'O' and winPatterns[highestNumIndex][k] != 'X'):
                print(f'Placement : {winPatterns[i][k]}')
                print(f'memPatterns {memPatterns}')
                return int(winPatterns[highestNumIndex][k])
    else:
        for i in range(0, len(winPatterns)):
            for m in range(0, len(winPatterns[i])):
                if(winPatterns[i][m] == 'O'):
                    memPatternsEnnemy[i] -= 1
                if(winPatterns[i][m] == 'X'):
                    memPatternsEnnemy[i] += 1
                    if(memPatternsEnnemy[i] == 2):
                        for k in range(0, 3):
                            print(k)
                            if(winPatterns[i][k] != 'O' and winPatterns[i][k] != 'X'):
                                print(f'Placement : {winPatterns[i][k]}')
                                print(f'memPatternsEnnemy {memPatternsEnnemy}')
                                print('Ennemy counter')
                                return int(winPatterns[i][k])     
    
    print(memPatterns)
    while(True):
        for k in range(0, 3):
            if(winPatterns[highestNumIndex][k] != 'O' and winPatterns[highestNumIndex][k] != 'X'):
                print(f'Placement : {winPatterns[i][k]}')
                print(f'memPatterns {memPatterns}')
                return int(winPatterns[highestNumIndex][k])
        print('secondaire')
        rand = random.randint(1, 9)
        if(matrixValues[rand] != 'X' and matrixValues[rand] != 'O'):
            return rand
