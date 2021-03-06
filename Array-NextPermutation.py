#Solution 1 - O(2n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        
            
        
        #1st step - find the first number not in the descending line
        first_number=float("-inf")
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                first_number=i
                break        
        #2nd step - condition if it cannot find the first number
        if  first_number==float('-inf'):
            nums.reverse()
        else:
            first_larger=float("inf")
            #3rd step - find the first number larger than the first_number
            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[first_number]:
                    first_larger=i
                    break
            #4th step - swap and reverse
            temp=nums[first_number]
            nums[first_number]=nums[first_larger]
            nums[first_larger]=temp
            nums[first_number+1:]=reversed(nums[first_number+1:])