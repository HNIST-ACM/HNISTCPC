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
    n, m = ilist()
    assert 1 <= n <= int(2e5)
    assert 1 <= m <= int(2e5)
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    assert 1 <= sum(len(x) for x in s) <= int(2e5)
    assert 1 <= sum(len(x) for x in t) <= int(2e5)
    r = [(i+1) % n for i in range(n)]
    l = [(i+n-1) % n for i in range(n)]

    vis = [0]*n
    p = 0
    cnt = 0
    for x in t:
        cnt += 1
        if x == s[p]:
            if cnt == 1:
                vis[p] = 1
                if r[p] == p:
                    break
                else:
                    r[l[p]] = r[p]
                    l[r[p]] = l[p]
                    p = r[p]
            else:
                p = r[p]
            cnt = 0

    for i in range(n):
        if vis[i]:
            print(s[i])


for t in range(tt):
    main()
