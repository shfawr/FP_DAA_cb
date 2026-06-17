import random

def generate_maze(size, seed=None):
    """Buat grid size x size dengan dinding (1) dan lantai (0), pastikan semua terhubung."""
    if seed is not None:
        random.seed(seed)

    grid = [[1 for _ in range(size)] for _ in range(size)]   # 1 = wall
    start_r, start_c = random.randint(0, size-1), random.randint(0, size-1)
    grid[start_r][start_c] = 0   # floor

    stack = [(start_r, start_c)]
    while stack:
        r, c = stack[-1]
        neighbors = []
        for dr, dc in [(-2,0),(2,0),(0,-2),(0,2)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 1:
                neighbors.append((nr, nc, dr//2, dc//2))
        if neighbors:
            nr, nc, wr, wc = random.choice(neighbors)
            grid[r+wr][c+wc] = 0   # buka tembok di antara
            grid[nr][nc] = 0
            stack.append((nr, nc))
        else:
            stack.pop()

    # (Opsional) tambahkan beberapa jalan acak agar tidak terlalu koridor
    return grid