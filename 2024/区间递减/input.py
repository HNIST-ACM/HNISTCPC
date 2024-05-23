# 使用指南：https://github.com/luogu-dev/cyaron/wiki/%E5%9B%BE-Graph
from cyaron import *
import os


def writeln(fo, *args, sep=' ', end='\n'):
    ans = ''
    flag = 0
    for x in args:
        if flag:
            ans += sep
        else:
            flag = 1
        ans += str(x)
    ans += end
    fo.write(ans)


def main():
    if not os.access("./data/", os.F_OK):
        os.makedirs("./data/")

    # 4.in 2e5~1
    for i in range(4, 4 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[n-i for i in range(n)])
            for i in range(q):
                writeln(fo, 1, n)

    # return

    # 3.in 1~2e5
    for i in range(3, 3 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[i+1 for i in range(n)])
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 16 倒金字塔: 1e5 ~ 2,1 ~ 1e5+1
    for i in range(16, 16 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[i for i in range(int(1e5), 1, -1)], end=' ')
            writeln(fo, *[i+1 for i in range(int(1e5)+1)])
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 15 金字塔: 1 ~ 1e5+1 ~ 2
    for i in range(15, 15 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[i+1 for i in range(int(1e5)+1)], end=' ')
            writeln(fo, *[i for i in range(int(1e5), 1, -1)])
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 14 循环降: 100,99,98,97, ...
    for i in range(14, 14 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[100 - i % 100 for i in range(n)])
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 13 循环升: 1,2,..,99,100, ...
    for i in range(13, 13 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[i % 100+1 for i in range(n)])
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 12 升降升降: 1,2,..,99,100,101,100,99,98,..,2,  ...
    for i in range(12, 12 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            a = []
            for i in range(n):
                t = i % 200
                a.append(t+1 if t < 101 else 101-(t-100))
            writeln(fo, *a)
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 11 升降升降: 1,2,1,2,..
    for i in range(11, 11 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n, q = int(2e5), int(2e5)
            writeln(fo, n, q)
            writeln(fo, *[i % 2+1 for i in range(n)])
            for i in range(q):
                writeln(fo, 1, n)
    return

    # 5-10 random
    for i in range(5, 10 + 1):
        with open('./data/'+str(i)+'.in', 'w') as fo:
            n = randint(1, 2e5)
            q = randint(1, 2e5)
            writeln(fo, n, q)
            writeln(fo, *[randint(1, 1e9) for i in range(n)])
            for i in range(q):
                l = randint(1, n)
                r = randint(l, n)
                writeln(fo, l, r)
    return


main()
