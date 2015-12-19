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

'''grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
grid = [[0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]]'''
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
expand = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
print expand
        
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

path = []

def getNextOpenSpaces(grid, current, cost):
    #print "CurrExp: ", exp
    nextOpen = []
    grid[current[1]][current[2]] = 'c'
    for i in range(len(delta_name)):
        #get next space that will be reached from motion
        nextSpace = [current[0] + cost, current[1] + delta[i][0], current[2] + delta[i][1]]
        #if we fall out of bounds...this is not a vlid move...try next move
        if (nextSpace[1] > len(grid)-1 or nextSpace[2] > len(grid[0])-1 or nextSpace[1] < 0 or nextSpace[2] < 0):
            #print "Wrong move: ", nextSpace
            continue
        #see if space is already marked or obstacle
        #if(grid[nextSpace[0]][nextSpace[1]] == 1 or grid[nextSpace[0]][nextSpace[1]] == 'c'):
            #print "Obstacle at: ", nextSpace
        if(grid[nextSpace[1]][nextSpace[2]] == 0):
            #print "Next Space at: ", nextSpace
            grid[nextSpace[1]][nextSpace[2]] = 'c'
            expand[nextSpace[1]][nextSpace[2]] = nextSpace[0]
            nextOpen.append(nextSpace)
    #print nextOpen
    return nextOpen
    

def search(grid,initial,goal,cost):
    #print "exp: ", exp
    #print initial
    begin = [0, initial[0], initial[1]] #cost, y, x
    expand[0][0] = 0
    #path.append(begin)
    goalReached = False
    failed = False
    
    openSpaces = []
    openSpaces.append(begin)
    #print openSpaces
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    #cost = 0;
    #nextSpaces = getNextOpenSpaces(grid, init)
    
    while goalReached is False and failed is False:
        if len(openSpaces) == 0:
            failed = True
            result = 'Fail'
        
        else:
            openSpaces.sort(reverse=True)
            #print openSpaces
            nextStep = openSpaces.pop()
            if (nextStep[1] == goal[0] and nextStep[2] == goal[1]):
                goalReached = True;
                result = nextStep
                continue
            nextOpen = getNextOpenSpaces(grid, nextStep, cost)
            for space in nextOpen:
                openSpaces.append(space)
    return result
    
    #while: no solution found
        #if nothing more and no goal reached...quit and say fail
        
        #else see nextOpenSpaces
            #sort in descending order of cost the list of spaces we have. pick(pop) the first(smallest cost).
            # append spaces available from this spot
            
    '''best = [0, 0, 99999]
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
        return "fail"'''
    #return path


print search(grid, init, goal, cost)
print expand
