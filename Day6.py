debug=False
part = 2

if debug:
  fileName = "sample6.txt"
else:
  fileName = "day6.txt"

if part == 1:
  windowSize = 4
  msg = 'packet'
else:
  windowSize = 14
  msg = 'message'

with open(fileName, 'r') as file:
  datastream = file.read()

for i in range(len(datastream) - windowSize + 1):
  window = (datastream[i: i + windowSize])
  print(window)
  if (len(set(window))) == windowSize:
    packetStart = i + windowSize
    print(f"Start of {msg} is at {packetStart}")
    break
  