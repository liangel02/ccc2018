n = int(input())

village = []
allDistances = []
neighbourhood = []

for i in range(0, n, 1):
    input1 = int(input())
    village.append(input1)
village.sort()

for i in range(1, len(village), 1):
    difference = village[i]-village[i-1]
    distance = difference/2
    allDistances.append(distance)

for i in range(0, len(allDistances)-1, 1):
    addition = allDistances[i] + allDistances[i+1]
    neighbourhood.append(addition)
neighbourhood.sort()
print(neighbourhood[0])
