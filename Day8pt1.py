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
print(visibleTrees)

#Make all external trees visible 
print("Making external trees visible")
for i, row in enumerate(forest):
  print(row)
  for j, tree in enumerate(row):
    print(tree)
    print(row[0:j])
    if j == 0 or j == numCols-1 or i == 0  or i == numRows-1:
        visibleTrees[i][j] = 1

#Check each internal tree on each row
#Left
print("Checking trees to the left")
for i, row in enumerate(forest):
  print(row)
  for j, tree in enumerate(row):
    print(tree)
    print(row[0:j])
    try:
      if tree > max(row[0:j]):
        print("Visible!")
        visibleTrees[i][j] = 1
    except:
      print("First item")
#Right
print("Checking trees to the right")
for i, row in enumerate(forest):
  print(row)
  for j, tree in enumerate(row):
    try:
      print(f"The current tree is {tree}")
      print(f"i is {i}")
      print(f"j is {j}")
      print(f"The area to examine is {row[j+1:]}")
      print(f"The highest value is {max(row[j+1:])}")
      if tree > max(row[j+1:]):
        print("Visible!")
        visibleTrees[i][j] = 1
    except:
      print("First item")
#Down 
print("Checking trees below")
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      #Get the column it is in as a list
      currentCol=[]
      for x in range(numRows):
        currentCol.append(forest[x][j])
      print(f"The current column is {currentCol}")
      print(f"The current tree is {tree}")
      print(f"i is {i}")
      print(f"j is {j}")
      print(f"The area to examine is {currentCol[i+1:]}")
      print(f"The highest value is {max(currentCol[i+1:])}")
      
      if tree > max(currentCol[i+1:]):
        print("Visible!")
        visibleTrees[i][j] = 1
    except:
      print("First item")
#Up
print()
print("Checking trees above")
print()
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      #Get the column it is in as a list
      currentCol=[]
      for x in range(numRows):
        currentCol.append(forest[x][j])
      print(f"The current column is {currentCol}")
      print(f"The current tree is {tree}")
      print(f"i is {i}")
      print(f"j is {j}")
      print(f"The area to examine is {currentCol[:i]}") #This is not correct
      print(f"The highest value is {max(currentCol[:i])}")
      
      if tree > max(currentCol[:i]):
        print("Visible!")
        visibleTrees[i][j] = 1
    except:
      print("First item")

      
#Show the results
print(visibleTrees)
result = list(map(sum, visibleTrees))
print(sum(result))

