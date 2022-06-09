class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def partition(pivot_idx, left, right):
            pivot_dist = dist(pivot_idx)
            
            # 1. move pivot to end
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            store_idx = left
            
            # 2. move more close elements to the left
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
                    
            # 3. move pivot to its final place
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            
            return store_idx
            
        def quickselect(left, right):
            """
            Sort a list within left..right till kth less close element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return 
            
            # select a random pivot_index
            pivot_idx = randint(left, right)
            
            # find the pivot position in a sorted list
            true_idx = partition(pivot_idx, left, right)
            
            # if the pivot is in its final sorted position
            if true_idx == k:
                return
            
            if true_idx < k:
                # go left
                quickselect(true_idx, right)
            else:
                # go right
                quickselect(left, true_idx)
        
        nums = inorder(root)
        dist = lambda idx : abs(nums[idx] - target) #nice definition of inline function here
        quickselect(0, len(nums) - 1)
        return nums[:k]
