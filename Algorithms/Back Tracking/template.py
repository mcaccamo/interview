#https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
            
            
  # example:
  
  class Solution:
    def totalNQueens(self, n):
      
      ###Backtracking:
        def backtrack(row, diagonals, anti_diagonals, cols):
            # Base case - N queens have been placed
            if row == n:
                return 1

            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols 
                      or curr_diagonal in diagonals 
                      or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                # Move on to the next row with the updated board state
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

            return solutions

          #### End backtracking
        return backtrack(0, set(), set(), set())
    
    
    
    
    ##############################################################################################################
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res= []
    candidates.sort()
    
    def backtrack(i, tempSum, tempList, res):
        if tempSum > target:
            return
        if tempSum == target:
            res.append(tempList[:])
            return
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]: continue
            tempList.append(candidates[j])
            backtrack(j+1, tempSum+candidates[j], tempList, res)
            tempList.pop()
            
    backtrack(0, 0, [], res)
    return res
    ##############################################################################################################
