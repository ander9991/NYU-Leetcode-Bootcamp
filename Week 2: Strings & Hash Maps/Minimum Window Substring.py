class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.defaultdict(int)
        for c in t:
            count_t[c] -= 1 

        n_found = -len(t)
        minString, minLen = "", len(s)
        l, r = 0, 0 

        while r < len(s):
            if s[r] in count_t:
                if count_t[s[r]] < 0:
                    n_found += 1
                count_t[s[r]] += 1

            if n_found == 0: 
                while True:
                    if s[l] in count_t:
                        count_t[s[l]] -= 1
                        if count_t[s[l]] < 0:
                            n_found -= 1
                            break
                    l += 1
                substring = s[l:r+1]
                l += 1
                if r-l < minLen:
                    minString, minLen = substring, r-l
            r += 1       
        return minString
