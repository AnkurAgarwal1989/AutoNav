# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
grid = [[0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]]
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

path = []

def getNextOpenSpaces(grid, current):
    #print "Curr: ", current
    nextOpen = []
    grid[current[0]][current[1]] = 'c'
    for i in range(len(delta_name)):
        #get next space that will be reached from motion
        nextSpace = [current[0] + delta[i][0], current[1] + delta[i][1], current[2] + cost]
        #if we fall out of bounds...this is not a vlid move...try next move
        if (nextSpace[0] > len(grid)-1 or nextSpace[1] > len(grid[0])-1 or nextSpace[0] < 0 or nextSpace[1] < 0):
            #print "Wrong move: ", nextSpace
            continue
        #see if space is already marked or obstacle
        #if(grid[nextSpace[0]][nextSpace[1]] == 1 or grid[nextSpace[0]][nextSpace[1]] == 'c'):
            #print "Obstacle at: ", nextSpace
        if(grid[nextSpace[0]][nextSpace[1]] == 0):
            #print "Next Space at: ", nextSpace
            grid[nextSpace[0]][nextSpace[1]] = 'c'
            nextOpen.append(nextSpace)
    #print nextOpen
    return nextOpen
    

def search(grid,initial,goal,cost):
    print initial
    initial.append(0)
    path.append(initial)
    goalReached = False
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    #cost = 0;
    #nextSpaces = getNextOpenSpaces(grid, init)
    best = [0, 0, 99999]
    for p in path:
        #print p
        if (p[0] == goal[0] and p[1] == goal[1]):
            goalReached = True
            if p[2] < best[2]:
                best = p
            #print "Goal reached"
            continue
        nextSpaces = getNextOpenSpaces(grid, p)
        for nextSpace in nextSpaces:
            path.append(nextSpace)
        #print path
        #print grid
    if goalReached:
        return [best[2], best[0], best[1]]
    else:
        return "fail"
    #return path
print search(grid, init, goal, cost)
