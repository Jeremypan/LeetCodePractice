class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        keep=[0]*len(A)
        swap=[0]*len(B)
        swap[0]=1
        for i in range(1,len(A)):
            keep[i]=swap[i]=0x7fffffff
            if A[i]>A[i-1] and B[i]>B[i-1]:
                # if keep, no need to swap here
                keep[i]=keep[i-1]
                # if swap, swap need to do one more time
                swap[i]=swap[i-1]+1
            if A[i]>B[i-1] and B[i]>A[i-1]: 
                """
                    if the sequence do not fit the first if condition, it has to swap
                    if the sequence fit the first if condition, it needs to choose the short path
                """
                keep[i]=min(swap[i-1],keep[i]) #the first 
                swap[i]=min(swap[i],keep[i-1]+1)
        return min(keep[-1],swap[-1])