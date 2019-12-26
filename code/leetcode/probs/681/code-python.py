// Increment by Time O(1), O(1)
class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        cur = 60*int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ":"}
        while True:
            cur = (cur + 1) % (24*60)
            if all(digit in allowed 
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

// Increment by Combinations O(1), O(1)
class Solution:
    def nextClosestTime(self, time: str) -> str:
        hr, ms = time.split(":")
        ans = start = int(hr)*60 + int(ms)
        elapsed = 24*60
        st = {int(x) for x in time if x != ":"}
        # print(st)
        for h1 in st:
            for h2 in st:
                for m1 in st:
                    for m2 in st:
                        hr, ms  = 10*h1 + h2, 10*m1 + m2
                        if hr < 24 and ms < 60:
                            cur = hr*60 + ms
                            cand_elapsed = (cur - start) % (24*60)
                            if 0 < cand_elapsed < elapsed:
                                ans = cur
                                elapsed = cand_elapsed
        return "{:02d}:{:02d}".format(*divmod(ans, 60))

// Initial Solution Used Sorting, not optimal...
// Combination is few so performance is okay but bad overral.

class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        digit_set = set()
        for ch in time.replace(":", ""):
            digit_set.add(ch)
        m = time.index(":")   # I thought the given time could be in "1:13" format
        timeList = list(time)
        if m == 1:
            timeList.insert(m, "0")
        if len(time) - m - 1 == 1:
            timeList.insert(m+1, "0")
        time = "".join(timeList)
            
        
        res = [i+j+":"+k+l for i in digit_set \
                            for j in digit_set \
                            for k in digit_set \
                            for l in digit_set \
                            if "0" <= i+j <="23" and "0" <= k+l <= "59"]
        res.sort()
        for el in res:
            if el > time:
                return el
        else:
            return res[0]