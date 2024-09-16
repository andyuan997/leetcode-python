from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # 將deadends轉為集合，方便快速查找
        dead_set = set(deadends)
        # 如果初始狀態就在deadends中，直接返回-1
        if "0000" in dead_set:
            return -1

        # 初始化BFS的隊列和已訪問集合
        queue = deque([("0000", 0)])  # 初始狀態是"0000"，步數為0
        visited = set("0000")  # 記錄已訪問過的組合，避免重複訪問

        while queue:
            current, steps = queue.popleft()

            # 如果當前組合等於目標組合，返回步數
            if current == target:
                return steps

            # 嘗試對鎖的四個轉盤進行操作
            for i in range(4):
                # 對第 i 個轉盤，向上轉和向下轉
                for direction in [-1, 1]:
                    # 取出第i位的數字，將其轉為新的數字
                    new_digit = (int(current[i]) + direction) % 10
                    # 生成新的組合
                    new_combination = current[:i] + str(new_digit) + current[i + 1:]

                    # 如果新組合不在deadends且沒被訪問過，加入隊列
                    if new_combination not in dead_set and new_combination not in visited:
                        queue.append((new_combination, steps + 1))
                        visited.add(new_combination)

        # 如果無法達到目標，返回-1
        return -1
