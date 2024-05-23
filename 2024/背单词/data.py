from random import choice, choices, randint
from string import ascii_lowercase


print("""3 6
abandon
makabaka
waibibabo
abandom
abandon
wuxidixi
makabaka
waibibabo
abandon
""")

maxv = int(2e5)


def rdm(s: str):
    k = randint(0, len(s) - 1)
    c = choice(ascii_lowercase)
    while c == s[k]:
        c = choice(ascii_lowercase)
    return s[:k] + c + s[k + 1:]


# 完全随机
an = [10, 100, 1000, 10000, 100000, 200000]
for n in an:
    for _ in range(2):
        sz = min(n, maxv // n)
        m = maxv // sz

        s = ["".join(choices(ascii_lowercase, k=sz)) for _ in range(n)]

        print(n, m)
        print(*s, sep='\n')
        i = j = 0
        while j < m:
            while j < m:
                j += 1
                if randint(0, 1):
                    print(s[i])
                    break
                else:
                    k = randint(0, sz - 1)
                    print(rdm(s[i]))

            i = (i + 1) % n

        print()

# 标记的单词不会再拼写
for _ in range(10):
    n = sz = 50
    m = maxv // sz

    s = ["".join(choices(ascii_lowercase, k=sz)) for _ in range(n)]
    t = s.copy()

    print(n, m)
    print(*s, sep='\n')
    i = j = 0
    while j < m:
        cnt = 0
        while j < m:
            cnt += 1
            j += 1
            if randint(0, 1):
                print(s[i])
                break
            else:
                k = randint(0, sz - 1)
                print(rdm(s[i]))

        if cnt == 1:
            s.pop(i)
            if not s:
                break
        else:
            i += 1
        i %= len(s)

    while j < m:
        j += 1
        print(t[i])
        i = (i + 1) % n

    print()

# 第一遍将除了两端的单词标记，然后一直不标记两端的单词，卡 n^2 暴力
for _ in range(5):
    n = int(1e5)
    sz = 1
    m = maxv // sz

    s = ["".join(choices(ascii_lowercase, k=sz)) for _ in range(n)]

    print(n, m)
    print(*s, sep='\n')

    j = 0
    print(rdm(s[0]))
    print(s[0])
    j += 1
    for i in range(1, n - 1):
        print(s[i])
        j += 1
    print(rdm(s[-1]))
    print(s[-1])
    j += 1

    while j < m:
        print(rdm(s[0]))
        print(s[0])
        print(rdm(s[-1]))
        print(s[-1])
        j += 2

    print()