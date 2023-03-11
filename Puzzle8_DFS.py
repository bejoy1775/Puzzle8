import copy

# Method to determine if the state is in goal state
def is_goal(state):
    end_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    return state == end_state

# This method takes input of a state and previous state.
# It returns all possible child states with possible moves
def action(state, prev_state):
    result = []
    moves = []

    # This method is used to swap two input tiles within a state for a specified move
    def swap(new_state, tile1, tile2, move):
        new_state = new_state.copy()
        temp = new_state[tile1]
        new_state[tile1] = new_state[tile2]
        new_state[tile2] = temp
        result.append(new_state)
        moves.append(move)

    # Identify the blank tile as the tile with value = 0
    current_blank_tile = state.index(0)

    # Determine the previous position of the blank tile
    if len(prev_state) == 0:
        previous_blank_tile = current_blank_tile
    else:
        previous_blank_tile = prev_state.index(0)

    # Following logic determines all possible moves allowed with following rules
    # - Only allowed moves are up, down, left and right
    # - Blank tile does not move back to the tile where it came from
    # - Blank tiles on four corners does not move out of the 3 by 3 range
    # - Blank tiles on left columns, right columns, top row and bottom rows does not move out of the 3 by 3 range
    left_move = current_blank_tile - 1
    right_move = current_blank_tile + 1
    up_move = current_blank_tile - 3
    down_move = current_blank_tile + 3

    if (left_move in range(0, 9)) & (left_move != previous_blank_tile):
        swap(state, current_blank_tile, left_move, 'L')

    if (right_move in range(0, 9)) & (right_move != previous_blank_tile):
        swap(state, current_blank_tile, right_move, 'R')

    if (up_move in range(0, 9)) & (up_move != previous_blank_tile):
        swap(state, current_blank_tile, up_move, 'U')

    if (down_move in range(0, 9)) & (down_move != previous_blank_tile):
        swap(state, current_blank_tile, down_move, 'D')

    return moves, result

# recursive method that takes node and limit as input
def recursive_dfs(node, limit):

    # check state to if its goal state, if yes return solution
    if is_goal(node[0]):
        return node[1]
    # else check if we reached cutoff limit
    elif limit == 0:
        return cutoff
    else:
        cutoff_occurred = False

        # call action to determine child nodes and corresponding moves
        temp1, temp2 = action(node[0], node[2])
        for move, child in zip(temp1, temp2):
            child_node = copy.deepcopy(node)
            child_node[0] = child
            child_node[1].append(move)
            child_node[2] = node[0]

            # for each child again call recursive to generate its child nodes.
            # This ensures that we keep going deeper in the tree first.
            result = recursive_dfs(child_node, limit - 1)

            # in each recursion, look at result for cutoff
            if result == cutoff:
                cutoff_occurred = True
            elif result != failure:
                return result

        # at this point we are either at cutoff or we got a failure
        if cutoff_occurred:
            return cutoff
        else:
            return failure

# Main method to execute DFS algorithim, takes probelm and limit as input
def dfs_search(problem, limit):

    previous_state = []
    moves = []
    node = [problem, moves, previous_state]

    # Builds the initial node with problem, moves and previous status to call recursive fundtion.
    return recursive_dfs(node, limit)

# Used to represent cutoff
cutoff = ['cutoff']

# Used to represent failure
failure = ['failure']

# Used a depth limit of 10 for test here
limit = 12

#  Following are test cases for testing the BFS for different kind of inputs

# Already solved input
problem1 = [ 1, 2, 3, 8, 0, 4, 7, 6, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your DFS Solution is with following moves {0}".format(dfs_search(problem1, limit)))

# Solvable in depth of 1
problem1 = [ 1, 0, 3, 8, 2, 4, 7, 6, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your DFS Solution is with following moves {0}".format(dfs_search(problem1, limit)))

# Solvable in 6 moves
problem1 = [ 1, 3, 4, 8, 0, 5, 7, 2, 6]
print("\n Problem input is: {0}".format(problem1))
print("Your DFS  Solution is with following moves {0}".format(dfs_search(problem1, limit)))

# Another problem solvable in 6 moves
problem1 = [1, 3, 4, 8, 6, 2, 0, 7, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your DFS Solution is with following moves {0}".format(dfs_search(problem1, limit)))

# Solvable in 11 moves
problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your DFS Solution is with following moves {0}".format(dfs_search(problem1, limit)))

# Iff solution exists beyond the depth limit, expect a cutoff response
problem1 = [6, 8, 7, 2, 5, 4, 3, 0, 1]
print("\n Problem input is: {0}".format(problem1))
print("Your DFS Solution is with following moves {0}".format(dfs_search(problem1, limit)))