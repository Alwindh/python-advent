
with open('day2\input.txt', 'r') as openFile:
    readFile=openFile.read()

print(readFile.split('\n')[0])

totalScore = 0



def checkScore(inputLine):
    opponent = inputLine[0]
    you = inputLine[-1]
    if opponent == 'A': #they chose rock
        if you == 'X':
            return 0+3
        if you == 'Y':
            return 3+1
        if you == 'Z':
            return 6+2
    if opponent == 'B':  # they chose paper
        if you == 'X':
            return 0+1
        if you == 'Y':
            return 3+2
        if you == 'Z':
            return 6+3
    if opponent == 'C':  # they chose sciccoror
        if you == 'X':
            return 0+2
        if you == 'Y':
            return 3+3
        if you == 'Z':
            return 6+1
        
for lineee in readFile.split('\n'):
    totalScore+=checkScore(lineee)
    
print(totalScore)