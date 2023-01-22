import sys

with open(sys.path[0]+'\\input.txt', 'r') as openFile:
    readFile = openFile.read()
    fileLines = readFile.split('\n')

def determineStackAmount(fileLines):
    #count how many stacks of crates there are, assuming the last line contains the most
    lines = 0
    for line in fileLines:
        if '[' in line:
            lines=len(line.split('['))-1
        else:
            break
    return lines

def buildStacks(stackAmount):
    #set up an empty array of stacks depending on the amount of required stacks
    stackArray = {}
    for i in range(stackAmount):
        stackArray[i+1] = []
    return(stackArray)

def fillStacks(stacks,fileLines):
    #start adding the crates to the stacks, from top to bottom
    for line in fileLines:
        if '[' in line:
            for i in stacks.keys():
                foundLetter = line[i+((i-1)*3)]
                if foundLetter != ' ':
                    stacks[i].insert(0,line[i+((i-1)*3)])
    return stacks

def performIterativeMove(stacks, amount, source, target):
    #perform a single move, iterating over the amount of crates that should be moved
    for i in range(amount):
        moveSubStack = stacks[source][-1:]
        stacks[source] = stacks[source][:-1]
        stacks[target] = stacks[target] + moveSubStack
    return stacks


def performStackMove(stacks, amount, source, target):
    #move the crates as a substack, rather than one-by-one
    moveSubStack = stacks[source][-amount:]
    stacks[source] = stacks[source][:-amount]
    stacks[target] = stacks[target] + moveSubStack
    return stacks

def moveCrates(stacks, fileLines, iterative=True): 
    #perform all the moves from the input document
    for line in fileLines:
        if 'move' in line:
            moveAmount = int(line.split(' ')[1])
            moveSource = int(line.split(' ')[3])
            moveTarget = int(line.split(' ')[5])
            if moveAmount > len(stacks[moveSource]):
                moveAmount = len(stacks[moveSource])
            if iterative:
                stacks = performIterativeMove(stacks, moveAmount, moveSource, moveTarget)
            else:
                stacks = performStackMove(stacks, moveAmount, moveSource, moveTarget)
                
    return stacks
    

amountOfStacks = determineStackAmount(fileLines)
emptyStacks = buildStacks(amountOfStacks)
stacks = fillStacks(emptyStacks, fileLines)
stacks = moveCrates(stacks, fileLines)
print('The crates have been moved, one by one')
stackString = ''
for stack in stacks:
    stackString+=stacks[stack][-1]
print(f'The string formed by looking at the top crates is: {stackString}')
print()
emptyStacks = buildStacks(amountOfStacks)
stacks = fillStacks(emptyStacks, fileLines)
stacks = moveCrates(stacks, fileLines, False)
print('Now the crates have been moved by stack')
stackString = ''
for stack in stacks:
    stackString += stacks[stack][-1]
print(f'This way, the string formed by looking at the top crates is: {stackString}')

