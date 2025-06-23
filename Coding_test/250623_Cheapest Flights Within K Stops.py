

import collections
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # visited[node][stops] = 최소비용
        visited = [[float('inf')] * (k + 2) for _ in range(n)]

        # 우선순위 큐: (cost, current_city, remaining_stops)
        heap = [(0, src, 0)]
        visited[src][0] = 0

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            # stop 수가 제한을 넘지 않을 때만 다음 탐색
            if stops <= k:
                for neighbor, price in graph[city]:
                    new_cost = cost + price
                    # 만약 기존보다 더 적은 비용으로 방문 가능하면 진행
                    if new_cost < visited[neighbor][stops + 1]:
                        visited[neighbor][stops + 1] = new_cost
                        heapq.heappush(heap, (new_cost, neighbor, stops + 1))

        return -1
