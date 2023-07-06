n = int(input().strip())

for i in range(n):
    string = input()
    strEven = [x for j, x in enumerate(string) if j % 2 == 0]
    strOdd = [x for j, x in enumerate(string) if j % 2 != 0]
    print("".join(strEven), "".join(strOdd))
