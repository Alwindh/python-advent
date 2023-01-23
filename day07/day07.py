import sys

with open(sys.path[0]+'\\input.txt', 'r') as openFile:
    readFile = openFile.read()
    lineList = readFile.split('\n')

currentPosition = []
dirDict = {}

def moveCursor(current, command):
    #this will move the cursor to the new target, and return the entire path it's currently in
    moveGoal = command.split(' cd ')[-1]
    if current == [] or moveGoal == '/':
        return [moveGoal]
    if moveGoal == '..':
        if len(current) > 1:
            return current[:-1]
        else:
            return ['/']
    current.append(moveGoal)
    return current

for line in lineList:
    if '$ cd ' in line: #then it's a change directory command, so handle it via moveCursor
        currentPosition = moveCursor(currentPosition, line)
    if line[0] != '$': #not a command, so either a folder or a file.
        isFile = line[:4] != 'dir ' #quick check to determine whether it's a file or directory
        fileSize = 0 #for simplicity's sake, folders have a filesize of 0
        if isFile:
            fileSize = int(line.split(' ')[0]) #if it is a file, set the file size accordingly
        try: # if it exists, append contents to list, and update total size
            dirDict[tuple(currentPosition)]['contents'].append(line)
            dirDict[tuple(currentPosition)]['totalSize'] += fileSize
        except KeyError: #if not, create it
            dirDict[tuple(currentPosition)] = {'contents' : [line], 'totalSize': fileSize}
            
for dir in dirDict:
    dirStr = str(dir)[1:-1] #turning it into a string for easy comparison
    for subDir in dirDict:
        subDirStr = str(subDir)[1:-1] #turning it into a string for easy comparison
        if dirStr in subDirStr and dirStr != subDirStr: # if it's a subdirectory 
            dirDict[dir]['totalSize'] += dirDict[subDir]['totalSize'] # add it to the higher level total
            
tally = 0
for dir in dirDict:
    if dirDict[dir]['totalSize'] <= 100000: # if it's smaller
        tally += dirDict[dir]['totalSize'] # add to tally
print(f"The total of folders smaller than 100000 is {tally}")

remainingSpace = 70000000 - dirDict[tuple(['/'])]['totalSize']
goalSpace = 30000000 - remainingSpace

removeFolder = {'directory': tuple(['/']), 'totalSize': dirDict[tuple(['/'])]['totalSize']} # baseline case

for dir in dirDict:
    # check whether it's big enough to make sufficient space, and smaller than the current smallest option
    if dirDict[dir]['totalSize'] > goalSpace and dirDict[dir]['totalSize'] < removeFolder['totalSize']:
        removeFolder = {'directory': dir,
                        'totalSize': dirDict[dir]['totalSize']}
print(
    f'In order to free up enough space, you can remove {removeFolder["directory"]} to save {removeFolder["totalSize"]}')
