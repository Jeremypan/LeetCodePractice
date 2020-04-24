
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        start=0
        permutation=list()
        for i in range(m):
            start=start+1
            permutation.append(start)
        result=[]
        for index_number in queries:
            query=permutation.index(index_number)
            result.append(query)
            permutation=[permutation.pop(query)]+permutation
        return result