import heapq

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = 0
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((self.timer, tweetId))
        self.timer -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        alltweets = [self.tweets[user] for user in self.followees[userId] | {userId}]
        res = list(heapq.merge(*alltweets))[:10]
        return [tweet for timer, tweet in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].discard(followeeId)