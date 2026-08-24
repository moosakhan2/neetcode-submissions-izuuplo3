import heapq
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        def h(state):
            total = 0
            for i in range(4):
                d = abs(int(state[i]) - int(target[i]))
                total += min(d, 10 - d)
            return total

        def neighbors(state):
            for i in range(4):
                d = int(state[i])
                for move in (1, -1):
                    nd = (d + move) % 10
                    yield state[:i] + str(nd) + state[i+1:]

        start = "0000"
        pq = [(h(start), 0, start)]        # (f = g + h, g, state)
        best_g = {start: 0}

        while pq:
            f, g, state = heapq.heappop(pq)
            if state == target:
                return g
            if g > best_g.get(state, float("inf")):
                continue                    # stale heap entry, skip
            for nxt in neighbors(state):
                if nxt in dead:
                    continue
                ng = g + 1
                if ng < best_g.get(nxt, float("inf")):
                    best_g[nxt] = ng
                    heapq.heappush(pq, (ng + h(nxt), ng, nxt))

        return -1