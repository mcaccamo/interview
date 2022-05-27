#<template?

#https://leetcode.com/problems/fruit-into-baskets
def totalFruit(self, fruits: List[int]) -> int:
    if not fruits:
        return -1
    fruitCounts = collections.defaultdict(int)
    l = r = 0
    res = float('-inf')
    for r in range(len(fruits)):
        fruitCounts[fruits[r]]+=1
        while l < r and len(fruitCounts) > 2:
            fruitCounts[fruits[l]]-=1
            if fruitCounts[fruits[l]] == 0:
                del fruitCounts[fruits[l]]
            l+=1
        res = max(res, r-l+1)
    return res
        
