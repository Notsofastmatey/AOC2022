class Computer:
  def __init__(self, lines):
    self.commands = lines
    self.clock = 0
    self.x = 1
    self.totalSignalStrength = 0

  def run(self):
    for line in self.commands:
      if line[:4]=='noop':
        self.noop()
      else:
        v=int(line.split(' ')[1])
        self.add(v)

  def noop(self):
    self.tick()

  def add(self, v):
    self.tick()
    self.tick()
    self.x += v

  def tick(self):
    self.clock +=1
    if (self.clock-20) % 40 == 0:
      self.totalSignalStrength += self.clock * self.x
      print(f"Clock: {self.clock} | X: {self.x} | Total Signal Strength: {self.totalSignalStrength}")

def getData(fileName):
  '''Gets the commands as a 2D list from the text file'''
  with open(fileName, 'r') as f:
    data = f.readlines()   
  return data
    
#Main program
debug=False
      
if debug:
 fileName = 'sample10.txt' 
else:
  fileName = 'day10.txt'

 


commands = getData(fileName)
computer = Computer(commands)
computer.run()

print(f"Part 1: {computer.totalSignalStrength}")