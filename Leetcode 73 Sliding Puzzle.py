'''

Leetcode 73 Sliding Puzzle

On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
 
Example 1:
        Input: board = [[1,2,3],[4,0,5]]
        Output: 1
        Explanation: Swap the 0 and the 5 in one move.

Example 2:
Input: board = [[1,2,3],[5,4,0]]
        Output: -1
        Explanation: No number of moves will make the board solved.
        
Example 3:        
        Input: board = [[4,1,2],[5,0,3]]
        Output: 5
        Explanation: 5 is the smallest number of moves that solves the board.
        An example path:
                        After move 0: [[4,1,2],[5,0,3]]
                        After move 1: [[4,1,2],[0,5,3]]
                        After move 2: [[0,1,2],[4,5,3]]
                        After move 3: [[1,0,2],[4,5,3]]
                        After move 4: [[1,2,0],[4,5,3]]
                        After move 5: [[1,2,3],[4,5,0]] 

Constraints:
        board.length == 2
        board[i].length == 3
        0 <= board[i][j] <= 5
        Each value board[i][j] is unique.

'''


from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        """
        Solves the 2x3 sliding puzzle problem, finding the fewest number of moves
        to reach the target configuration.

        Parameters:
        board (List[List[int]]): The initial state of the 2x3 board as a list of lists.

        Returns:
        int: The minimum number of moves to solve the puzzle or -1 if it is unsolvable.
        """

        # Define possible swaps for each position of '0'
        directions = [
            [1, 3],     # Swaps for position 0
            [0, 2, 4],  # Swaps for position 1
            [1, 5],     # Swaps for position 2
            [0, 4],     # Swaps for position 3
            [1, 3, 5],  # Swaps for position 4
            [2, 4]      # Swaps for position 5
        ]

        target = "123450"  # Target configuration to achieve
        visited = set()    # Set to track visited board configurations
        queue = deque()    # Queue to perform BFS
        start_state = ""   # Start configuration as a string

        # Convert 2D board to a single string to facilitate easier manipulation
        for row in board:
            for value in row:
                start_state += str(value)

        # Initialize BFS with starting configuration
        queue.append(start_state)
        visited.add(start_state)
        steps = 0

        # Perform BFS to find the minimum number of moves
        while queue:
            level_size = len(queue)

            # Process all nodes at the current level
            for _ in range(level_size):
                current_state = queue.popleft()

                # Check if current configuration matches the target
                if current_state == target:
                    return steps

                zero_index = current_state.find('0')  # Find the position of '0'

                # Generate all possible moves from the current configuration
                for move in directions[zero_index]:
                    next_state = list(current_state)  # Convert current state to list to modify it
                    next_state[zero_index], next_state[move] = next_state[move], next_state[zero_index]
                    next_state_str = ''.join(next_state)  # Convert back to string after swapping

                    # Add new configuration to queue if not visited
                    if next_state_str not in visited:
                        visited.add(next_state_str)
                        queue.append(next_state_str)

            steps += 1  # Increment step count after processing the current level

        # If target configuration is not reached, return -1
        return -1

