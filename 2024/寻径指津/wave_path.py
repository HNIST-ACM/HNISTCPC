def create_wave_path(rows, cols):
    # 创建一个空的网格
    grid = [['.' for _ in range(cols)] for _ in range(rows)]

    # 遍历每一列
    for col in range(cols):
        if col % 2 == 1:  # 对于奇数列
            for row in range(rows):
                grid[row][col] = '#'  # 默认填充 '#'
            if col % 4 == 1:
                grid[rows - 1][col] = '.'  # i%4 == 1，最下面的位置缺失
            elif col % 4 == 3:
                grid[0][col] = '.'  # i%4 == 3，最上面的位置缺失

    # 设置起点和终点
    grid[0][0] = 'S'  # 起点
    grid[rows - 1][cols - 1] = 'T'  # 终点

    return grid


def save_grid_to_file(grid, filename):
    with open(filename, 'w') as file:
        file.write(' '.join([str(len(grid)), str(len(grid[0]))]) + '\n')
        for row in grid:
            file.write(''.join(row) + '\n')


# 设置网格大小
rows, cols = 9, 10  # 可以根据需要调整大小
wave_path = create_wave_path(rows, cols)
save_grid_to_file(wave_path, 'wave_path.in')

'''
.#...
.#.#.
.#.#.
.#.#.
...#.
'''
