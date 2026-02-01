numbers = input().split()
numN = int(numbers[0])
numM = int(numbers[1])
textS = input()
textT = input()
count = 0

for i in range(numM - numN + 1):
    match = True
    for j in range(numN):
        if textT[i + j] != textS[j]:
            match = False
            break
    if match:
        count += 1

print(count)

