def min_base_stations(houses, radius=4):
    
    houses = sorted(houses)
    n = len(houses)
    stations = []

    i = 0
    while i < n:
        # самый левый непокрытый дом
        left_house = houses[i]

        # ставим станцию максимально вправо
        station_pos = left_house + radius
        stations.append(station_pos)

        # покрытие этой станции справа до station_pos + radius 
        cover_right = station_pos + radius

        # пропускаем все покрытые дома
        i += 1
        while i < n and houses[i] <= cover_right:
            i += 1

    return len(stations), stations


houses = [1, 2, 3, 7, 9, 11, 16, 17]
count, stations = min_base_stations(houses, radius=4)
print("Минимум станций:", count)
print("Позиции:", stations)