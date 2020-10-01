
'''
Matrix disposition:
  a | b | c 
 -----------
  d | e | f
 -----------
  g | h | i 
'''
# Call at the begining
def initMatrix():
    matrixValues = {
                    7: '7',
                    8: '8',
                    9: '9',
                    4: '4',
                    5: '5',
                    6: '6',
                    1: '1',
                    2: '2',
                    3: '3',
                    }                    
    return matrixValues
    
# Print the matrix with values
def showMatrix(matrixValues):
    a = matrixValues[7]
    b = matrixValues[8]
    c = matrixValues[9]
    d = matrixValues[4]
    e = matrixValues[5]
    f = matrixValues[6]
    g = matrixValues[1]
    h = matrixValues[2]
    i = matrixValues[3]
    
    print('\n\n\n\n\n')
    print(f' {a} | {b} | {c} ')
    print('-----------')
    print(f' {d} | {e} | {f} ')
    print('-----------')
    print(f' {g} | {h} | {i} ')
    
# Check win
def checkWin(matrixValues):
    a = matrixValues[7]
    b = matrixValues[8]
    c = matrixValues[9]
    d = matrixValues[4]
    e = matrixValues[5]
    f = matrixValues[6]
    g = matrixValues[1]
    h = matrixValues[2]
    i = matrixValues[3]
    
    if(a == 'X' and b == 'X' and c == 'X'):
        return 'X'
    if(d == 'X' and e == 'X' and f == 'X'):
        return 'X'
    if(g == 'X' and h == 'X' and i == 'X'):
        return 'X'
    if(a == 'X' and d == 'X' and g == 'X'):
        return 'X'
    if(b == 'X' and e == 'X' and h == 'X'):
        return 'X'
    if(c == 'X' and f == 'X' and i == 'X'):
        return 'X'
    if(a == 'X' and e == 'X' and i == 'X'):
        return 'X'
    if(g == 'X' and e == 'X' and c == 'X'):
        return 'X'
    
    if(a == 'O' and b == 'O' and c == 'O'):
        return 'O'
    if(d == 'O' and e == 'O' and f == 'O'):
        return 'O'
    if(g == 'O' and h == 'O' and i == 'O'):
        return 'O'
    if(a == 'O' and d == 'O' and g == 'O'):
        return 'O'
    if(b == 'O' and e == 'O' and h == 'O'):
        return 'O'
    if(c == 'O' and f == 'O' and i == 'O'):
        return 'O'
    if(a == 'O' and e == 'O' and i == 'O'):
        return 'O'
    if(g == 'O' and e == 'O' and c == 'O'):
        return 'O'
        
        
        
        
        
        
        
        
  
