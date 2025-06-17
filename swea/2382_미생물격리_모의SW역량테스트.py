dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
r_dir = [0, 2, 1, 4, 3]
 
T = int(input())
 
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
     
    #상: 1, 하: 2, 좌: 3, 우: 4
    for _ in range(m):
        for d in data:
            d[0] = d[0] + dr[d[3]]
            d[1] = d[1] + dc[d[3]]
             
        for i in range(len(data)):
            if data[i][0] == 0 or data[i][0] == n-1 or data[i][1] == 0 or data[i][1] == n-1:
                data[i][2] //= 2
                data[i][3] = r_dir[data[i][3]]
         
        data.sort(key=lambda x : (x[0], x[1], x[2]), reverse=True)
        c = 1
        while c < len(data):
            if data[c-1][0:2] == data[c][0:2]:
                data[c-1][2] += data[c][2]
                data.pop(c)
            else:
                c += 1
     
     
    for d in data:
        ans += d[2]
         
    print(f'#{tc} {ans}')