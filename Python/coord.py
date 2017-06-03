class Points:
    def __init__(self, k):
        # k -- размерность пространства
        self.points = list()
        self.k = k

    def add(self, *coords):
        # добавить точку
        self.points.append(coords)

    def remove(self, *coords):
        # удалить точку
        if coords in self.points :
            self.points.remove(coords)

    def range_query(self, *coord_ranges):
        r = coord_ranges
        return ( p for p in self.points if all( r[i][0] <= p[i] and p[i] <= r[i][1] for i in range(self.k) ))


ps = Points(2)
ps.add(1, 1)
ps.add(3, 1)
print(list(ps.range_query((1, 3), (1, 1)))) # [(1, 1), (3, 1)]
ps.add(3, 1)
print(list(ps.range_query((2, 3), (1, 1)))) # [(3, 1), (3, 1)]
ps.remove(2, 1)
ps.remove(3, 1)
print(list(ps.range_query((1, 3), (1, 1)))) # [(1, 1), (3, 1)]
