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
    n, m, V = ilist()
    assert 1 <= n <= 200
    assert 1 <= m <= 200
    assert 1 <= V <= 200

    v = [int(input()) for i in range(n)]
    for x in v:
        assert 1 <= x <= 200

    v.sort()
    # print(v)

    dp = [-1]*(V+1)
    dp[0] = 0
    ans = -1
    for x in v:
        if x <= V and dp[V-x] != -1:
            ans = max(ans, dp[V-x]+1+x*m)
            # print(x, ans)

        for i in range(V, x-1, -1):
            if dp[i-x] != -1:
                dp[i] = max(dp[i], dp[i-x]+1)
    print(ans)


for t in range(tt):
    main()
