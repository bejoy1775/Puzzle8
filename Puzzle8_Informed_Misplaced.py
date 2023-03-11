import copy
from collections import deque


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


def breath_first_search(problem):
    previous_state = []
    node = [[]]
    node[0] = problem.copy()
    node.append(previous_state)

    if is_goal(problem):
        return node[1]

    frontier_queue = deque()

    explored_queue = []

    frontier_queue.append(node)

    while True:

        if len(frontier_queue) == 0:
            print('No solution found')
            return []

        parent_node = frontier_queue.popleft().copy()

        explored_queue.append(parent_node[0])

        temp1, temp2 = action(parent_node[0], previous_state)

        for move, child in zip(temp1, temp2):

            if (child not in frontier_queue) & (child not in explored_queue):
                child_node = copy.deepcopy(parent_node)
                child_node[0] = child
                child_node[-1].append(move)

                if is_goal(child):
                    return child_node[-1]

                frontier_queue.append(child_node)

        previous_state = parent_node[0]

# Already solved input
problem1 = [ 1, 2, 3, 8, 0, 4, 7, 6, 5]
# Solvable in depth of 1
# problem1 = [ 1, 0, 3, 8, 2, 4, 7, 6, 5]
# Solvable in 6 moves
# problem1 = [ 1, 3, 4, 8, 0, 5, 7, 2, 6]
# problem1 = [1, 3, 4, 8, 6, 2, 0, 7, 5]
# Solvable in 11 moves
# problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
# Not Solvable in some unknown depth
# problem1 = [ 3, 1, 4, 8, 0, 5, 7, 2, 6]
# problem1 = [ 1, 8, 2, 0, 4, 3, 7, 6, 5]
# problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
print("Your Solution is with following moves {0}".format(breath_first_search(problem1)))
