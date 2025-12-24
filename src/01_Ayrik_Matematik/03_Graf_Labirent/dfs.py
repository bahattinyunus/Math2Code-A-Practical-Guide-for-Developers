import heapq

def solve_maze_astar(maze, start, end):
    """
    A* Algoritması ile labirent çözümü.
    F(n) = G(n) + H(n)
    G(n): Başlangıçtan maliyet
    H(n): Hedefe tahmini uzaklık (Manhattan)
    """
    rows, cols = len(maze), len(maze[0])
    
    # Priority Queue: (F-score, (row, col))
    pq = []
    heapq.heappush(pq, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    while pq:
        current_f, current_node = heapq.heappop(pq)
        
        if current_node == end:
            return reconstruct_path(came_from, end)
        
        row, col = current_node
        
        # 4 yön: Yukarı, Aşağı, Sol, Sağ
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        
        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0:
                # Hareket maliyeti her zaman 1 varsayalım
                tentative_g = g_score[current_node] + 1
                
                if (r, c) not in g_score or tentative_g < g_score[(r, c)]:
                    came_from[(r, c)] = current_node
                    g_score[(r, c)] = tentative_g
                    h_score = abs(r - end[0]) + abs(c - end[1]) # Manhattan Distance
                    f_score = tentative_g + h_score
                    heapq.heappush(pq, (f_score, (r, c)))
                    
    return None # Yol bulunamadı

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

if __name__ == "__main__":
    # 0: Yol, 1: Duvar
    maze_grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)
    end_pos = (4, 4)
    
    print("Labirent Çözülüyor (A*)...")
    path = solve_maze_astar(maze_grid, start_pos, end_pos)
    
    if path:
        print("Yol Bulundu:", path)
        # Görselleştirme (Basit ASCII)
        for r in range(len(maze_grid)):
            line = ""
            for c in range(len(maze_grid[0])):
                if (r, c) in path:
                    line += "*"
                elif maze_grid[r][c] == 1:
                    line += "#"
                else:
                    line += "."
            print(line)
    else:
        print("Yol Yok!")
