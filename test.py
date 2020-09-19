location = [[0,1], [1,5], [2,3]]
B = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(4):
    try:
        nx = x + location[j][0]
        ny = y + location[j][1]
        val += B[nx][ny]
    except IndexError:
        continue