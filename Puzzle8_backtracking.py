
def isEnd(state):
    endState = [1,2,3,8,0,4,7,6,5]
    return state == endState

def succAndCost(state, prevState):
    result = []

    def swap(tile1, tile2, action):
        temp = state[tile1]
        state[tile1] = state[tile2]
        state[tile2] = temp
        result.append((action, state, 1))

    currentBlankTile = state.index(0)

    if prevState == None:
        previousBlankTile = currentBlankTile
    else:
        previousBlankTile = prevState.index(0)

    leftMove = currentBlankTile - 1
    rightMove = currentBlankTile + 1
    upMove = currentBlankTile - 3
    downMove = currentBlankTile + 3

    if (leftMove == range(0,8)) & (leftMove != previousBlankTile):
        swap(currentBlankTile, leftMove, 'L')

    if (rightMove == range(0,8)) & (rightMove != previousBlankTile):
        swap(currentBlankTile, rightMove, 'R')

    if (upMove == range(0,8)) & (upMove != previousBlankTile):
        swap(currentBlankTile, upMove, 'U')

    if (downMove == range(0,8)) & (downMove != previousBlankTile):
        swap(currentBlankTile, downMove, 'D')

    return result

def dynamicProgramming(problem, previousState):
    cache = {} # state -> futureCost(state)

    def futureCost(state):
        # Base case
        if isEnd(state):
            return 0
        # if state in cache: # Exponential savings
        #     return cache[state]
        # Actually doing work
        result = min(cost+futureCost(newState) for action, newState, cost in succAndCost(state, previousState))
        cache[state] = result
        previousState = state
        return result
    return futureCost(problem)

previousState = []
problem = [ 3, 1, 4, 8, 0, 5, 7, 2, 6]
dynamicProgramming(problem, previousState)











