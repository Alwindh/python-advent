import sys

with open(sys.path[0]+'\\input.txt', 'r') as openFile:
    readFile = openFile.read()
    pairsList = readFile.split('\n')
    
def checkFullContain(pair):
    #checks if one of the elfs numbers fully contains the other
    firstElf = pair.split(',')[0]
    secondElf = pair.split(',')[1]
    return checkElfs(firstElf, secondElf) or checkElfs(secondElf,firstElf)

def checkElfs(elf1, elf2):
    #checks if elf1 contains elf2
    return int(elf2.split('-')[0]) >= int(elf1.split('-')[0]) and int(elf2.split('-')[-1]) <= int(elf1.split('-')[-1])

def checkPartialElfs(elf1, elf2):
    #checks if elf1 has any overlap at all with elf 2
    firstCheck = int(elf1.split('-')[0]) >= int(elf2.split('-')[0]) and int(elf1.split('-')[0]) <= int(elf2.split('-')[-1])
    secondCheck = int(elf1.split('-')[-1]) >= int(elf2.split('-')[0]) and int(elf1.split('-')[0]) <= int(elf2.split('-')[-1])
    return(firstCheck or secondCheck)


def checkPartialContain(pair):
    # checks if one of the elfs numbers at least partially contains the other
    firstElf = pair.split(',')[0]
    secondElf = pair.split(',')[1]
    partialContain = checkPartialElfs(firstElf, secondElf)
    return partialContain

containedPairs = 0
for pairs in pairsList:
    if checkPartialContain(pairs):
        containedPairs +=1
print(containedPairs)