from random import randint, shuffle


print(6, 2)
print(1, 1, 4, 5, 1, 4)
print()

print(1, 1)
print(1)
print()

an = [10, 100, 1000, 10000, 100000, 200000]
for n in an:
    # 完全随机
    print(n, randint(1, n))
    print(*(randint(1, n) for _ in range(n)))
    print()

    # 无解
    k = randint(1, n)
    print(n, k)
    print(n, *range(1, n))
    print()

    # k 很大倒序满足并且答案为 Yes(hack 暴力和每个元素满足的滚动求错)
    k = randint(n // 2, n)
    opt = list(range(k))
    shuffle(opt)

    print(n, k)
    for i in range(n, 0, -1):
        if opt:
            t = i + opt[-1]
            opt.pop()
            if t > n:
                t -= n
            print(t, end=" ")
        else:
            print(i, end=" ")
    print()
    print()

    # 向左滚动为 Yes 但向右滚动为 No
    k = randint(n // 2, n)
    opt = list(range(k))
    shuffle(opt)

    print(n, k)
    for i in range(n, 0, -1):
        if opt:
            t = i - opt[-1]
            opt.pop()
            if t <= 0:
                t += n
            print(t, end=" ")

        else:
            print(i, end=" ")
    print()
    print()

    # 开头长度不足 k，但后面满足(hack 可以滚动的位置只要有连续的一段 和 总和超过 k 就 Yes)
    k = randint(2, n // 2)
    print(n, k)
    print(*(k - 1 for _ in range(k)), *(k + 1 for _ in range(n - k)))
    print()
