import copy


def is_goal(state):
    end_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    return state == end_state


def action(state, prev_state):
    result = []
    moves = []

    def swap(new_state, tile1, tile2, move):
        new_state = new_state.copy()
        temp = new_state[tile1]
        new_state[tile1] = new_state[tile2]
        new_state[tile2] = temp
        result.append(new_state)
        moves.append(move)

    current_blank_tile = state.index(0)

    if len(prev_state) == 0:
        previous_blank_tile = current_blank_tile
    else:
        previous_blank_tile = prev_state.index(0)

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



def recursive_dfs(node, limit):

    if is_goal(node[0]):
        return node[1]
    elif limit == 0:
        return cutoff
    else:
        cutoff_occurred = False

        temp1, temp2 = action(node[0], node[2])
        for move, child in zip(temp1, temp2):
            child_node = copy.deepcopy(node)
            child_node[0] = child
            child_node[1].append(move)
            child_node[2] = node[0]

            result = recursive_dfs(child_node, limit - 1)

            if result == cutoff:
                cutoff_occurred = True
            elif result != failure:
                return result

        if cutoff_occurred:
            return cutoff
        else:
            return failure

def dfs_search(problem, limit):

    previous_state = []
    moves = []
    node = [problem, moves, previous_state]

    return recursive_dfs(node, limit)

def iterative_df_search(problem):

    for limit in range(0,40):
        result =  dfs_search(problem, limit)
        if result != cutoff:
            return result


# Input format
# e.g. if we have an input of following
#  1 2 3
#  8 0 4
#  7 6 5
# the input is represented as a list as [ 1, 2, 3, 8, 0, 4, 7, 6, 5]

# Used to represent cutoff
cutoff = ['cutoff']

# Used to represent failure
failure = ['failure']

#  Following are test cases for testing the BFS for different kind of inputs

# Already solved input
problem1 = [ 1, 2, 3, 8, 0, 4, 7, 6, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(iterative_df_search(problem1)))

# Solvable in depth of 1
problem1 = [ 1, 0, 3, 8, 2, 4, 7, 6, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(iterative_df_search(problem1)))

# Solvable in 6 moves
problem1 = [ 1, 3, 4, 8, 0, 5, 7, 2, 6]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS  Solution is with following moves {0}".format(iterative_df_search(problem1)))

# Another problem solvable in 6 moves
problem1 = [1, 3, 4, 8, 6, 2, 0, 7, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(iterative_df_search(problem1)))

# Solvable in 11 moves
problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(iterative_df_search(problem1)))

print("Your Solution is with following moves {0}".format(iterative_df_search(problem1)))
