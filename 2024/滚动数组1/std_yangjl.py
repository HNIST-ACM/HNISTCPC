import math
import calendar
import decimal
import sys
import functools
# list.sort(key=functools.cmp_to_key(lambda a, b: -1 if a<b else 1))
import datetime
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def ilist():
    return list(map(int, input().split()))


def extract(s, sub):
    i = s.find(sub)
    return s[i:i+len(sub)] + s[:i] + s[i+len(sub):]


sys.setrecursionlimit(50000007)  # 递归调用的最大深度，默认只有1000
tt = 1
# tt = int(input())


def main():
    n, k = ilist()
    assert 1 <= n <= int(2e5)
    assert 1 <= k <= n

    a = ilist()
    assert len(a) == n
    for x in a:
        assert 1 <= x <= n

    def check(b):
        for i in range(n):
            if i+1 == b[i]:
                return True
        return False

    ans = 0
    if check(a):
        ans = 1
        if check(a[1:]+a[0:1]) or check(a[n-1:]+a[:n-1]):
            ans = k
    print('Yes' if ans >= k else 'No')


for t in range(tt):
    main()
