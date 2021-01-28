c = int(input())
for i in range(c):
    count = 1
    score = 0
    In = input()
    for j in range(len(In)):
        if In[j] == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)