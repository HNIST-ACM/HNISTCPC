def ilist():
    return list(map(int, input().split()))


def main():
    n, k = ilist()
    assert 1 <= n <= int(2e5)
    assert 1 <= k <= n
    a = ilist()
    assert len(a) == n
    vis = [0]*n
    for i in range(n):
        assert 1 <= a[i] <= n
        vis[(a[i]-i-1+n) % n] = 1

    i = 0
    while i < n and vis[i]:
        i += 1
    print('Yes' if i >= k else 'No')


main()
