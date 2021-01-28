# BOJ Lost Parenthesis
res = []
for sep in input().split('-'):
    res.append(sum([*map(int, sep.split('+'))]))
print(res[0]-sum(res[1:]))

#res = [sum([*map(int, sep.split('+'))]) for sep in input().split('-')]
#print(res[0]-sum(res[1:]))