points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]  # координаты точек
start_point = 0  # индекс начальной точки
start = points[start_point]  # начальная точка
ds = 0  # расстояние которое прошел почтальон


# Логика : вычисляем расстояния от начальной точки, до каждой точки из списка координат.
#          выбираем минимальное расстояние, удаляем начальную точку, повторяем дейтвия, пока не останется одна точка.

def distance(fist_point: int, list_points: list, dis):
    """

    :param fist_point: индекс нчальной точки в списке координат
    :param list_points: список координат точек
    :param dis: расстояние которое прошел почтальон
    :return: если точек больше одной:
                    передает в функцию min_distance список расстояний от начальной точки, до каждой другой точки.
            если осталась одна точка, вычисляет расстояние от этой точки до начальной точки, и возвращает
            расстояние, которое прошел почтальон
    """
    fist_coor = list_points[fist_point]
    print(fist_coor, '->')
    if len(list_points) == 1:
        list_points.append(start)  # точка начала пути
        print(start)
        dist = ((fist_coor[0] - list_points[1][0]) ** 2 + (fist_coor[1] - list_points[1][1]) ** 2) ** 0.5
        dis += dist
        return dis
    distanse_list = []
    for index, coordinates in enumerate(list_points):
        dist = ((fist_coor[0] - coordinates[0]) ** 2 + (fist_coor[1] - coordinates[1]) ** 2) ** 0.5
        distanse_list.append(dist)
    return min_distance(distanse_list, list_points, fist_point, dis)


def min_distance(list_distances: list, list_points: list, fist_point: int, dis):
    """

    :param list_distances: список расстояний от начальной точки, до других
    :param list_points: список координат точек
    :param fist_point: индекс нчальной точки в списке координат
    :param dis: расстояние которое прошел почтальон
    :return: передает в функцию distance индекс следующей точки, спискок кооординат,
     и расстояние которое прошел почтальон
    """
    list_points.pop(fist_point)
    list_distances.remove(0.0)
    fist_point = list_distances.index(min(list_distances))
    if list_distances:
        dis += min(list_distances)
        print(list_points[fist_point])
        print(dis)

    return distance(fist_point, list_points, dis)


if __name__ == '__main__':
    print(distance(start_point, points, ds))
