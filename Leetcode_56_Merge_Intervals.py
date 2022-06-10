class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastIntervalEnd = output[-1][1]
            if start <= lastIntervalEnd:
                output[-1][1] = max(lastIntervalEnd , end)
            else:
                output.append([start, end])
        return output
      
  '''
# Second solution 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
	if intervals ==[]:
	return []
	sorted = []

	intervals.sort() # sort the inrvals
	for intrval in intervals:
		if sorted == [] or sorted[-1][1] < interval[0]:
			sorted.append(interval)
		else: 
			sorted[-1][1] = max(sorted[-1][1], interval[1])	
''''	
	

      
      
      
