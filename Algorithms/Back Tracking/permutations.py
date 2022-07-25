class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, seen, out, curr):
            if len(curr) == len(nums):
                out.append(curr)
            for i, num in enumerate(nums):
                if i not in seen:
                    seen.add(i)
                    backtrack(nums, seen, out, curr + [num])
                    seen.remove(i)
        seen = set()
        out = []
        backtrack(nums, seen, out, [])
        return out
        


        
class Solution:
    def permuteDiffWay(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, seen, out, curr):
            if len(curr) == len(nums):
                out.append(curr[:])
            for i, num in enumerate(nums):
                if i not in seen:
                    seen.add(i)
                    curr.append(num)
                    backtrack(nums, seen, out, curr)
                    curr.pop()
                    seen.remove(i)
        seen = set()
        out = []
        backtrack(nums, seen, out, [])
        return out
        

