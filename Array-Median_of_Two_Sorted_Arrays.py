#Solution 1 - Binary Search to find Kth Num in two Array - 基本思路写的
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #find Kth Num in two array
        def findKthNum(nums1,left1,nums2,left2,k):
            if left1>=len(nums1):
                return nums2[left2+k-1]
            if left2>=len(nums2):
                return nums1[left1+k-1]
            if k==1:
                return min(nums1[left1],nums2[left2])
            #mid1=left1+k/2-1 确保mid比array1的长度小，该array 还能用
            mid1=nums1[left1+(k//2)-1] if (left1+(k//2)-1)<len(nums1) else float('inf')
            
            #mid1=left2+k/2-1 确保mid比array2的长度小，该array 还能用
            mid2=nums2[left2+(k//2)-1] if (left2+(k//2)-1)<len(nums2) else float('inf')
          
            # 二进制搜索 如果左边小就删左边
            if mid1<=mid2:
                return findKthNum(nums1,left1+(k//2),nums2,left2,k-(k//2))
            return findKthNum(nums1,left1,nums2,left2+(k//2),k-(k//2))
        total_len=len(nums1)+len(nums2)
        if total_len%2==0:
            
            return (findKthNum(nums1,0,nums2,0,(total_len//2))+findKthNum(nums1,0,nums2,0,(total_len//2)+1))/2
        else:
            return findKthNum(nums1,0,nums2,0,(total_len+1)//2)

#Solution 2 - 更有效的方法 - 参考了大佬的想法
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1=len(nums1)
        N2=len(nums2)
        if N1>N2:
            return self.findMedianSortedArrays(nums2,nums1)
        if N1==0:
            return (nums2[(N2-1)//2]+nums2[N2//2])/2
        size=N1+N2
        cutL,cutR=0,N1
        cut1=N1//2
        cut2=size//2-cut1
        while cut1<=N1:
            cut1 = (cutR-cutL)//2+cutL
            cut2 = size//2-cut1
            L1 = float('-inf') if cut1==0 else nums1[cut1-1]
            L2 = float('-inf') if cut2==0 else nums2[cut2-1]
            R1 = float('inf') if cut1==N1 else nums1[cut1]
            R2 = float('inf') if cut2==N2 else nums2[cut2]
            if L1>R2:
                cutR = cut1 - 1
            elif L2>R1:
                cutL = cut1 + 1
            else:
                if size%2==0:
                    L1 = L1 if L1>L2 else L2
                    R1 = R1 if R1<R2 else R2
                    return (L1+R1)/2
                else:
                    R1 = R1 if R1<R2 else R2
                    return R1
        return -1

