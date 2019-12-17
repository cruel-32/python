import re
import math

def getStringScores(strScore):
    blockReg = re.compile('[0-9]{1,2}[^0-9]+')
    blocks = blockReg.findall(strScore)
    stringScores = []

    for i in range(len(blocks)):
        charReg = re.compile('([0-9]{1,2})([^0-9]?)([^0-9]?)')
        scoreChar = charReg.findall(blocks[i])[0]
        
        tmpNumber = scoreChar[0]
        if(scoreChar[1] == 'S'):
            tmpNumber+='^1'
        if(scoreChar[1] == 'D'):
            tmpNumber+='^2'
        if(scoreChar[1] == 'T'):
            tmpNumber+='^3'
        if(scoreChar[2] == '#'):
            tmpNumber+=' * (-1)'
        if(scoreChar[2] == '*'):
            if(i != 0):
                prevNumber = stringScores[i-1]
                stringScores[i-1] = (prevNumber+' * 2')
            tmpNumber+=' * 2'
        stringScores.append(tmpNumber)
    return ' + '.join(stringScores)

print( getStringScores('1S2D*3T') )
print( getStringScores('1D2S#10S') )
print( getStringScores('1D2S0T') )
print( getStringScores('1S*2T*3S') )
print( getStringScores('1D#2S*3S') )
print( getStringScores('1T2D3D#') )
print( getStringScores('1D2S3T*') )


