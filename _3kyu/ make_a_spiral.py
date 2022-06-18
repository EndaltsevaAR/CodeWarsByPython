"""Description:
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given
size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself."""


def spiralize(size):
    spiral = [[0] * size for i in range(size)]
    min_column = 0
    max_column = size - 1
    min_row = 0
    max_row = size - 1
    while min_row <= max_row:
        for x in range(min_column, max_column + 1):
            spiral[min_row][x] = 1
        for y in range(min_row, max_row + 1):
            spiral[y][max_column] = 1
        if min_row != 0:
            min_column += 1
        if max_row - 1 == min_row:
            break
        for reverse_x in range(max_column - 1, min_column - 1, -1):
            spiral[max_row][reverse_x] = 1
        for reverse_y in range(max_row - 1, min_row + 1, -1):
            spiral[reverse_y][min_column] = 1
        min_column += 1
        max_column -= 2
        min_row += 2
        max_row -= 2
    return spiral

test_array = spiralize(5)
for row in test_array:
    for element in row:
        print(element, end=' ')
    print()
