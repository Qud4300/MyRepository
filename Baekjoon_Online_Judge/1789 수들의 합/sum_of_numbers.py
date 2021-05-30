# BOJ 1789 수들의 합
s = int(input())
count = 0
seq = 1
while count + seq <= s:
    count += seq
    seq += 1
print(seq-1)
