import copy
from itertools import combinations
from collections import deque

def virus_bfs(copy_data):
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and copy_data[nr][nc] == 0:
                copy_data[nr][nc] = 2
                q.append((nr, nc))

    return sum(row.count(0) for row in copy_data)


n, m = map(int, input().split())
data = []
empty = []
virus = []
mx = 0

for i in range(n):
    row = list(map(int, input().split()))
    data.append(row)
    for j in range(m):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))

for walls in combinations(empty, 3):
    copy_data = copy.deepcopy(data)
    
    for r, c in walls:
        copy_data[r][c] = 1
    
    area = virus_bfs(copy_data)
    mx = max(mx, area)

print(mx)