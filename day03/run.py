class ruckSacks:
    def __init__(self):
        self.list = self.generateList()
        self.totalValue = self.calculateValue(self.list)
        print(self.totalValue)
    
    def generateList(self):
        with open('day2\day3\input.txt', 'r') as openFile:
            readFile = openFile.read()
        return readFile.split('\n')
    
    def checkCombination(self,inputItem):
        itemLength = int(len(inputItem)/2)
        firstItem = inputItem[:itemLength]
        secondItem = inputItem[itemLength:]
        combination = ""
        for i in firstItem:
            if i in secondItem:
                combination = i
        return combination
    
    def checkValue(self, itemKey):
        valueString='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return 1+valueString.index(itemKey)
    
    def calculateValue(self, inputList):
        totalValue = 0
        for item in inputList:
            itemKey = self.checkCombination(item)
            itemValue = self.checkValue(itemKey)
            totalValue+=itemValue
        return totalValue
            
# item = ruckSacks()


class ruckSackGroups:
    def __init__(self):
        self.list = self.generateList()
        self.groups = self.splitGroups(self.list)
        self.totalValue = self.calculateValue(self.groups)
        print(self.totalValue)

    def generateList(self):
        with open('day2\day3\input2.txt', 'r') as openFile:
            readFile = openFile.read()
        return readFile.split('\n')
    
    def splitGroups(self,inputList):
        groupList = []
        while len(inputList) > 0:
            groupList.append(inputList[:3])
            inputList = inputList[3:]
        return groupList

    def checkCombination(self, inputItem):
        print(inputItem)
        firstItem = inputItem[0]
        secondItem = inputItem[1]
        thirdItem = inputItem[2]
        combination = ""
        for i in firstItem:
            if i in secondItem and i in thirdItem:
                combination = i
        print(combination)
        return combination

    def checkValue(self, itemKey):
        valueString = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return 1+valueString.index(itemKey)

    def calculateValue(self, inputList):
        totalValue = 0
        for itemGroup in inputList:
            itemKey = self.checkCombination(itemGroup)
            itemValue = self.checkValue(itemKey)
            totalValue += itemValue
        return totalValue

groups = ruckSackGroups()