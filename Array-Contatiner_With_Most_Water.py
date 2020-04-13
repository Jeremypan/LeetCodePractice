#Solution- two pointers Easy!!
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==0 or len(height)==1:
            return 0
        if len(height)==2:
            return min(height[0],height[1])*1
        start_index=0
        end_index=len(height)-1
        max_container_size=0
        while start_index<=end_index:
            water_size=(end_index-start_index)*min(height[start_index],height[end_index])
            if water_size>max_container_size:
                max_container_size=water_size
            if height[start_index]>=height[end_index]:
                end_index-=1
            else:
                start_index+=1
        return max_container_size
        
