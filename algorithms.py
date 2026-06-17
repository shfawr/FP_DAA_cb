from collections import deque
import heapq

def get_neighbors(grid, r, c, forbidden=None):
    """4-neighbor, kembalikan list (nr, nc) yang walkable (bukan WALL)."""
    neighbors = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != 1:   # asumsi 1 = WALL, sesuaikan dengan definisi di settings
                neighbors.append((nr, nc))
    return neighbors

def bfs(grid, start, goal):
    """Kembalikan (path, expanded_nodes). Path = list of cells dari start ke goal."""
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    came_from = {start: None}
    expanded = 0

    while queue:
        cur = queue.popleft()
        expanded += 1
        if cur == goal:
            break
        for nb in get_neighbors(grid, cur[0], cur[1]):
            if nb not in came_from:
                came_from[nb] = cur
                queue.append(nb)

    if goal not in came_from:
        return [], expanded

    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path, expanded

def astar(grid, start, goal):
    """Kembalikan (path, expanded_nodes)."""
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    expanded = 0

    while open_set:
        _, cur = heapq.heappop(open_set)
        expanded += 1
        if cur == goal:
            path = []
            while cur != start:
                path.append(cur)
                cur = came_from[cur]
            path.reverse()
            return path, expanded

        for nb in get_neighbors(grid, cur[0], cur[1]):
            tentative_g = g_score[cur] + 1
            if nb not in g_score or tentative_g < g_score[nb]:
                came_from[nb] = cur
                g_score[nb] = tentative_g
                f_score[nb] = tentative_g + heuristic(nb, goal)
                heapq.heappush(open_set, (f_score[nb], nb))

    return [], expanded