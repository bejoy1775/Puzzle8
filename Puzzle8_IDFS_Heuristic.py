import copy
import time


def is_goal(state):
    return state == end_state

def calculate_heuristic(state1):

    return len([i for i, x in enumerate(zip(state1,end_state)) if x[0]!=x[1]])

def action(state, prev_state):

    result1 = []

    def swap(new_state, tile1, tile2, move):
        new_state = new_state.copy()
        temp = new_state[tile1]
        new_state[tile1] = new_state[tile2]
        new_state[tile2] = temp
        temp1 = []
        temp1.append(new_state)
        temp1.append(move)
        temp1.append(calculate_heuristic(new_state))
        result1.append(temp1)

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

    result2 = sorted(result1, key=lambda x: x[2])

    return result2



def recursive_dfs(node, limit):

    if is_goal(node[0]):
        return node[1]
    elif limit == 0:
        return cutoff
    else:
        cutoff_occurred = False

        for child, move, factor in action(node[0], node[2]):
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
        print(limit)
        if result != cutoff:
            return result



# Already solved input
# problem1 = [ 1, 2, 3, 8, 0, 4, 7, 6, 5]
# Solvable in depth of 1
# problem1 = [ 1, 0, 3, 8, 2, 4, 7, 6, 5]
# Solvable in 6 moves
# problem1 = [ 1, 3, 4, 8, 0, 5, 7, 2, 6]
# problem1 = [1, 3, 4, 8, 6, 2, 0, 7, 5]
# Solvable in 11 moves
# problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
# Not Solvable
# problem1 = [1, 8, 2, 0, 4, 3, 7, 6, 5]

# TBD
problem1 = [6, 8, 7, 2, 5, 4, 3, 0, 1]

# Solvable in 31 moves
cutoff = ['cutoff']
failure = ['failure']
end_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]


solution = iterative_df_search(problem1)
print("Your Solution is with following moves {0}".format(iterative_df_search(problem1)))
