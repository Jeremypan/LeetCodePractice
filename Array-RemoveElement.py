#Solution 1 - unecessary to remove the element as the step of remove include copy operation
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
         General verison pointer
        """
        if len(nums)==0:
            return 0
        start=0
        end_size=len(nums)
        while start<end_size:
            if nums[start]==val:
                nums[start]=nums[end_size-1]
                end_size-=1
            else:
                start+=1
        return end_size
#Solution 2 - General Way by two pointers
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
         General verison pointer
        """
        if len(nums)==0:
            return 0
        start=0
        end=len(nums)-1
        while start<=end:
            if nums[start]==val:
                del nums[start]
                end-=1
                continue
            start+=1
        return len(nums)
       
