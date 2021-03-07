def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                print([hash_table[target - num], i])
                break    # 看到有人在這加了break, 理論上不會執行到, 但時間卻會比較短
            hash_table[num] = i
        return([])

# Driver Code
num_arr = [2, 7, 11, 15]
pair_sum = 9    
  
# Calling function
twoSum(num_arr, pair_sum)
