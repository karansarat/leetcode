class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        array_sum = 0
        
        local_min_sum, global_min_sum = 0, float('inf')
        local_max_sum, global_max_sum = 0, float('-inf')
        
        for number in A:
            
            local_min_sum = min(local_min_sum + number, number )
            global_min_sum = min(global_min_sum, local_min_sum )
            
            local_max_sum = max(local_max_sum + number, number )
            global_max_sum = max(global_max_sum, local_max_sum )
            
            array_sum += number

        if global_max_sum > 0:
            return max(array_sum - global_min_sum, global_max_sum )
        else:
            return global_max_sum