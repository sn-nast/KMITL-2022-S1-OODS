# Box

inp = input('Enter Input : ').split('/')
maxBoxCount, inp = int(inp[1]), list(map(int, inp[0].split(' ')))
qSum = None
size = len(inp)+1
ans = []
for i in range(len(inp)+1):
    ans.append([])
    for j in range(len(inp)+1):
        ans[i].append([])
        for k in range(maxBoxCount+1):
            ans[i][j].append(9999999)
qSum = [0]+inp
for i in range(len(qSum)-1):
    qSum[i+1] += qSum[i]
for i in range(len(inp)):
    ans[i][1][1] = inp[i]


def func(startIndex, length, leftLength, rightLength, leftWeigth, rightWeigth):
    newValue = max(ans[startIndex][leftLength][leftWeigth],
                   ans[startIndex+leftLength][rightLength][rightWeigth])
    ans[startIndex][length][leftWeigth +
                            rightWeigth] = min(ans[startIndex][length][leftWeigth+rightWeigth], newValue)


length = 2
count = 0
while length < len(inp)+1:
    startIndex = 0
    while startIndex+length < len(inp)+1:
        ans[startIndex][length][1] = qSum[startIndex+length]-qSum[startIndex]
        count += 1
        leftLength = 1
        while leftLength < length:
            rightLength = length - leftLength
            leftWeigth = 1
            while leftWeigth <= leftLength:
                rightWeigth = 1
                while rightWeigth <= rightLength and rightWeigth + leftWeigth <= maxBoxCount:
                    func(startIndex, length, leftLength,
                         rightLength, leftWeigth, rightWeigth)
                    count += 1
                    rightWeigth += 1
                leftWeigth += 1
            leftLength += 1
        startIndex += 1
    length += 1

print('Minimum weigth for {0} box(es) = {1}'.format(
    maxBoxCount, ans[0][len(inp)][maxBoxCount]))

# From Au.
