import copy
from collections import deque

# Method to determine if the state is in goal state
def is_goal(state):
    end_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    return state == end_state

# This method takes input of a state and previous state.
# It returns all possible child states with possible moves
def action(state, prev_state):
    result = []
    moves = []

    #This method is used to swap two input tiles within a state for a specified move
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


def breath_first_search(problem):
    previous_state = []
    node = [[]]
    node[0] = problem.copy()
    node.append(previous_state)

    # Checks to see if the initial problem state is already a goal state
    if is_goal(problem):
        return node[1]

    # Frontier FIFO queue to keep track of nodes that are getting generated
    frontier_queue = deque()

    # Explored queue to keep track of nodes that are explored
    explored_queue = []

    # Add the root node to FIFO frontier
    frontier_queue.append(node)

    # Infinite loop
    while True:

        # if FIFO runs out of nodes, get out the loop with no solution found
        if len(frontier_queue) == 0:
            print('No solution found')
            return []

        # For BFS, pop the shallowest first node by take the first node that was put in the queue
        parent_node = frontier_queue.popleft().copy()

        # Add the node to explored queue
        explored_queue.append(parent_node[0])

        # Identify all possible child nodes for a given parent node
        temp1, temp2 = action(parent_node[0], previous_state)

        # Loop through all child nodes with corresponding moves
        for move, child in zip(temp1, temp2):

            # If the child nodes were already generated previously as those states were already explored
            # as part of a shallower node, we already have a better optimal solution above in the tree. Hence,
            # ignore child not if it already  exists in frontier or explored queue
            if (child not in frontier_queue) & (child not in explored_queue):
                child_node = copy.deepcopy(parent_node)
                child_node[0] = child
                child_node[-1].append(move)

                # If solution found, return the identified moves for the same.
                if is_goal(child):
                    return child_node[-1]

                # Add the generated child node to frontier queue
                frontier_queue.append(child_node)

        # Update the previous state with the parent node for next depth of node generation
        previous_state = parent_node[0]

# Input format
# e.g. if we have an input of following
#  1 2 3
#  8 0 4
#  7 6 5
# the input is represented as a list as [ 1, 2, 3, 8, 0, 4, 7, 6, 5]

#  Following are test cases for testing the BFS for different kind of inputs

# Already solved input
problem1 = [ 1, 2, 3, 8, 0, 4, 7, 6, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(breath_first_search(problem1)))

# Solvable in depth of 1
problem1 = [ 1, 0, 3, 8, 2, 4, 7, 6, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(breath_first_search(problem1)))

# Solvable in 6 moves
problem1 = [ 1, 3, 4, 8, 0, 5, 7, 2, 6]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS  Solution is with following moves {0}".format(breath_first_search(problem1)))

# Another problem solvable in 6 moves
problem1 = [1, 3, 4, 8, 6, 2, 0, 7, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(breath_first_search(problem1)))

# Solvable in 11 moves
problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
print("\n Problem input is: {0}".format(problem1))
print("Your BFS Solution is with following moves {0}".format(breath_first_search(problem1)))

