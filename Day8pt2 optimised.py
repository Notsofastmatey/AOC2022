debug=False

def flatten(seq):
  for el in seq:
    if isinstance(el, list):
      yield from flatten(el)
    else:
      yield el

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

#Set up a 2D list for scenic scores
numRows = len(forest)
numCols = len(forest[0])

scenicScores = [[0]*numCols for i in range(numRows)]
#print(scenicScores)

#Check each internal tree on each row
#Left
#print("Checking trees to the left")
for i, row in enumerate(forest):
  #print(row)
  for j, tree in enumerate(row):
    try:
      # print(f"The current tree is {tree}")
      # print(f"i is {i}")
      # print(f"j is {j}")
      # print(f"The area to examine is {row[0:j]}")
      for viewedTree in reversed(row [0:j]):
        if tree > viewedTree:
          scenicScores[i][j] += 1
          #print(f"{tree} is bigger than {viewedTree} so the score is now {scenicScores[i][j]}.")
        elif tree <=viewedTree:
          scenicScores[i][j] += 1
          #print(f"{tree} is the same size or smaller than {viewedTree} so we stop here and the score is now {scenicScores[i][j]}.")
          break
          

    except:
      print("First item")
#Right
# print()
# print("Checking trees to the right")
# print()
for i, row in enumerate(forest):
  #print(row)
  for j, tree in enumerate(row):
    try:
      temp=0
      # print(f"The current tree is {tree}")
      # print(f"i is {i}")
      # print(f"j is {j}")
      # print(f"The area to examine is {row[j+1:]}")
      for viewedTree in row [j+1:]:
        if tree > viewedTree:
          temp+=1
          #print(f"{tree} is bigger than {viewedTree} so the score is now {temp}.")
        elif tree <=viewedTree:
          temp += 1
          #print(f"{tree} is the same size or smaller than {viewedTree} so we stop here and the score is now {temp}.")
          break
      #print(f"The score for this tree is {temp}.")
      scenicScores[i][j] = scenicScores[i][j] * temp
    except:
      print("First item")
#Down 
# print()
# print("Checking trees below")
# print()
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      #Get the column it is in as a list
      currentCol=[]
      for x in range(numRows):
        currentCol.append(forest[x][j])
      temp=0  
      # print(f"The current column is {currentCol}")
      # print(f"The current tree is {tree}")
      # print(f"i is {i}")
      # print(f"j is {j}")
      # print(f"The area to examine is {currentCol[i+1:]}")

      for viewedTree in currentCol[i+1:]:
        if tree > viewedTree:
          temp+=1
          #print(f"{tree} is bigger than {viewedTree} so the score is now {temp}.")
        elif tree <=viewedTree:
          temp+=1
          #print(f"{tree} is the same size or smaller than {viewedTree} so we stop here and the score is now {temp}.")
          break
      scenicScores[i][j] = scenicScores[i][j] * temp
    except:
      print("First item")
#Up
# print()
# print("Checking trees above")
# print()
for i, row in enumerate(forest):
  for j, tree in enumerate(row):
    try:
      #Get the column it is in as a list
      currentCol=[]
      for x in range(numRows):
        currentCol.append(forest[x][j])
      temp=0
      # print(f"The current column is {currentCol}")
      # print(f"The current tree is {tree}")
      # print(f"i is {i}")
      # print(f"j is {j}")
      # print(f"The area to examine is {currentCol[:i]}")
      for viewedTree in reversed(currentCol[:i]):
        if tree > viewedTree:
          temp+=1
          #print(f"{tree} is bigger than {viewedTree} so the score is now {temp}.")
        elif tree <=viewedTree:
          temp+=1
          #print(f"{tree} is the same size or smaller than {viewedTree} so we stop here and the score is now {temp}.")
          break
      scenicScores[i][j] = scenicScores[i][j] * temp
    except:
      print("First item")

      
#Show the results
for s in scenicScores:
  print(s)
print(max(flatten(scenicScores)))
