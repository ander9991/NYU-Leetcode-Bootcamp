class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = {}
        for i in nums:
            if i in dict_count:
                dict_count[i] += 1
            else:
                dict_count[i] = 1
        rev_count = {}
        for i in dict_count:
            if dict_count[i] in rev_count:
                rev_count[dict_count[i]].append(i)
            else:
                rev_count[dict_count[i]] = [i]
                
        ans = []
        for c in range(len(nums), -1, -1):
            if c in rev_count:
                ans.extend(rev_count[c])
            if len(ans) >= k:
                return ans[:k]
        return ans[:k]
