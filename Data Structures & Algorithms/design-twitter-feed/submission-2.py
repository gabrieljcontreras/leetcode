import heapq
import collections
class Twitter:
    def __init__(self):
        self.time = 0 
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []

        all_users = self.following[userId] | {userId}

        for u in all_users:
            if self.tweets[u]:
                last_index = len(self.tweets[u]) - 1
                neg_time, tweetId = self.tweets[u][last_index]
                heapq.heappush(min_heap,(neg_time, tweetId, u, last_index))

        while min_heap and len(res) < 10: 
            neg_time, tweetId, userId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index > 0:
                next_neg_time, next_tweetId = self.tweets[userId][index - 1]
                heapq.heappush(min_heap, (next_neg_time, next_tweetId, userId, index - 1))
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
