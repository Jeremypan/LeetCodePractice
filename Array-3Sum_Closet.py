#Two pointer (similar to 3 Sum)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #ensure 3 integers in the array
        if len(nums)<=2:
            return []
        nums=sorted(nums)
        solution_list=[]
        distance=float('inf')
        for i in range(len(nums)-2):
            start_index=i+1
            end_index=len(nums)-1
            while start_index<end_index:
                if abs(target-sum([nums[start_index],nums[i],nums[end_index]]))<distance:
                    distance=abs(target-sum([nums[start_index],nums[i],nums[end_index]]))
                    solution_list=[nums[start_index],nums[i],nums[end_index]]
                    if distance==0:
                        return sum(solution_list)
                elif nums[start_index]+nums[i]+nums[end_index]>target:
                    end_index-=1
                else:
                    start_index+=1
        return sum(solution_list)
                
