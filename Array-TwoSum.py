class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        k=0
        for num in nums:
            if target-num in hash_table:
                return [hash_table[target-num],k]
                break #理论上不执行 为啥会快？
            hash_table[num]=k
            k+=1
        return -1
            