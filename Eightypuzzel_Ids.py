# 8-Puzzle using Iterative Deepening Search (IDS)

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


def depth_limited_search(state, goal, depth, path, visited):

    # Goal test
    if state == goal:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    visited.add(tuple(state))

    for move, new_state in get_neighbors(state):

        if tuple(new_state) not in visited:

            result = depth_limited_search(
                new_state,
                goal,
                depth - 1,
                path + [move],
                visited
            )

            if result is not None:
                return result

    visited.remove(tuple(state))

    return None


def ids(initial, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = set()

        result = depth_limited_search(
            initial,
            goal,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

        depth += 1


# Initial state
initial = [1, 2, 3,
           4, 0, 6,
           7, 5, 8]

# Goal state
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

print("Initial State:")
print_puzzle(initial)

print("Goal State:")
print_puzzle(goal)

solution = ids(initial, goal)

print("IDS Solution:")
print(" -> ".join(solution))
print("Number of moves:", len(solution))
