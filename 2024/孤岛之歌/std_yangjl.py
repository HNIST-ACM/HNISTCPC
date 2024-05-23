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
    n = int(input())
    a = ilist()
    if sum(a) & 1:
        print(-1)
    else:
        print(sum([x % 2 == 0 for x in a]) + sum([x % 2 == 1 for x in a])//2)


for t in range(tt):
    main()
