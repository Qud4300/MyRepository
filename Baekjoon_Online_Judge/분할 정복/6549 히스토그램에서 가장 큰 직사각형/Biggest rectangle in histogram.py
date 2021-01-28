# BOJ 6549 Biggest rectangle in histogram
import sys

input = sys.stdin.readline
arr = []


def biggest(left, right):
    global arr
    if right == left:
        return arr[left]
    mid = (left + right) // 2
    mid_l, mid_r = (left + right) // 2, (left + right) // 2 + 1
    cur_height = min(arr[mid_l], arr[mid_r])
    cur_area = cur_height * 2
    while mid_l > left or mid_r < right:
        if left < mid_l and (mid_r == right or arr[mid_l - 1] > arr[mid_r + 1]):
            mid_l -= 1
            cur_height = min(cur_height, arr[mid_l])
        elif mid_r < right:
            mid_r += 1
            cur_height = min(cur_height, arr[mid_r])
        cur_area = max(cur_area, cur_height * (mid_r - mid_l + 1))
    return max(biggest(left, mid), biggest(mid + 1, right), cur_area)


res = ""
while True:
    n, *arr = map(int, input().rstrip().split())
    if n == 0:
        break
    res += str(biggest(0, len(arr) - 1)) + '\n'
print(res)
