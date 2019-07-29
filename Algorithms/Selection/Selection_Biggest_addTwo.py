k = int(input())
row = list(int(x) for x in input().split())
row.sort()
count = 0 # 찾은 유효 조합의 수 저장.
neg, over = None, None
for i in range(len(row)):
    if row[i] >= 0:
        neg = i-1 # neg는 음수범위 종결 표지자.
        break
for i in range(len(row)):
    if row[i] > k:
        over = i #over 는 k값 초과 범위시작 표지자.
        break
# 이제 row[0]~row[neg] 는 음수, row[over]~는 k값 초과.
# (1) 음수 범위와 k값 초과 범위에서의 두 수를 조합함으로 k를 만들 수 있다.
# (2) 사이 범위는 0 이상 k이하이다.    

if (neg and over):
    for i in range(0, neg+1): #(1)
        for j in range(over, len(row)):
            if row[i]+row[j] == k: count+=1
if not over: over = len(row)
for i in range(neg+1, over): #(2)
    for j in range(i+1,over):
        if row[i]+row[j] == k: count+=1
print(count)
