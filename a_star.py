

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
        
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], 
         [ 0, -1], 
         [ 1, 0 ], 
         [ 0, 1 ]] 

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))] 
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    prevs = [[None for row in range(len(grid[0]))] for col in range(len(grid))]
   
    x = init[0]
    y = init[1]
    
    g = 0
    f = g + heuristic[x][y]

    open = [[f, g, x, y]]

    found = False  
    resign = False 
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            f = next[0]
            g = next[1]
            x = next[2]
            y = next[3]
            
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            
            else:

                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            prevs[x2][y2] = [x,y,delta_name[i]]
                            g2 = g + cost
                            f2 = g2 + heuristic[x2][y2]
                            open.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x][y] = 1
   
    for i in range(len(expand)):
        print expand[i]

    print ("\n")
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    x = goal[0]
    y = goal[1]
    path[x][y] = '*'
    
    while prevs[x][y]:
        p = prevs[x][y]
        path[p[0]][p[1]] = p[2]
        x = p[0]
        y = p[1]
    return path 


for line in search(grid,init,goal,cost):
    print line
