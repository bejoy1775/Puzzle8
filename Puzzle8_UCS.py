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

# executes UCS algorithim, takes in problem and associated cost. For this problem, cost is assumed to be 1
def uniform_cost_search(problem, cost):
    previous_state = []
    moves = []
    current_cost  = 0
    node = [problem, moves, current_cost]

    # Frontier FIFO queue to keep track of nodes that are getting generated
    # Add the root node to FIFO frontier
    frontier_queue = {0: node}

    # Explored queue to keep track of nodes that are explored
    explored_queue = []

    while True:

        # if FIFO runs out of nodes, get out the loop with no solution found
        if not frontier_queue:
            print('No solution found')
            return []

        # For UCS, pop the most priority first node by take the first node that was put in the queue
        # Queue is treated like a priority queue. We pop the node with the minimum cost
        parent_node = frontier_queue.pop(min(frontier_queue.keys()))

        # Evaluate goal state for parent node before child not generation, if found return solution.
        if is_goal(parent_node[0]):
            return parent_node[1]

        # Add parent node to explored queue
        explored_queue.append(parent_node[0])

        # Call action to identify all child nodes and corresponding moves
        temp1, temp2 = action(parent_node[0], previous_state)

        # For each child, determine cost associated
        for move, child in zip(temp1, temp2):

            # create child with  state, moves and associated cost
            child_node = copy.deepcopy(parent_node)
            child_node[0] = child
            child_node[1].append(move)
            child_node[2] = parent_node[2] + cost

            # if child not in frontier, neither in explored, add child to end of FIFO frontier queue.
            if (child not in frontier_queue.values()) & (child not in explored_queue):
                if frontier_queue:
                    newkey = max(frontier_queue.keys()) + 1
                else:
                    newkey = 0

                frontier_queue[newkey] = child_node

            # else child exists in frontier queue but with better cost, overite the existing node with this child node
            elif child in frontier_queue.values():
                for key, value, node_cost in frontier_queue.items():
                    if value == child & node_cost > child_node[2]:
                        frontier_queue[key] = child_node

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
cost = 1
print("\n Problem input is: {0}".format(problem1))
print("Your UCS Solution is with following moves {0}".format(uniform_cost_search(problem1, cost)))

# Solvable in depth of 1
problem1 = [ 1, 0, 3, 8, 2, 4, 7, 6, 5]
cost = 1
print("\n Problem input is: {0}".format(problem1))
print("Your UCS Solution is with following moves {0}".format(uniform_cost_search(problem1, cost)))

# Solvable in 6 moves
problem1 = [ 1, 3, 4, 8, 0, 5, 7, 2, 6]
cost = 1
print("\n Problem input is: {0}".format(problem1))
print("Your UCS Solution is with following moves {0}".format(uniform_cost_search(problem1, cost)))

# Another problem solvable in 6 moves
problem1 = [1, 3, 4, 8, 6, 2, 0, 7, 5]
cost = 1
print("\n Problem input is: {0}".format(problem1))
print("Your UCS Solution is with following moves {0}".format(uniform_cost_search(problem1, cost)))

# Solvable in 11 moves
problem1 = [ 3, 6, 4, 0, 1, 2, 8, 7, 5]
cost = 1
print("\n Problem input is: {0}".format(problem1))
print("Your UCS Solution is with following moves {0}".format(uniform_cost_search(problem1, cost)))
