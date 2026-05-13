def update_mst(T, v, w, c):
    # DFS: найдём путь v->w и самое тяжёлое ребро
    stack = [v]
    parent = {v: None}
    parent_edge = {v: None}

    while stack:
        u = stack.pop()
        if u == w:
            break
        for nei, wt in T[u]:
            if nei not in parent:
                parent[nei] = u
                parent_edge[nei] = (u, nei, wt)
                stack.append(nei)

    # идём по пути и ищем максимум
    max_w = -1
    max_edge = None
    cur = w
    while cur != v:
        a, b, wt = parent_edge[cur]
        if wt > max_w:
            max_w = wt
            max_edge = (a, b, wt)
        cur = a

    # если новое ребро не лучше — MST не меняется
    if c >= max_w:
        return T

    # удалить максимальное ребро
    a, b, _ = max_edge
    T[a] = [(x, wt) for x, wt in T[a] if x != b]
    T[b] = [(x, wt) for x, wt in T[b] if x != a]

    # добавить новое ребро
    T[v].append((w, c))
    T[w].append((v, c))

    return T


# пример
T = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('A', 3), ('D', 4)],
    'D': [('C', 4)]
}
print(update_mst(T, 'A', 'D', 1))