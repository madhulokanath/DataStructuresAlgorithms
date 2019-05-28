#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

#Input:
#11110
#11010
#11000
#00000

#Output: 1

#Input:
#11000
#11000
#00100
#00011

#Output:3

#THis Problem can be solved by bfs
# check for first grid cell which is 1 then traverse, increment count of islands by 1
# traverse through bfs and convert all connected 1 to 0 
# do the same for all other grid cells


def NumberOfIslands(grid):
    count=0
    if grid:
        row=len(grid)                                               #calculate rows
        col=len(grid[0])                                            #calculate columns
        list1=[]                                                    #initialize list which helps to keep track of level in graph
        for i in range(row):                                        #looping through rows
            for j in range(col):                                    # looping through each column under row
                if grid[i][j]==1:                                   # Check if the cell has '1' (atleast one cell with 1 required to count as island)
                    count+=1                                        # Increase the island count by 1
                    print(grid) 
                    grid[i][j]=0                                    #since we calculated the count, change the 1 to 0
                    
                    list1.append([i,j])                             # Append the cell to list to traverse through its neighbours
                    print(list1)
                    while len(list1)>0:                             # the loop runs for all neighbours of the cell
                        x=list1.pop()                               # once processing a cell, pop the cell from list1
                        print(list1)
                        r=x[0]                                      # getting the row from x
                        c=x[1]                                      # getting column from x
                        if r-1>=0 and grid[r-1][c]==1:              # check by miving up if the neighnouring cell is 1
                            print(r-1,c,'up') 
                            list1.append([r-1,c])                   # add the cell to list to traverse
                            grid[r-1][c]=0                          #since this cell is processed convert to 0
                        if r+1<row and grid[r+1][c]==1:             # similarly checking in direction down
                            print(r+1,c,'down')
                            list1.append([r+1,c])
                            grid[r+1][c]=0
                        if c-1>=0 and grid[r][c-1]==1:              # similarly checking in direction left
                            print(r,c-1,'left')
                            list1.append([r,c-1])
                            grid[r][c-1]=0
                        if c+1<col and grid[r][c+1]==1:             # similarly checking in direction right
                            print(r,c+1,'right')
                            list1.append([r,c+1])
                            grid[r][c+1]=0
    return count                                                    # return the islands count.

# This Problem can also be solved by dfs method.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row=len(grid)
        if row==0:
            return 0
        col=len(grid[0])
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,i,j)
        return count
    
    def dfs(self,grid,row,col):
        if grid:
            r=len(grid)
            c=len(grid[0])                
            grid[row][col]='0'

            if row-1>=0 and grid[row-1][col]=='1':
                self.dfs(grid,row-1,col)
            if row+1<r and grid[row+1][col]=='1':
                self.dfs(grid,row+1,col)
            if col-1>=0 and grid[row][col-1]=='1':
                self.dfs(grid,row,col-1)
            if col+1 < c and grid[row][col+1]=='1':
                self.dfs(grid,row,col+1)


#using dfs
