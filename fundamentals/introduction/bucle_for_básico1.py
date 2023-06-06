for idx in range(0, 151):
    print(idx)

for idx in range(0, 1001, 5):
    if (idx % 5 == 0):
        print(idx)

for idx in range(0, 101):
    if idx % 5 == 0:
        if idx % 2 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(idx)

sumImpares = 0
for idx in range(1, 500001, 2):
    sumImpares += idx
print(sumImpares)

for x in range(2018, 0, -4):
    print(x)

lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)
