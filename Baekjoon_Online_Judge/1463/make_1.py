# BOJ 1463 Make 1
n = int(input())
if n == 1:
    print(0)
else:
    temp = [n]
    count = 0
    while 1 not in temp:
        count += 1
        arr = temp.copy()
        temp = []
        for i in arr:
            temp.append(i - 1)
            if i % 3 == 0: temp.append(i // 3)
            if i % 2 == 0: temp.append(i // 2)
    print(count)
