import heapq

class Solution:
    def trapRainWater(self, heightMap) -> int:
        
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        q = []

        for i in range(n):
            for j in [0, m-1]:
                heapq.heappush(q, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        for i in range(m):
            for j in [0, n-1]:
                if not visited[j][i]:
                    heapq.heappush(q, (heightMap[j][i], j, i))
                    visited[j][i] = True
            
        output = 0
        maxheight = -1

        dirc = [[0,1],[0,-1],[1,0],[-1,0]]

        while q:
            wall, x, y = heapq.heappop(q)
            maxheight = max(maxheight, wall)
            for i, j in dirc:
                newx = x + i
                newy = y + j
                if 0 <= newx < n and 0 <= newy < m and not visited[newx][newy]:
                    visited[newx][newy] = True
                    if heightMap[newx][newy] < maxheight:
                        output += wall - heightMap[newx][newy]
                    
                    heapq.heappush(q, (max(heightMap[newx][newy], wall), newx, newy))
                
        return output
        

