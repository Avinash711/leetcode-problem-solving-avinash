import bisect
def jobScheduling(startTime, endTime, profit):
        # sorting the cominations with endtime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda end: end[1])
        print(jobs)
        dp = [[0, 0]]
        for s, e, p in jobs:
            print(s,e,p,"-----")
            #print(bisect.bisect(dp, [s+1]))
            i = bisect.bisect(dp, [s + 1]) - 1
            #print(i,dp,s+1)
            print(i, dp[i][1]+p, dp[-1][1])
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
                print(dp)
        return dp[-1][1]


print(jobScheduling([3,2,3,1], [6,4,5,3], [70,10,40,50]))