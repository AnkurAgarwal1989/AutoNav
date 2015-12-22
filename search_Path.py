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
from pprint import PrettyPrinter

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

'''grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]'''
grid = [[0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0]]
'''grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]'''
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
expand = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
path = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
action = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
print expand
print path
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def getNextOpenSpaces(grid, current, cost, time):
    #print "CurrExp: ", exp
    nextOpen = []
    grid[current[1]][current[2]] = 'c'
    expand[current[1]][current[2]] = time
    
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
            #expand[nextSpace[1]][nextSpace[2]] = nextSpace[0]
            nextOpen.append(nextSpace)
            
            #action required to get to new space from current space
            action[nextSpace[1]][nextSpace[2]] = i
    #print nextOpen
    return nextOpen

#go back from goal..at each step...we already have the action that got us to that place.
def findPath(grid):
    current = goal
    path[current[0]][current[1]] = '*'
    minCost = expand[current[0]][current[1]]
    #minCost = grid[current[0]][current[1]]
    while (current[0] > 0 or current[1] > 0):
        act = action[current[0]][current[1]]
        prevSpace_x = current[0] - delta[act][0]
        prevSpace_y = current[1] - delta[act][1]
        path[prevSpace_x][prevSpace_y] = delta_name[action[current[0]][current[1]]]
        current = [prevSpace_x, prevSpace_y]
    return path
            

def prettyPrint(x):
    for i in x:
        print i

def search(grid,initial,goal,cost):
    
    begin = [0, initial[0], initial[1]] #cost, y, x
    
    expandStep = 0;
    
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
    result = 'Fail'
    
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
                #continue
            nextOpen = getNextOpenSpaces(grid, nextStep, cost, expandStep)
            expandStep += 1
            for space in nextOpen:
                openSpaces.append(space)
    
    prettyPrint(action)
    if result is not "Fail":
        prettyPrint(findPath(grid))
    return result
    
    #while: no solution found
        #if nothing more and no goal reached...quit and say fail
        
        #else see nextOpenSpaces
            #sort in descending order of cost the list of spaces we have. pick(pop) the first(smallest cost).
            # append spaces available from this spot
            

print search(grid, init, goal, cost)
prettyPrint(expand)
prettyPrint(grid)
