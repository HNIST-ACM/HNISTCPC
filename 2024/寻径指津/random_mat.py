import random


def generate_random_matrix(maxn):
    # 随机生成 n 和 m
    n = random.randint(2, maxn)
    m = random.randint(2, maxn)

    # 创建一个 n*m 的矩阵，随机填充 '.' 或 '#'
    grid = [[('.', '#')[random.randint(0, 1000) % 5 == 0]
             for _ in range(m)] for _ in range(n)]

    # 找到所有的 '.' 位置
    empty_positions = [(i, j) for i in range(n)
                       for j in range(m) if grid[i][j] == '.']

    # 随机选择两个不同的 '.' 位置设置为 'S' 和 'T'
    if len(empty_positions) >= 2:
        start, end = random.sample(empty_positions, 2)
        grid[start[0]][start[1]] = 'S'
        grid[end[0]][end[1]] = 'T'
    else:
        print("没有足够的 '.' 来放置 'S' 和 'T'")
        assert 0

    return grid, n, m


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def save_grid_to_file(grid, filename):
    with open(filename, 'w') as file:
        file.write(' '.join([str(len(grid)), str(len(grid[0]))]) + '\n')
        for row in grid:
            file.write(''.join(row) + '\n')


# 生成随机矩阵并打印
pref = './data0/'
# for i in range(5, 10+1):
#     grid, n, m = generate_random_matrix(50)
#     save_grid_to_file(grid, pref+str(i)+'xx.in')
for i in range(16, 20+1):
    grid, n, m = generate_random_matrix(1000)
    save_grid_to_file(grid, pref+str(i)+'xx.in')
