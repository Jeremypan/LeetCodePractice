#Solution - Unecessary to delete
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        len_num=0
        for i in range(1,len(nums)):
            if nums[i]==nums[len_num]:
                continue
            len_num+=1
            nums[len_num]=nums[i]
        return len_num+1 #记得加一