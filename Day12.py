from collections import deque
#This is a double-ended queue. We can add and remove items from both ends.

debug=False
if debug:
  fileName = "sample12.txt"
else:
  fileName = "day12.txt"

#Get the text file
grid = [list(x) for x in open(fileName).read().strip().splitlines()]

#Get the start and end positions and set their actual heights
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

#Create a queue and add the start position, with its distance from itself
q = deque()
q.append((0, sr, sc))

#Create a set to hold nodes we've visited. 
visitedNodes = {(sr, sc)}

#Iterate over the grid.
while q:
    #Remove the next item from the queue
    d, r, c = q.popleft()
    #Look through the neighbours
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        #Ignore if off the grid
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        #Ignore if already visited
        if (nr, nc) in visitedNodes:
            continue
        #Ignore if too great a step up
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
            continue
        #Print the distance if it's the end
        if nr == er and nc == ec:
            print(f"The distance is {d + 1}.")
            break
        #Add next row/col to visited set and queue
        visitedNodes.add((nr, nc))
        q.append((d + 1, nr, nc))