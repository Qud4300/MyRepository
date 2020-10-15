# BOJ 2004 zeros in combination
def find_five(n):
    res = 0
    while n != 0:
        res += n // 5
        n //= 5
    return res


def find_two(n):
    res = 0
    while n != 0:
        res += n // 2
        n //= 2
    return res


n, m = map(int, input().split())
print(
    min(
        find_two(n) - find_two(n - m) - find_two(m),
        find_five(n) - find_five(n - m) - find_five(m)
    )
)
