def prison(n, m, h, v): 
    global ROW, COL 
      
    # row number is in range, column number is in  
    # range and value is 1 and not yet visited  
    return ((m >= 0) and (m < ROW) and
            (h >= 0) and (h < COL) and 
            (n[m][h] and not v[m][h])) 
  
# A utility function to do DFS for a 2D  
# boolean matrix. It only considers  
# the 8 neighbours as adjacent vertices  
def DFS(n, m, h, v, count): 
      
    # These arrays are used to get row and column  
    # numbers of 8 neighbours of a given cell  
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]  
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]  
  
    # Mark this cell as visited  
    v[m][h] = True
  
    # Recur for all connected neighbours  
    for k in range(8): 
        if (prison(n, m + rowNbr[k],  
                   h + colNbr[k], v)): 
                         
            # increment region length by one  
            count[0] += 1
            DFS(n, m + rowNbr[k],  
                h + colNbr[k], v, count) 
  
# The main function that returns largest 
# length region of a given boolean 2D matrix  
def largestRegion(n): 
    global ROW, COL 
      
    # Make a bool array to mark visited cells.  
    # Initially all cells are unvisited  
    v = [[0] * COL for i in range(ROW)] 
  
    # Initialize result as 0 and travesle  
    # through the all cells of given matrix  
    result = -999999999999
    for i in range(ROW): 
        for j in range(COL): 
              
            # If a cell with value 1 is not  
            if (n[i][j] and not v[i][j]): 
                  
                # visited yet, then new region found  
                count = [1]  
                DFS(n, i, j, v, count)  
  
                # maximum region  
                result = max(result, count[0]) 
    return result 
  
# Driver Code 
ROW = 4
COL = 5
  
n = [[0, 0, 1, 1, 0], 
     [1, 0, 1, 1, 0],  
     [0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 1]]  
  
print(largestRegion(n)) 
