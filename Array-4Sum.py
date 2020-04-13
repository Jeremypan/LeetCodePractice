#Solution 1 - General way of two pointers
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        nums=sorted(nums)
        solution_list=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i-1]==nums[i]:continue #remove case in duplicates
            #turn to 3 sum
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j-1]==nums[j]: continue #remove case in duplicate
                start_index=j+1    
                end_index=len(nums)-1
                while start_index<end_index:
                    sum_ans=nums[i]+nums[j]+nums[start_index]+nums[end_index]
                    if sum_ans==target:
                        solution_list.append([nums[i],nums[j],nums[start_index],nums[end_index]])
                        while start_index<end_index and nums[start_index]==nums[start_index+1]:
                            #delete repeat number
                            start_index+=1
                        while start_index<end_index and nums[end_index-1]==nums[end_index]:
                            end_index-=1
                        start_index+=1
                        end_index-=1
                    elif sum_ans<target:
                        start_index+=1
                    else:
                        end_index-=1
        return solution_list

#Solution 2 - Recursive
class Solution:
    def fourSum(self, nums, target):
            results = []
            nums.sort()
            
            def df(l, r, target, N, result):
                if r-l+1 < N or N < 2:
                    return
                if N == 2:
                    while l < r:
                        s = nums[l] + nums[r]
                        if s == target:
                            results.append(result + [nums[l], nums[r]])
                            l += 1
                            while l < r and nums[l-1] == nums[l]:
                                l += 1
                        elif s < target:
                            l += 1
                        else:
                            r -= 1
                else:
                    for i in range(l, r+1):
                        if i == l or (i > l and nums[i-1] != nums[i]):
                            df(i+1, r, target-nums[i], N-1, result + [nums[i]])
                    
            df(0, len(nums)-1, target, N=4, result=[])
            return results
