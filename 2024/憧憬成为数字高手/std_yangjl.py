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


sys.setrecursionlimit(50000007)  # 递归调用的最大深度，默认只有1000
tt = 1
# tt = int(input())


def main():
    N = int(1e5)
    f = [0]*(N+1)
    for i in range(1, N+1):
        f[i] += 1
        for j in range(i+i, N+1, i):
            f[j] += f[i]
    n = int(input())
    a = ilist()
    assert 1 <= n <= int(1e5)
    assert len(a) == n
    for x in a:
        assert 1 <= x <= int(1e5)
        print(f[x], end=' ', flush=False)


for t in range(tt):
    main()
