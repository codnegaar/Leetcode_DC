'''

Leetcode 3568 Minimum Moves to Clean the Classroom

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

Example 1:
        Input: classroom = ["S.", "XL"], energy = 2
        Output: 2
        Explanation:
        The student starts at cell (0, 0) with 2 units of energy.
        Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
        A valid sequence of moves to collect all litter is as follows:
        Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
        Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
        The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:        
        Input: classroom = ["LS", "RL"], energy = 4        
        Output: 3        
        Explanation:        
        The student starts at cell (0, 1) with 4 units of energy.
        A valid sequence of moves to collect all litter is as follows:
        Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
        Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
        Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
        The student collects all the litter using 3 moves. Thus, the output is 3.
        
Example 3:
          Input: classroom = ["L.S", "RXL"], energy = 3
          Output: -1
          Explanation:
          No valid path collects all 'L'.
          Constraints:
          1 <= m == classroom.length <= 20
          1 <= n == classroom[i].length <= 20
          classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
          1 <= energy <= 50
          There is exactly one 'S' in the grid.
          There are at most 10 'L' cells in the grid.
'''


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n, trash = len(classroom), len(classroom[0]), 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = defaultdict(int)
        grid = [list(row) for row in classroom]

        for row, col in product(range(m), range(n)):

            if grid[row][col] == "L":
                grid[row][col] = str(trash)
                trash += 1

            if grid[row][col] == "S":
                queue = deque([(row, col, energy, 0, 0)])
                visited[(row, col, 0)] = energy

        if trash == 0: return 0

        while queue:
            row, col, fuel, mask, moves = queue.pop()
            moves+= 1                

            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if r < 0 or m <= r or c < 0 or n <= c or grid[r][c] == "X":
                    continue

                if grid[r][c] == 'R':
                    nxtFuel = energy
                else: nxtFuel = fuel - 1    

                if grid[r][c].isnumeric():
                    nxtMask =  mask | (1 << int(grid[r][c]))
                    if nxtMask.bit_count() == trash:
                        return moves
                        
                else: nxtMask = mask

                state = (r, c, nxtMask)
                
                if  visited[state] < nxtFuel:
                    visited[state] = nxtFuel
                    queue.appendleft((r, c, nxtFuel, nxtMask, moves))

        return -1
