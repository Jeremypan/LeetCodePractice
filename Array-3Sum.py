#Solution 1 - two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #special case
        if len(nums)<=2:
            return []
        nums=sorted(nums) #用于sorted array
        #unique triplets
        #initialize the solution list
        solution=[]
        for i in range(len(nums)-2):#至少有三个不同element 被pointed
            if i>0 and nums[i]==nums[i-1]:
                #删除重复的数字
                continue
            start_pointer=i+1
            end_pointer=len(nums)-1
            sum_ans=0-nums[i]
            #array中的每不重复的数字都进行搜索 通过pointer 找出相关答案存入solution
            while start_pointer<end_pointer:
                if nums[start_pointer]+nums[end_pointer]==sum_ans:
                    solution.append([nums[start_pointer],nums[i],nums[end_pointer]])
                    while (start_pointer<end_pointer) and nums[start_pointer]==nums[start_pointer+1]:
                        #搜索中跳过相同的数字
                        start_pointer+=1
                    while (start_pointer<end_pointer) and nums[end_pointer]==nums[end_pointer-1]:
                        #搜索中跳过相同的数字
                        end_pointer-=1
                    #找到结果后进行move on
                    start_pointer+=1
                    end_pointer-=1
                elif nums[start_pointer]+nums[end_pointer]<sum_ans:
                    #小于目标 start pointer 往前走
                    start_pointer+=1
                else:
                    #大于目标 end pointer 往回走
                    end_pointer-=1     
        return solution
#Solution 2  - Recursive Way - More Efficient (turn to find target in K Sum)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
results=[]
        nums=sorted(nums)
        def dfs(l,r,target,N,result):
            if r-l+1<N or N<2:
                return 
            if N==2:
                while l < r:
                    s=nums[l]+nums[r]
                    if s==target:
                        results.append(result+[nums[l],nums[r]])
                        l +=1
                        while l<r and nums[l-1]==nums[l]:
                            l+=1
                    elif s<target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(l,r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        dfs(i+1,r,target-nums[i],N-1,result+[nums[i]])
        dfs(0,len(nums)-1,0,N=3,result=[])
        return results