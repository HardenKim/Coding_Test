import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]

if len(a) > r-1 and len(a[0]) > c-1:
    if a[r-1][c-1] == k:
        print(0)
        sys.exit()

ans = 1
while ans <= 100:
    next_a, max_len, is_transpose = [], 0, 0
    if len(a) < len(a[0]):
        a = [list(x) for x in zip(*a)]
        is_transpose = 1

    for row in a:
        maxn = max(row)
        cnt = [0 for _ in range(maxn+1)]
        temp_row = []
        for v in row:
            if v > 0:
                cnt[v] += 1
        for index, key in enumerate(cnt):
            if key:
                temp_row.append([key, index])
        temp_row.sort()
        temp_row2 = []
        for l in temp_row:
            temp_row2.extend([l[1], l[0]])
        next_a.append(temp_row2)
        max_len = max(max_len, len(temp_row2))

    for row in next_a:
        if len(row) < max_len:
            z = [0 for _ in range(max_len - len(row))]
            row.extend(z)
    a = next_a

    if is_transpose:
        a = [list(x) for x in zip(*a)]

    if len(a) > r-1 and len(a[0]) > c-1:
        if a[r-1][c-1] == k:
            print(ans)
            sys.exit()
    ans += 1
print(-1)