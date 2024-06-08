def calculate_heights(n, parent_child_pairs):
    from collections import defaultdict, deque

    tree = defaultdict(list)
    for child, parent in parent_child_pairs:
        tree[parent].append(child)

    heights = {0: 0}  # Родоначальник имеет высоту 0
    queue = deque([0])

    while queue:
        parent = queue.popleft()
        for child in tree[parent]:
            heights[child] = heights[parent] + 1
            queue.append(child)

    return heights

# Пример использования:
n = 5
parent_child_pairs = [(1, 0), (2, 0), (3, 1), (4, 1)]
print(calculate_heights(n, parent_child_pairs))  # Вывод: {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
