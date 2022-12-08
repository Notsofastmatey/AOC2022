debug=False

def getData(fileName):
  '''Gets the forest as a 2D list from the text file'''
  with open(fileName, 'r') as f:
    data = f.readlines()
  forest = [] 
  for raw_line in data:
      split_line = raw_line.strip()
      nums = [int(x) for x in split_line]
      forest.append(nums)
  return forest


#Main program
if debug:
 fileName = 'sample8.txt' 
else:
  fileName = 'day8.txt'

#Get the forest
forest = getData(fileName)

#Set up a 2D list for visibility
numRows = len(forest)
numCols = len(forest[0])

visibleTrees = [ [0]*numCols for i in range(numRows)]

#Make all external trees visible 
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    if j == 0 or j == numCols-1 or i == 0  or i == numRows-1:
        visibleTrees[i][j] = 1

#Check each internal tree on each row
#Left
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      if tree > max(row[0:j]):
        visibleTrees[i][j] = 1
    except:
      pass
#Right
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      if tree > max(row[j+1:]):
        visibleTrees[i][j] = 1
    except:
      pass
#Down 
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      #Get the column it is in as a list
      currentCol=[]
      for x in range(numRows):
        currentCol.append(forest[x][j])
      if tree > max(currentCol[i+1:]):
        visibleTrees[i][j] = 1
    except:
      pass
#Up
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      #Get the column it is in as a list
      currentCol=[]
      for x in range(numRows):
        currentCol.append(forest[x][j])      
      if tree > max(currentCol[:i]):
        visibleTrees[i][j] = 1
    except:
      pass

      
#Show the results
#print(visibleTrees)
result = list(map(sum, visibleTrees))
print(sum(result))

