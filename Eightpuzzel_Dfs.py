# 8-Puzzle using DFS

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    # Up
    if row > 0:
        new_state = state.copy()
        new_state[zero], new_state[zero - 3] = \
            new_state[zero - 3], new_state[zero]
        neighbors.append(("Up", new_state))

    # Down
    if row < 2:
        new_state = state.copy()
        new_state[zero], new_state[zero + 3] = \
            new_state[zero + 3], new_state[zero]
        neighbors.append(("Down", new_state))

    # Left
    if col > 0:
        new_state = state.copy()
        new_state[zero], new_state[zero - 1] = \
            new_state[zero - 1], new_state[zero]
        neighbors.append(("Left", new_state))

    # Right
    if col < 2:
        new_state = state.copy()
        new_state[zero], new_state[zero + 1] = \
            new_state[zero + 1], new_state[zero]
        neighbors.append(("Right", new_state))

    return neighbors


def dfs(initial, goal):
    stack = [(initial, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        state_tuple = tuple(state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        # Goal test
        if state == goal:
            return path

        # Generate next states
        for move, new_state in get_neighbors(state):
            if tuple(new_state) not in visited:
                stack.append((new_state, path + [move]))

    return None


# Initial and goal states
initial = [1, 2, 3,
           4, 0, 6,
           7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

print("Initial State:")
print_puzzle(initial)

print("Goal State:")
print_puzzle(goal)

solution = dfs(initial, goal)

if solution:
    print("DFS Solution:")
    print(" -> ".join(solution))
    print("Number of moves:", len(solution))
else:
    print("No solution found.")
