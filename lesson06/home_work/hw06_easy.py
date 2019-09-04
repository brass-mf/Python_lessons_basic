# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_square(self):
    return (self.coordinates[0][0]*(self.coordinates[1][1]-self.coordinates[2][1])+self.coordinates[1][0]*(self.coordinates[2][1]-self.coordinates[0][1])+self.coordinates[2][0]*(self.coordinates[0][1]-self.coordinates[1][1]))/2

var_triangle = Triangle([(1,2),(3,4),(5,6)])
print('Координаты точек:'+ str(var_triangle.get_square))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

