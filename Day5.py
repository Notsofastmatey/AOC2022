debug=False
part = 2

sampleStacks = [
['Z', 'N'],
['M', 'C', 'D'],
['P'],
]

realStacks = [
['D','B','J','V'],
['P','V','B','W','R','D','F'],
['R','G','F','L','D','C','W','Q'],
['W','J','P','M','L','N','D','B'],
['H','N','B','P','C','S','Q'],
['R','D','B','S','N','G'],
['Z','B','P','M','Q','F','S','H'],
['W','L','F'],
['S','V','F','M','R']
]

def getMoves(file):
  moves=[]
  cleanedMoves=[]
  for line in file:
    if line[0] == 'm':
        moves.append(line.strip())
  for move in moves:
    cleanedMoves.append(move.split(' '))
  for cleanedMove in cleanedMoves:
    del cleanedMove[0]
    del cleanedMove[1]
    del cleanedMove[2]
  return cleanedMoves

def moveCrates(stacks, moveCommands, part):
  for move in moveCommands:
    numCrates = int(move[0])
    fromStack = int(move[1])
    toStack = int(move[2])
    print(f"Moving {numCrates} crate(s) from stack {fromStack} to stack {toStack}")

    if part == 1:
      #Repeat the move as many times as specified, popping out the last crate each time
      for i in range(numCrates):
        stacks[toStack-1].append(stacks[fromStack-1].pop())
    else:
      #Use a negative list slice to get the last n crates and join them to the toStack
      stacks[toStack-1] = stacks[toStack-1] + stacks[fromStack-1][-numCrates:] 
      #Pop the last element out of the fromStack however many times we need to.
      for i in range(int(move[0])):
        stacks[fromStack-1].pop()
  #Print the stacks and return the answer
  answer = ''
  for count,stack in enumerate(stacks):
    print(f"Stack {count+1}: {stacks[count]}")
    answer+=stack[-1]
  return answer

# Main program
if debug:
  fileName = "sample5.txt"
  startStacks = sampleStacks
else:
  fileName = "day5.txt"
  startStacks = realStacks
  
with open(fileName) as file:
  answer = moveCrates(startStacks, getMoves(file), part)
  print(f"The answer to part {part} is {answer}.")

