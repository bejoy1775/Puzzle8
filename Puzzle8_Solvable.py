# Python3 program to check if a given
# instance of 8 puzzle is solvable or not

# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isEven(puzzle):
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])

    # return true if inversion count is even.
    return (inv_count % 2 == 0)


# Driver code
problem = [[6, 8, 7], [2, 5, 4], [3, -1, 1]]
goal    = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]
problem_inversion_even =  isEven(problem)
goal_inversion_even = isEven(goal)
if problem_inversion_even & goal_inversion_even:
    print("Solvable")
elif (not problem_inversion_even) & (not goal_inversion_even):
    print("Solvable")
else:
    print("Not Solvable")

# This code is contributed by vitorhugooli
# Fala meu povo desse Brasil varonil



