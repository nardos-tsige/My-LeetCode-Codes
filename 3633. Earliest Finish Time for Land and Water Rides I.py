class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], 
                          waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                #order 1: land first, then water
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(waterStartTime[j], land_finish)
                water_finish = water_start + waterDuration[j]
                finish_time1 = water_finish
                #order 2: water first, then land
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(landStartTime[i], water_finish)
                land_finish = land_start + landDuration[i]
                finish_time2 = land_finish
                
                min_finish = min(min_finish, finish_time1, finish_time2)
        
        return min_finish
