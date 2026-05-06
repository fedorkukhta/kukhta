from itertools import permutations

# Пример
r = [0.9, 0.5, 0.8, 0.95]

best_order = None
best_value = -1.0

for p in permutations(range(len(r))):
    s = 0.0
    for t, i in enumerate(p):
        s += 100 * (r[i] ** t) 
    if s > best_value:
        best_value = s
        best_order = p

print("Оптимальный порядок продажи:", [i + 1 for i in best_order])
print("Максимальная суммарная выручка:", best_value)