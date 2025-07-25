from collections import deque

def get_successors(state):
    successors = []
    state = list(state)
    for i in range(len(state)):
        if state[i] == 'E':
         
            if i + 1 < len(state) and state[i + 1] == '.':
                new_state = state[:]
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                successors.append((''.join(new_state), (i, i + 1)))
          
            if i + 2 < len(state) and state[i + 1] in ['W', 'E'] and state[i + 2] == '.':
                new_state = state[:]
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                successors.append((''.join(new_state), (i, i + 2)))

        elif state[i] == 'W':
         
            if i - 1 >= 0 and state[i - 1] == '.':
                new_state = state[:]
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                successors.append((''.join(new_state), (i, i - 1)))
           
            if i - 2 >= 0 and state[i - 1] in ['W', 'E'] and state[i - 2] == '.':
                new_state = state[:]
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                successors.append((''.join(new_state), (i, i - 2)))
    return successors

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]
        visited.add(current)
        for next_state, _ in get_successors(current):
            if next_state not in visited:
                queue.append((next_state, path + [current]))
    return None

def dfs(start, goal):
    stack = [(start, [])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path + [current]
        visited.add(current)
        for next_state, _ in get_successors(current):
            if next_state not in visited:
                stack.append((next_state, path + [current]))
    return None

start_state = 'EEE.WWW'
goal_state = 'WWW.EEE'

print("BFS Solution Path:")
bfs_path = bfs(start_state, goal_state)
for state in bfs_path:
    print(state)

print("\nDFS Solution Path:")
dfs_path = dfs(start_state, goal_state)
for state in dfs_path:
    print(state)
