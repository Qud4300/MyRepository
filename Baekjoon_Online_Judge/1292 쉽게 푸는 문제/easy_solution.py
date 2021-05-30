# BOJ 1292 쉽게 푸는 문제
a, b = map(int, input().split())

count = 0
seq = 1
arr = [0]
while count < b:
    arr += [seq]*seq
    count += seq
    seq += 1

print(sum(arr[a:b+1]))
