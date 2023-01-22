import sys

with open(sys.path[0]+'\\input.txt', 'r') as openFile:
    readFile = openFile.read()


def checkIfSignal(checkString):
    #iterate of the characters, checking if it's in the remaining string
    for i in range(len(checkString)):
        if checkString[i] in checkString[i+1:]:
            return False
    return True


for i in range(0,len(readFile)-3):
    markerLength = 14 #somehow the second assignment was to change 4 into 14?
    chunk = readFile[i:i+markerLength]
    if (checkIfSignal(chunk)):
        print(f'The signal appears at index: {i+len(chunk)}')
        break
