from collections import defaultdict
import numpy as np

debug=False
part = 1

if debug:
  fileName = "sample7.txt"
else:
  fileName = "day7.txt"

def getDirectories(fileName):
  path=[]
  folderSizes = defaultdict(int)
  with open(fileName) as file:
    for line in file:
      commands=line.strip().split(' ')
      if commands[0] == '$' and commands[1] == 'cd':
        if commands[2] == '/':
          path=['/']
        elif commands[2] == '..':
          path.pop()
        else:
          path.append(commands[2])     
      elif commands[0] == '$' and commands[1] == 'ls':
        pass
      else:
        if commands[0][0].isdigit():
          size = int(commands[0])
          for i in range(len(path)):
            folderSizes['/'.join(path[:i+1])] += size
    
    pt1 = sum(fsize for fsize in folderSizes.values() if fsize <= 100000)
    
    needed = 30000000
    used = folderSizes['/']
    available = 70000000-used
    diff = needed-available

    newdictionary = dict()
    for key, value in folderSizes.items():
      if value >= diff:
        newdictionary[key] = value

    keys = list(newdictionary.keys())
    values = list(newdictionary.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    pt2 = list(sorted_dict.values())[0]
    
    return pt1, pt2
    
pt1, pt2 = getDirectories(fileName)  
print(f"Part 1: {pt1}")
print(f"Part 2: {pt2}")

