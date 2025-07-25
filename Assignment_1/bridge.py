from collections import deque
from itertools import combinations

people = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

initial_state = (frozenset(people.keys()), frozenset(), 0, 'left')
goal_state = frozenset(), frozenset(people.keys())

def get_successors(state):
    left, right, time_elapsed, umbrella_side = state
    successors = []

    if umbrella_side == 'left':
        candidates = left
        other_side = right
        move_direction = 'right'
    else:
        candidates = right
        other_side = left
        move_direction = 'left'

    for movers in combinations(candidates, 2) if umbrella_side == 'left' else combinations(candidates, 1):
        move_time = max(people[p] for p in movers)
        new_time = time_elapsed + move_time

        if new_time > 60:
            continue

        new_left = set(left)
        new_right = set(right)

        if umbrella_side == 'left':
            for p in movers:
                new_left.remove(p)
                new_right.add(p)
        else:
            for p in movers:
                new_right.remove(p)
                new_left.add(p)

        new_state = (
            frozenset(new_left),
            frozenset(new_right),
            new_time,
            move_direction
        )
        successors.append((new_state, movers, move_time))

    return successors

def bfs():
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        current_state, path = queue.popleft()
        left, right, time_elapsed, umbrella_side = current_state

        if left == frozenset() and right == frozenset(people.keys()):
            return path + [(current_state, None, 0)]

        if current_state in visited:
            continue
        visited.add(current_state)

        for succ, movers, move_time in get_successors(current_state):
            move = (succ, movers, move_time)
            queue.append((succ, path + [(current_state, movers, move_time)]))
    return None

def dfs():
    stack = [(initial_state, [])]
    visited = set()
    while stack:
        current_state, path = stack.pop()
        left, right, time_elapsed, umbrella_side = current_state

        if left == frozenset() and right == frozenset(people.keys()):
            return path + [(current_state, None, 0)]

        if current_state in visited:
            continue
        visited.add(current_state)

        for succ, movers, move_time in get_successors(current_state):
            move = (succ, movers, move_time)
            stack.append((succ, path + [(current_state, movers, move_time)]))
    return None

def print_solution(path):
    if not path:
        print("No solution found.")
        return
    total_time = 0
    for state, movers, move_time in path:
        left, right, time_elapsed, umbrella = state
        if movers:
            direction = "→" if umbrella == "right" else "←"
            print(f"{' & '.join(movers)} {direction} ({move_time} min) | Time so far: {time_elapsed} min")
        else:
            print(f"All crossed within {time_elapsed} minutes.")
        total_time = time_elapsed
   

print("BFS Solution:")
bfs_path = bfs()
print_solution(bfs_path)

print("\nDFS Solution:")
dfs_path = dfs()
print_solution(dfs_path)

