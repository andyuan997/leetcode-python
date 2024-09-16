from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])  # 使用不同的變數保存行數和列數

        # Step 1: 初始化，把腐爛橘子的座標加入隊列，並統計新鮮橘子的數量
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    queue.append((x, y))  # 將座標作為元組加入隊列
                elif grid[y][x] == 1:
                    fresh_oranges += 1

        # 如果沒有新鮮橘子，直接返回 0
        if fresh_oranges == 0:
            return 0

        # Step 2: BFS 開始腐蝕橘子
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 上下左右四個方向
        step = 0

        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # 使用 cols 和 rows 來檢查範圍，而不是 x 和 y
                    if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 1:
                        grid[ny][nx] = 2  # 新鮮橘子變腐爛
                        fresh_oranges -= 1
                        queue.append((nx, ny))  # 將新腐爛的橘子座標加入隊列

        # 如果還有新鮮橘子，無法完全腐爛，返回 -1
        return step - 1 if fresh_oranges == 0 else -1


# 測試
solution = Solution()
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
result = solution.orangesRotting(grid=grid)
print(result)
