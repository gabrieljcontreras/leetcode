import heapq
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)

        time = 0
        queue = collections.deque()

        while heap or queue: 
            time += 1

            if heap: 
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                cnt, available_time = queue.popleft()
                heapq.heappush(heap, cnt)

        return time