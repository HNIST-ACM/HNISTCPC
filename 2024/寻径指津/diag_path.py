def save_grid_to_file(grid, filename):
    with open(filename, 'w') as file:
        file.write(' '.join([str(len(grid)), str(len(grid[0]))]) + '\n')
        for row in grid:
            file.write(''.join(row) + '\n')


# 创建一个空的网格
n, m = 904, 904
# n, m = 10, 10
grid = [['#' for _ in range(m+2)] for _ in range(n+2)]

for i in range(n):
    a = []
    if i == 0:
        a = list('...#') + list('....##')*m
    elif i % 6 == 1 or i % 6 == 4:
        a = list('..#') + list('..#')*m
    elif i % 6 == 2:
        a = list('.#') + list('..#')*m
    elif i % 6 == 3:
        a = list('...#') + list('..#')*m
    elif i % 6 == 5:
        a = list('##') + list('..#')*m
    else:
        a = list('#') + list('..#')*m
    while len(a) > m:
        a.pop()
    a = list('#')+a+list('#')
    grid[i+1] = a

i = n
f = 1
for j in range(1, m+1):
    if grid[i][j] == '#':
        f = 1 - f
        if f:
            grid[i][j] = '.'

j = m
f = 1
for i in range(1, n+1):
    if grid[i][j] == '#':
        f ^= 1
        if f:
            grid[i][j] = '.'
grid[1][1] = 'S'
grid[n][m] = 'T'
save_grid_to_file(grid, './data/diag_path900.in')
