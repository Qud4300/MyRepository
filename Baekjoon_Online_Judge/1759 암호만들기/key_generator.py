# BOJ 1759 암호만들기
from itertools import combinations as comb

L, C = map(int, input().split())
s = set(input().split())
consonants = set()
vowels = set()
excepts = set()
for i in s:
    if i in ('a', 'e', 'i', 'o', 'u'):
        vowels.update(i)
    else:
        consonants.update(i)

if C-len(vowels) >= L:  # case : not having any vowels
    for case in list(comb(consonants, L)):
        excepts.add(tuple(sorted(case)))
if len(vowels) + 1 >= L:
    for c in consonants:  # case : having only 1 consonant
        for case in list(comb(vowels, L-1)):
            excepts.add(tuple(sorted(set(case).union({c}))))
if len(vowels) >= L:  # case : not having any consonant
    for case in list(comb(vowels, L)):
        excepts.add(tuple(sorted(case)))

total = set()
for case in comb(s, L):
    total.add(tuple(sorted(case)))
res = list(total-excepts)

for i in range(len(res)):
    res[i] = list(res[i])
    res[i].sort()

for i in sorted(res):
    print(*i, sep='')
