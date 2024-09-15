class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != start_color:
                return

            image[r][c] = color

            dfs(r + 1, c)  # 向下
            dfs(r - 1, c)  # 向上
            dfs(r, c + 1)  # 向右
            dfs(r, c - 1)  # 向左

        dfs(sr, sc)
        return image
