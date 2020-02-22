def rotation(m, inputtbl, outputtbl):

    for c in range(0, m + 1, 1):
        for r in range(0, m + 1, 1):
            outputtbl[c][m-r] = inputtbl[r][c]



n = int(input())
N = n-1
table = []
tempTable = []
minimum = []
rotate = 0

for i in range(0, n, 1):
    input2 = input()
    input2 = input2.split()
    input2 = list(map(int, input2))
    table.append(input2)

minimum.append(table[0][0])
minimum.append(table[N][0])
minimum.append(table[N][N])
minimum.append(table[0][N])
minimum.sort()

if minimum[0] == table[0][0]:
    rotate = 0
elif minimum [0] == table[N][0]:
    rotate = 1
elif minimum[0] == table[N][N]:
    rotate = 2
elif minimum[0] == table[0][N]:
    rotate = 3

tempTable = [[0 for i in range(n)] for j in range(n)]

for i in range(0, rotate, 1):
    rotation(N, table, tempTable)
    for j in range(n):
        for k in range(n):
            table[j][k] = tempTable[j][k]

for i in range(n):
    print(" ".join(str(x) for x in table[i]))
