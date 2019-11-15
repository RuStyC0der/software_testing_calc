from singleton import Singleton
from math import sin, cos, sqrt, pi

class Triangle_area(Singleton):

    def geron(self, a, b, c):
        """за формулою герона a, b, c - сторони"""
        p = (a+b+c)/2
        s = (c*((p-a) * (p - b) * (p - c))) ** 0.5
        return s

    def two_side_one_angle(self, side_a, side_b, angle):
        """Если мы имеем длину двух сторон треугольника a,b и величину угла γ между ними"""
        s = 0.5 * side_a * side_b * sin(angle)
        return s
    def side_height(self, side, height):
        """Если нам дано любую сторону треугольника и высоту, опущенную на эту сторону"""
        s = 0.5 * side * height
        return s

    def thre_side_described_circle(self, side_a, side_b, side_c, radius):
        """Формула площади треугольника по трем сторонам и радиусу описанной окружности"""
        s = (side_a * side_b * side_c) / (radius * 4)
        return s

    def tree_side_inscribed_circle(self, side_a, side_b, side_c, radius):
        """Формула площади треугольника по трем сторонам и радиусу описанной окружности"""
        p = (side_a + side_b + side_c)/2
        s = p * radius
        return s

    def one_side_two_angle(self, side, angle_a, angle_b):
        """Если известна одна сторона треугольника и два прилежащих к ней угла"""
        angle_c = 180 - (angle_a + angle_b)
        s = 0.5 * side ** 2 * ((sin(angle_b) * sin(angle_a)) / sin(angle_c))
        return s

class Quad_area(Singleton):

    def two_diagonal_one_angle(self, diagonal_a, diagonal_b, angle):
        """Формула площади четырехугольника по длине диагоналей и углу между ними"""
        s = 0.5 * diagonal_a * diagonal_b * sin(angle)
        return s

    def four_side_two_angle(self, side_a, side_b, side_c, side_d, angle_a, angle_b):
        """Формула площади четырехугольника по длине сторон и значению противоположных углов"""
        p = (side_a + side_b + side_c + side_d) / 2
        o = (angle_a + angle_b) / 2
        s = sqrt((p - side_a) * (p - side_b) * (p - side_c) * (p - side_d) * side_a * side_b * side_c * side_d * (cos(o) ** 2))
        return s

class Squad_area(Singleton):
    def one_side(self, side):
        """Формула площади квадрата по длине стороны"""
        return side ** 2

    def one_diagonal(self, diagonal):
        """Формула площади квадрата по длине диагонали"""
        return 0.5 * (diagonal ** 2)

class Rectangle_area(Singleton):

    def two_side(self, side_a, side_b):
        """прямокутника значення двох відомих сторін."""
        return side_b * side_a

class Parallelogram_area:
    def base_height(self, base, height):
        """Формула площади параллелограмма по длине стороны и высоте"""
        return base * height

    def two_side_one_angle(self, side_a, side_b, angle):
        """Формула площади параллелограмма по двум сторонам и углу между ними"""
        s = side_a * side_b * sin(angle)
        return s

    def two_diagonal_one_angle(self, diagonal_a, diagonal_b, angle):
        """Формула площади параллелограмма по двум диагоналям и углу между ними"""
        s = 0.5 * diagonal_a * diagonal_b * sin(angle)
        return s

class Diamond_area(Singleton):
    def one_side_one_angle(self, side, angle):
        """Формула площади ромба по длине стороны и углу"""
        s = (side ** 2) * sin(angle)
        return s

    def one_side_height(self, side, height):
        """Формула площади ромба по длине стороны и высоте"""
        return side * height

    def two_diagonal(self, diagonal_a, diagonal_b):
        """Формула площади ромба по длинам его диагоналей"""
        return 0.5 * diagonal_a * diagonal_b

class Trapeze_area(Singleton):

    def two_base_one_height(self, base_a, base_b, height):
        """Формула площади трапеции по длине основ и высоте"""
        s = 0.5*(base_a + base_b) * height
        return s

    def two_diagonal_one_angle(self, diagonal_a, diagonal_b, angle):
        """Формула площади трапеции по двум диагоналям и углу между ними"""
        s = 0.5 * diagonal_a * diagonal_b * sin(angle)
        return s

    def one_height_middle_line(self, height, middle_line):
        return height * middle_line

class Circle_area(Singleton):

    def one_length(self, length):
        """формула площади круга через длину"""
        s = (length **2) / (pi * 4)
        return s

    def one_radius(self, radius):
        """формула площади круга через радиус"""
        return pi * (radius ** 2)

    def one_diameter(self, diameter):
        """формула площади круга через диаметр. """
        return (pi /4) * (diameter ** 2)

class Ellipse_area(Singleton):

    def two_half_shaft(self, shaft_a, shaft_b):
        """знаходження площі через введення більшої та меншої напівосей еліпса."""
        return pi * shaft_a * shaft_b

class Area_calc(Singleton):

    def __init__(self):
        super().__init__()
        self.triangle = Triangle_area()
        self.quad = Quad_area()
        self.squad = Squad_area()
        self.rectangle = Rectangle_area()
        self.parallelogram = Parallelogram_area()
        self.diamond = Diamond_area()
        self.trapeze = Trapeze_area()
        self.circle = Circle_area()
        self.ellipse = Ellipse_area()



if __name__ == '__main__':
    a = Area_calc()
    b = Area_calc()
    # z = a.triangle.
    print(a)
    print(b)