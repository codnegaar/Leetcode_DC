class Solution {
    public int minPathSum(int[][] grid) {
        
        int r = grid.length; // length of rows
        int c = grid[0].length; // length of columns
        
        for (int i = 0; i<r; i++){
           for (int j = 0; j<c; j++){
                if(i==0 && j==0){
                    continue;
                }
                else if (i == 0 && j !=0){
                    grid[i][j] = grid[i][j] + grid[i][j-1];
                }
                else if (i != 0 && j ==0){
                    grid[i][j] = grid[i][j] + grid[i-1][j]; 
            }
            else{
                grid[i][j] = Math.min( grid[i][j-1] , grid[i-1][j]) + grid[i][j];
            }                
        }
     }
       return grid[r-1][c-1];                    
  }
}      
