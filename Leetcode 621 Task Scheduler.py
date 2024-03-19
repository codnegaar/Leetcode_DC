'''

Leetcode 621 Task Scheduler

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. 
Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
​Return the minimum number of intervals required to complete all tasks.
 

Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
        After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, 
        so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
        Input: tasks = ["A","C","A","B","D","B"], n = 1
        Output: 6
        Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
        With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
        Input: tasks = ["A","A","A", "B","B","B"], n = 3
        Output: 10
        Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
        There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
        1 <= tasks.length <= 104
        tasks[i] is an uppercase English letter.
        0 <= n <= 100

'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
          STRATEGY
          Greedy; schedule the n most common in round-robin fashion.
          The "n most common" adjusts as "time" progresses.
          If there are fewer than n distinct tasks in todo, pad to n with idle states.

          QUEUING METHOD
          A Counter is a dictionary, with extensions like the convenient constructor
          below and most_common(). We'll be using our Counter as a priority queue.
        '''
        todo = Counter(tasks)
        units = 0                   # "Time" units
        n += 1                      # Actual cycle length is more convenient
        while todo:
            # Pick the n items with highest count
            ready = todo.most_common(n)
            n_ready = len(ready)
            units += n_ready
            for k, _ in ready:
                if todo[k] > 1:
                    todo[k] -= 1
                else:
                    del todo[k]     # Would go to 0; delete
            if todo:
                # Fill in with idle time as needed
                units += n - n_ready
        return units
