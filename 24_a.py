def check_mst(T, v, w, c):
    # T — список смежности дерева
    # возвращает True, если MST не меняется

    # DFS: найдём путь v->w и максимум на пути
    stack = [v]
    parent = {v: None}
    edge_w = {v: 0}

    while stack:
        u = stack.pop()
        if u == w:
            break
        for nei, wt in T[u]:
            if nei not in parent:
                parent[nei] = u
                edge_w[nei] = max(edge_w[u], wt)
                stack.append(nei)

    max_on_path = edge_w[w]
    return c >= max_on_path


# пример
T = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('A', 3), ('D', 4)],
    'D': [('C', 4)]
}
print(check_mst(T, 'A', 'D', 5))  