from random import randint


print(6, 2)
print(1, 1, 4, 5, 1, 4)
print()

print(1, 1)
print(1)
print()

an = [10, 100, 1000, 10000, 100000, 200000]
for n in an:
    # k >= 2 纯随机
    print(n, randint(2, n))
    print(*(randint(1, n) for _ in range(n)))
    print()

    # k >= 2 只有第一次滚动可以
    print(n, randint(2, n))
    if randint(0, 1):
        print(*range(1, n + 1))
    else:
        print(*(6 for _ in range(4)), 1, 6, 1, *(6 for _ in range(n - 7)))
    print()

    # k >= 2 只有第二次滚动可以
    print(n, randint(2, n))
    if randint(0, 1):
        print(n, *range(1, n))
    else:
        print(*range(2, n + 1), 1)
    print()

    # k = 1 纯随机
    print(n, 1)
    print(*(randint(1, n) for _ in range(n)))
    print()

    # k = 1 无解
    print(n, 1)
    print(n, *range(1, n))
    print()

    # 最后一个数右移
    print(n, n)
    print(1, 6, 6, *[2] * (n - 4), 1)
    print()

    # 第一个数左移
    print(n, n)
    print(n, 6, 6, *[2] * (n - 4), n)
    print()