class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        length_array = len(gas)
        start_index = len(gas)+1
        tank = 0
        broken = False
        #find start
        for i in range(length_array):
            broken = False
            for j in range(i,length_array):
                if gas[j] >= cost[j]:
                    start_index = j
                    break
            
            if start_index>length_array:
                return -1
            tank = gas[start_index]
            for i in range(length_array):
                
                tank =  tank - cost[(start_index + i) % length_array]
                if tank < 0:
                    tank = 0
                    broken = True
                    break
                tank +=  gas[(start_index + i + 1) % length_array]
            if broken == False: 
                return start_index
        return -1
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
	trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
	for i in range(n):
		trip_tank += gas[i] - cost[i]
		curr_tank += gas[i] - cost[i]
		if curr_tank < 0:
			start = i + 1
			curr_tank = 0 
	return start if trip_tank >= 0 else -1
    """

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

my_solution = Solution()
print(my_solution.canCompleteCircuit(gas, cost))