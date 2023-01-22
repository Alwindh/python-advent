import re

with open('input.txt', 'r') as openFile:
    readFile=openFile.read()


splitElfs = readFile.split('\n\n')
amountList = []
for elf in splitElfs:
    sumNum = 0
    for amount in elf.split('\n'):
        sumNum+=int(amount)
    amountList.append(sumNum)

# print(amountList[-1])


maxElf = (max(amountList))

print(maxElf)

amountList.pop(amountList.index(maxElf))
maxElf = (max(amountList))

print(maxElf)

amountList.pop(amountList.index(maxElf))
maxElf = (max(amountList))

print(maxElf)


