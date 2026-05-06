def calculate_tails(participants):
    """
    Для каждого участника считаем 'хвост' = время велосипеда + время бега.
    Возвращаем список кортежей: (индекс, плавание, велосипед, бег, хвост)
    """
    result = []
    for i, (swim, bike, run) in enumerate(participants):
        tail = bike + run
        result.append((i, swim, bike, run, tail))
    return result


def sort_by_tail_desc(indexed):
    """
    Сортируем участников по убыванию хвоста (велосипед + бег).
    """
    return sorted(indexed, key=lambda x: x[4], reverse=True)


def compute_schedule(indexed_sorted):
    """
    Считаем порядок и минимальное время завершения.
    """
    order = []
    current_swim_time = 0
    makespan = 0

    for i, swim, bike, run, tail in indexed_sorted:
        current_swim_time += swim         # время выхода из бассейна
        finish_time = current_swim_time + bike + run
        makespan = max(makespan, finish_time)
        order.append(i)

    return order, makespan


def optimal_schedule(participants):
    """
    Главная функция: строит оптимальный порядок и время завершения.
    """
    indexed = calculate_tails(participants)
    indexed_sorted = sort_by_tail_desc(indexed)
    order, makespan = compute_schedule(indexed_sorted)
    return order, makespan


participants = [
    (8, 10, 20),
    (5, 25, 25),
    (10, 20, 30)
]

order, makespan = optimal_schedule(participants)

print("Порядок:", " ".join(str(i + 1) for i in order))
print("Минимальное время завершения:", makespan)