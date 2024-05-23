def generate_spiral_path(n):
    # 创建一个空的网格
    grid = [[' ' for _ in range(n)] for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右, 下, 左, 上
    dir_index = 0  # 初始方向向右
    x, y = 0, 0  # 起始位置
    grid[x][y] = 'S'  # 起点

    step = 1  # 步数
    while True:
        # 尝试向当前方向移动
        while True:
            next_x = x + directions[dir_index][0]
            next_y = y + directions[dir_index][1]

            # 检查前方是否有两次即将碰到的路径
            twice_next_x = x + 2 * directions[dir_index][0]
            twice_next_y = y + 2 * directions[dir_index][1]
            if (0 <= twice_next_x < n and 0 <= twice_next_y < n and grid[twice_next_x][twice_next_y] != ' '):
                # 设置障碍物并拐弯
                next_x = x + directions[dir_index][0]
                next_y = y + directions[dir_index][1]
                if 0 <= next_x < n and 0 <= next_y < n:
                    grid[next_x][next_y] = '#'
                break

            # 检查是否撞墙或撞到已走过的路径
            if not (0 <= next_x < n and 0 <= next_y < n) or grid[next_x][next_y] != ' ':
                break  # 需要拐弯

            x, y = next_x, next_y
            grid[x][y] = '.'
            step += 1

        # 更改方向（顺时针拐弯）
        dir_index = (dir_index + 1) % 4
        next_x = x + directions[dir_index][0]
        next_y = y + directions[dir_index][1]
        if not (0 <= next_x < n and 0 <= next_y < n) or grid[next_x][next_y] != ' ':
            break  # 如果即使拐弯也无法继续走，就结束

    grid[x][y] = 'T'  # 终点
    return grid


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def save_grid_to_file(grid, filename):
    with open(filename, 'w') as file:
        file.write(' '.join([str(len(grid)), str(len(grid[0]))]) + '\n')
        for row in grid:
            file.write(''.join(row) + '\n')


# 设置螺旋网格的大小
size = 900  # 可以根据需要调整大小
spiral_grid = generate_spiral_path(size)
for i in range(size):
    for j in range(size):
        if spiral_grid[i][j] == ' ':
            spiral_grid[i][j] = '.'
save_grid_to_file(spiral_grid, 'spiral_grid900.in')

'''
S.....
#####.
....#.
.#T.#.
.####.
......
'''
