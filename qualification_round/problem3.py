t = int(input())
start_x, start_y = 400, 400
size_y = 4
for k in range(t):
    i, j = 10, 10
    a = int(input())
    m = [[0 for i in range(1000)] for j in range(1000)]
    x, y = 400, 400
    while (i != 0 and j != 0):
        while m[x][y] == 0 and  (i != 0 and j != 0):
            if y > start_y + size_y - 2 and (x - start_x + 2) * 5 < a: # 2 right most columns
                print(x + 1, start_y + size_y - 1, flush=True)
            elif (x - start_x + 2) * 5 >= a and not(y > start_y + size_y - 2): # Last 2 rows and not at 2 right most columns
                print(start_x + a // 5 - 1 , y + 1, flush=True)
            elif (x - start_x + 2) * 5 >= a and y > start_y + size_y - 2: # Last 2 rows and at 2 right most columns
                print(start_x + a // 5 - 1, start_y + size_y - 1, flush=True)
            else:
                print(x + 1, y + 1, flush=True) # Else take the diagonal square
            i, j = map(int, input().split(' '))
            m[i][j] = 1
        y += 1
        if y > start_y + size_y:
            y = start_y
            x += 1
