class Twitter:

    def __init__(self):
        self.user_tweets : dict[int, list] = {}
        self.user_followers : dict[int, set] = {} # follower : followees
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.user_tweets:
            self.user_tweets[userId] = [(self.time, tweetId)]
        else:
            self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        lsts = []
        if userId in self.user_tweets:
            lsts.append(self.user_tweets[userId])
        if userId in self.user_followers:
            followees = self.user_followers[userId]
            for followee in followees:
                lsts.append(self.user_tweets[followee])
        
        mostRecentTweets = []
        for i, tweets in enumerate(lsts):
            if not tweets:
                continue
            tweet = tweets[-1]
            tweet_cpy = (-tweet[0], tweet[1])
            heapq.heappush(mostRecentTweets, (tweet_cpy, i, len(tweets)-1))
        
        res = []
        while mostRecentTweets and len(res) < 10:
            (time, tweetId), lst_index, elem_index = heapq.heappop(mostRecentTweets)
            res.append(tweetId)
            if elem_index > 0:
                next_idx = elem_index - 1
                nextTweet = lsts[lst_index][next_idx]
                nextTweetCpy = (-nextTweet[0], nextTweet[1])
                heapq.heappush(mostRecentTweets, (nextTweetCpy, lst_index, next_idx))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 

        if followerId not in self.user_followers:
            self.user_followers[followerId] = {followeeId}
        else:
            self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
            
        if followerId not in self.user_followers:
            return
        if followeeId not in self.user_followers[followerId]:
            return
        self.user_followers[followerId].remove(followeeId)
