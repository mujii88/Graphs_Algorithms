
import heapq
from collections import defaultdict
from sortedcontainers import SortedSet
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self,V, edges,source):

        adj=defaultdict(list)

        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))

        res=[float('inf')]*V
        heap=[]
        res[source]=0

        heapq.heappush(heap,(0,source))
        while heap:
            dist,node=heapq.heappop(heap)

            for child in adj[node]:
                nde,wt=child
                if dist+wt<res[nde]:
                    res[nde]=dist+wt
                    heapq.heappush(heap,(dist+wt,nde))

        return res



# Dijkstra Algorithm using Set

    def dijkstra2(self,V, edges,source):

        adj=defaultdict(list)

        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))

        res=[float('inf')]*V
        
        res[source]=0

        seen=SortedSet()
        seen.add((0,source))
        while seen:
            dist,node=seen.pop(0)

            for child in adj[node]:
                nde,wt=child
                if dist+wt<res[nde]:
                    if res[nde]!=float('inf'):
                        seen.remove((res[nde],nde))
                    res[nde]=dist+wt
                    seen.add((dist+wt,nde))

        return res

A=Solution()
print(A.dijkstra(5,[[0,1,2],[0,4,6],[1,2,3],[1,3,8],[1,4,5],[2,3,1],[3,4,2]],0))
print(A.dijkstra2(5,[[0,1,2],[0,4,6],[1,2,3],[1,3,8],[1,4,5],[2,3,1],[3,4,2]],0))
