# BOJ 10816 숫자카드 2
import sys

input = sys.stdin.readline
n = int(input())
cards = sorted([*map(int, input().split())])
m = int(input())
keys = [*map(int, input().split())]


def check(key, start, end):
    if end-start<1:
        return int(bool(key == cards[start]))
    mid = (start + end) // 2
    if key != cards[mid]:
        if key < cards[mid]:
            end = max(mid - 1, start)
        else:
            start = min(mid + 1, end)
        return check(key, start, end)
    else:
        key_start = start
        key_end = end
        while cards[key_start] != key and key_start < mid:
            key_start += 1
        while cards[key_end] != key and key_end > mid:
            key_end -= 1
        return key_end - key_start + 1


res = ""
for key in keys:
    res += str(check(key, 0, len(cards)-1)) + " "
print(res.strip())
