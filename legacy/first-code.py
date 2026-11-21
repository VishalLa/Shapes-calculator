"""Code for shapes"""

import math


# class for Quadrilaterals
class Quadrilaterals:
    def __init__(self, side_1, side_2, side_3, side_4):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.side_4 = side_4


# condition for Triangle sum of 2 small size should be greate than larger side!
class Triangle:
    def __init__(self, base, side):
        self.base = base
        self.side = side


# class for cuboid!
class Three_dimension:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


# class for all shapes which use pie
class with_pie:
    def __init__(self, pie, radius):
        self.pie = pie
        self.radius = radius


class Quadrilateral(Quadrilaterals):
    def __init__(self, side_1, side_2, side_3, side_4):
        super().__init__(side_1, side_2, side_3, side_4)

        a = self.side_1
        b = self.side_2
        c = self.side_3
        d = self.side_4

        if self.side_1 == self.side_2 == self.side_3 == self.side_4:
            print(
                "It is a square"
            )

        elif (self.side_1 == self.side_2 and self.side_3 == self.side_4 or
              self.side_1 == self.side_3 and self.side_2 == self.side_4):
            print(
                "It is a Rectangle"
            )

        elif abs(a - b) < c < a + b - d:
            print(
                "This can be Trapezium with side 1 parallel to side 2"
            )

        elif abs(a - b) < d < a + b - c:
            print(
                "This can be Trapezium with side 1 parallel to side 2"
            )

        elif abs(a - c) < b < a + c - d:
            print(
                "This can be Trapezium with side 1 parallel to side 3"
            )

        elif abs(a - c) < d < a + c - b:
            print(
                "This can be Trapezium with side 1 parallel to side 2"
            )

        elif abs(a - d) < c < a + d - b:
            print(
                "This can be Trapezium with side 1 parallel side 3"
            )

        elif abs(a - d) < b < a + d - c:
            print(
                "This can be Trapezium with side 1 parallel to side 2"
            )

        elif abs(b - c) < a < b + c - d:
            print(
                "This can be Trapezium with side 2 parallel to side 3"
            )

        elif abs(b - c) < d < b + c - a:
            print(
                "This can be Trapezium with side 2 parallel to side 3"
            )

        elif abs(c - d) < a < c + d - b:
            print(
                "This can be Trapezium with side 3 parallel to side 4"
            )

        elif abs(c - d) < b < c + d - a:
            print(
                "This can be Trapezium with side 3 parallel to side 4"
            )

        else:
            print(
                "Invalid Input :("
            )

    def parameter_calculation(self):
        return self.side_1 + self.side_2 + self.side_3 + self.side_4

    def area_calculation(self):
        s = (self.side_1 + self.side_2 + self.side_3 + self.side_4) / 2
        area = (s - self.side_1) * (s - self.side_2) * (s - self.side_3) * (s - self.side_4)
        return area ** 0.5

    def diagonal1_calculation(self):
        return (self.side_1 ** 2 + self.side_3 ** 2) ** 0.5

    def diagonal2_calculation(self):
        return (self.side_2 ** 2 + self.side_4 ** 2) ** 0.5


class Rectangle(Quadrilaterals):
    def __init__(self, side_1, side_2, side_3, side_4):
        super().__init__(side_1, side_2, side_3, side_4)

    def parameter_calculation(self):
        return 2 * (self.side_1 + self.side_2)

    def area_calculation(self):
        return self.side_1 * self.side_2

    def diagonal_calculation(self):
        return (self.side_1 ** 2 + self.side_2 ** 2) ** 0.5


# class for trapezium and I did not thing that I give condition for angles only sides conditions !
class Trapezium(Quadrilaterals):
    def __init__(self, side_1, side_2, side_3, side_4):
        super().__init__(side_1, side_2, side_3, side_4)

        a = self.side_1
        b = self.side_2
        c = self.side_3
        d = self.side_4

        # conditions for which sides are parallel
        if abs(a - b) < c < a + b - d:
            print(
                "This is a Trapezium with side 1 parallel to side 2"
            )

        elif abs(a - b) < d < a + b - c:
            print(
                "This is a Trapezium with side 1 parallel to side 2"
            )

        elif abs(a - c) < b < a + c - d:
            print(
                "This is a Trapezium with side 1 parallel to side 3"
            )

        elif abs(a - c) < d < a + c - b:
            print(
                "This is a Trapezium with side 1 parallel to side 2"
            )

        elif abs(a - d) < c < a + d - b:
            print(
                "This is a Trapezium with side 1 parallel side 3"
            )

        elif abs(a - d) < b < a + d - c:
            print(
                "This is a Trapezium with side 1 parallel to side 2"
            )

        elif abs(b - c) < a < b + c - d:
            print(
                "This is a Trapezium with side 2 parallel to side 3"
            )

        elif abs(b - c) < d < b + c - a:
            print(
                "This is a Trapezium with side 2 parallel to side 3"
            )

        elif abs(c - d) < a < c + d - b:
            print(
                "This is a Trapezium with side 3 parallel to side 4"
            )

        elif abs(c - d) < b < c + d - a:
            print(
                "This is a Trapezium with side 3 parallel to side 4"
            )

    def parameter_calculation(self):
        return self.side_1 + self.side_2 + self.side_3 + self.side_4

    def area_calculation(self):
        a = self.side_1
        b = self.side_2
        c = self.side_3
        d = self.side_4
        return (abs(a ** 2 * ((d - b) ** 2 + a ** 2 - c ** 2) / 2 * (d - b))) ** 0.5

    def height_calculation(self):
        a = self.side_1
        b = self.side_2
        c = self.side_3
        d = self.side_4

        # updating parallel sides which side are parallel!
        if a == b:
            parallel_side_1 = a
            parallel_side_2 = c if c != d else d

        elif a == c:
            parallel_side_1 = a
            parallel_side_2 = b if b != d else d

        else:
            parallel_side_1 = b
            parallel_side_2 = c if c != d else d

        area = (abs(a ** 2 * ((d - b) ** 2 + a ** 2 - c ** 2) / 2 * (d - b))) ** 0.5
        return abs((2 * area) / parallel_side_1 - parallel_side_2)

    def diagonals_calculation(self):
        # Diagonal 1 connects side_1 and side_3
        diagonal1 = float((self.side_1 ** 2 + self.side_3 ** 2) ** 0.5)

        # Diagonal 2 connects side_2 and side_4
        diagonal2 = float((self.side_2 ** 2 + self.side_4 ** 4) ** 0.5)
        return diagonal1, diagonal2


# classes for Triangle !
class Equilateral(Triangle):
    def __init(self, base, side):
        super().__init__(base, side)

    def area_calculation(self):
        return ((3 ** 0.5) / 4) * self.side ** 2

    def parameter_calculation(self):
        return 3 * self.side

    def height_calculation(self):
        return (self.side / 2) ** 2 + self.side ** 2


class Isosceles(Triangle):
    def __init__(self, base, side):
        super().__init__(base, side)

    def parameter_calculation(self):
        return 2 * self.side + self.base

    def area_calculation(self):
        semi_parameter = (2 * self.side + self.base) / 2
        return (semi_parameter *
                ((semi_parameter - self.side) ** 2)
                * (semi_parameter - self.base))

    def height_with_base_as_base_and_side(self):
        H1 = (abs(self.side ** 2 - (self.base / 2) ** 2)) ** 0.5
        return H1

    def height_with_base_as_equal_side_and_base(self):
        H2 = (abs(self.base ** 2 - (self.side / 2) ** 2)) ** 0.5
        return H2


class Scalene(Triangle):
    def __init__(self, base, side, side_2):
        super().__init__(base, side)
        self.side_2 = side_2

        if (self.side < self.side_2 + self.base
                and self.side_2 < self.side + self.base
                and self.base < self.side + self.side_2):

            if self.base == self.side == self.side_2:
                print(
                    "This is a Equilateral Triangle!"
                )

            elif self.base == self.side or self.side == self.side_2 or self.base == self.side:
                print(
                    "This is Isosceles Triangle!"
                )

            elif self.side != self.side_2 and self.side != self.base and self.base != self.side_2:
                print(
                    "This is a Scalene Triangle!"
                )

    def area_calculation(self):
        semi_parameter = (self.base + self.side + self.side_2) / 2
        return (semi_parameter *
                (semi_parameter - self.base) *
                (semi_parameter - self.side) *
                (semi_parameter - self.side_2)) ** 0.5

    def parameter_calculation(self):
        return self.base + self.side + self.side_2

    def height_calculation_with_base_as_base(self):
        semi_parameter = (self.base + self.side + self.side_2) / 2
        area = (semi_parameter *
                (semi_parameter - self.base) *
                (semi_parameter - self.side) *
                (semi_parameter - self.side_2)) ** 0.5
        base = self.base
        return 2 * area / base


# class for circle
class Circle(with_pie):
    def __init__(self, pie, radius):
        super().__init__(pie, radius)

    def area_calculation(self):
        return self.pie * self.radius ** 2

    def circumference_calculation(self):
        return 2 * self.pie * self.radius


# classes of three dimension
class Cuboid(Three_dimension):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

        if self.length == self.width == self.height:
            print(
                "This is Cube!"
            )
        else:
            print(
                "This is Cuboid!"
            )

    def curved_surface_area_calculation(self):
        return 2 * self.height * (self.length + self.width)

    def total_surface_area_calculation(self):
        return 2 * (self.length * self.width +
                    self.width * self.height +
                    self.length * self.height)

    def volume_calculation(self):
        return self.length * self.width * self.height

    def long_diagonal_calculation(self):
        return (self.length ** 2 + self.width ** 2 + self.height ** 2) ** 0.5

    def short_diagonal_calculation_length_width(self):
        return (self.length ** 2 + self.width ** 2) ** 0.5

    def short_diagonal_calculation_width_height(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5

    def short_diagonal_calculation_length_height(self):
        return (self.length ** 2 + self.height ** 2) ** 0.5


class Sphere(with_pie):
    def __init__(self, pie, radius):
        super().__init__(pie, radius)

    def area_calculation(self):
        return 4 * self.pie * self.radius ** 2

    def volume_calculation(self):
        return 4 / 3 * self.pie * self.radius ** 3


class Hollow_sphere(with_pie):
    def __init__(self, pie, radius, inner_radius, outer_radius):
        super().__init__(pie, radius)
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius

    def volume_hollow_sphere_calculation(self):
        return abs((4 / 3 * self.pie *
                    (self.outer_radius ** 3 - self.inner_radius ** 3)))

    def area_hollow_sphere_calculation(self):
        return abs(4 * self.pie * self.outer_radius ** 3)


class Hemisphere(with_pie):
    def __init__(self, pie, radius):
        super().__init__(pie, radius)

    def curved_surface_area_hemisphere_calculation(self):
        return abs(2 * self.pie * self.radius ** 2)

    def total_surface_area_hemisphere_calculation(self):
        return abs(3 * self.pie * self.radius ** 2)

    def volume_hemisphere_calculation(self):
        return abs(2 / 3 * self.pie * self.radius ** 3)


class Hollow_hemisphere(with_pie):
    def __init__(self, pie, radius, inner_radius, outer_radius):
        super().__init__(pie, radius)
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius

    def curved_hollow_hemisphere_calculation(self):
        return abs(2 * self.pie * self.inner_radius ** 2)

    def total_hollow_hemisphere_calculation(self):
        return abs((2 * self.pie * (self.outer_radius ** 2 + self.inner_radius ** 2) +
                    self.pie * (self.outer_radius ** 2 - self.inner_radius ** 2)))

    def volume_hollow_hemisphere_calculation(self):
        return abs((2 / 3 * self.pie *
                    (self.outer_radius ** 3 - self.inner_radius ** 3)))


class Cylinder(with_pie):
    def __init__(self, pie, radius, height):
        super().__init__(pie, radius)
        self.height = height

    def volume_calculation(self):
        return abs(self.pie * self.height * self.radius ** 2)

    def curved_surface_area_calculation(self):
        return abs(2 * self.pie * self.radius * self.height)

    def total_surface_area_calculation(self):
        return abs(2 * self.pie * self.radius * (self.height + self.radius))


class Hollow_cylinder(with_pie):
    def __init__(self, pie, inner_radius, outer_radius, height, radius):
        super().__init__(pie, radius)
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.height = height

    def volume_calculation(self):
        return abs(self.pie * self.height *
                   (self.outer_radius ** 2 - self.inner_radius ** 2))

    def curved_surface_area_calculation(self):
        return abs(2 * self.pie * self.height * self.outer_radius)

    def total_surface_area_calculation(self):
        return abs(2 * self.pie * self.height * (self.outer_radius + self.inner_radius) +
                   self.pie * (self.outer_radius ** 2 - self.inner_radius ** 2))


class Cone(with_pie):
    def __init__(self, pie, radius, height):
        super().__init__(pie, radius)
        self.height = height

    def curved_surface_area_calculation(self):
        return self.pie * self.radius * (
                self.radius + (self.height ** 2 + self.radius ** 2) ** 0.5)

    def total_surface_area_calculation(self):
        return self.pie * self.radius * (self.radius + (
                self.height ** 2 + self.radius ** 2) ** 0.5) + self.pie * self.radius ** 2

    def volume_calculation(self):
        return 1 / 3 * self.pie * self.radius ** 2 * self.height

    def slant_height_calculation(self):
        return (self.height ** 2 + self.radius ** 2) ** 0.5


class Frustum(with_pie):
    def __init__(self, pie, radius, small_radius, big_radius, height):
        super().__init__(pie, radius)
        self.small_radius = small_radius
        self.big_radius = big_radius
        self.height = height

    def volume_calculation(self):
        Volume = 1 / 3 * (self.pie * self.height *
                          (self.small_radius ** 2 + self.big_radius ** 2 + self.small_radius * self.big_radius))
        return Volume

    def total_surface_area_calculation(self):
        slant_height = (self.height ** 2 + (self.big_radius - self.small_radius) ** 2) ** 0.5
        total_area = (self.pie * slant_height *
                      (self.small_radius + self.small_radius) +
                      self.pie * self.small_radius ** 2 + self.pie * self.big_radius)
        return total_area

    def curved_surface_area(self):
        slant_height = (self.height ** 2 + (self.big_radius - self.small_radius) ** 2) ** 0.5
        curved_area = self.pie * slant_height * (self.small_radius + self.big_radius)
        return curved_area

    def slant_height_calculation(self):
        slant_height = (self.height ** 2 + (self.big_radius - self.small_radius) ** 2) ** 0.5
        return slant_height

Unit = ["meter", "centimeter", "feat"]
unit = None
while unit not in Unit:
    unit = input("Please chose a unit\n"
                 "Meter / Centimeter / Feat: ").lower()


def quaderilateral():
    l=[float(input(f'side {i+1}')) for i in range(4)]
    quad = Quadrilateral(l[0],l[1],l[2],l[3])
    print(f'Area: {quad.area_calculation()} {unit} square')
    print(f'Parameter: {quad.parameter_calculation} {unit}')
    print(f'Diagonal 1: {quad.diagonal1_calculation()} {unit}\n'
          f'with side 1 and side 3')
    print(f'Diagonal 2: {quad.diagonal2_calculation()} {unit}\n'
          f'with side 2 and side 4')
    
def rectangle():
    length = float(input('Length: '))
    width = float(input('Width: '))
    rect = Rectangle(length, width, 0,0)
    print(f'Area: {rect.area_calculation()} {unit} square')
    print(f'Parameter: {rect.parameter_calculation()} {unit}')
    print(f'Diagonal: {rect.diagonal_calculation()} {unit}')

def trapezium():
    l=[float(input(f'side {i+1}')) for i in range(4)]
    trap = Trapezium(l[0],l[1],l[2],l[3])
    side_1, side_2, side_3, side_4 = l[0],l[1],l[2],l[3]
    if (abs(side_1 - side_2) < side_3 < side_1 + side_2 - side_4 or
        abs(side_1 - side_2) < side_4 < side_1 + side_2 - side_3 or
        abs(side_1 - side_3) < side_2 < side_1 + side_3 - side_4 or
        abs(side_1 - side_3) < side_4 < side_1 + side_3 - side_2 or
        abs(side_1 - side_4) < side_3 < side_1 + side_4 - side_2 or
        abs(side_1 - side_4) < side_2 < side_1 + side_4 - side_3 or
        abs(side_2 - side_3) < side_1 < side_2 + side_3 - side_4 or
        abs(side_2 - side_3) < side_4 < side_2 + side_3 - side_1 or
        abs(side_3 - side_4) < side_1 < side_3 + side_4 - side_2 or
        abs(side_3 - side_4) < side_2 < side_3 + side_4 - side_1):

        print(f'Area: {trap.area_calculation()} {unit} square')
        print(f'Parmeter: {trap.parameter_calculation()} {unit}')
        print(f'Diagonal: 1: {trap.diagonals_calculation()} {unit}')
        print(f'Heighit: {trap.height_calculation()} {unit}')
    else:
        print('Invalid Input :(')

def triangles():
    Triangle_Type: list[str] = ['Equilateral', 'Isosceles', 'Scalene']
    Triangle_type = None
    while Triangle_type not in Triangle_Type:
        Triangle_type = input("Equilateral / Isosceles / Scalene: ").capitalize()

        if Triangle_type == "Equilateral":
            side = float(input("Side: "))
            base = 0
            equilateral = Equilateral(base, side)

            print(f'Area: {equilateral.area_calculation():f} {unit} square')
            print(f'Parameter: {equilateral.parameter_calculation():f} {unit}')
            print(f'Height: {equilateral.height_calculation():f} {unit}')

        elif Triangle_type == "Isosceles":
            side = float(input("Equal Side: "))
            base = float(input("Base: "))
            isosceles = Isosceles(base, side)

            print(f'Area: {isosceles.area_calculation():f} {unit} square')
            print(f'Parameter: {isosceles.parameter_calculation():f} {unit}')
            print(f'Height with base and side: '
                 f'{isosceles.height_with_base_as_base_and_side():f} {unit}')
            print(f'Height with base as side and side as base: '
                  f'{isosceles.height_with_base_as_equal_side_and_base():f} {unit}')

        elif Triangle_type == "Scalene":
            side = float(input("Side_1: "))
            side_2 = float(input("Side_2: "))
            base = float(input("Base: "))
            scalene = Scalene(base, side, side_2)

            if side < side_2 + base and base < side_2 + side and side_2 < base + side:
                print(f'Area: {scalene.area_calculation():f} {unit} square')
                print(f'Parameter: {scalene.parameter_calculation():f} {unit}')
                print('Height: {scalene.height_calculation_with_base_as_base():f} {unit}')

        else:
            print("Invalid Input :(")

def circle():
    pie = math.pi
    radius = float(input('Radius: '))
    cir = Circle(pie, radius)
    print(f'Area: {cir.area_calculation} {unit} square')
    print(f'Circumference: {cir.circumference_calculation} {unit}')

def cuboid():
    length = float(input("Length: "))
    width = float(input("Width: "))
    height = float(input("Height: "))
    cub = Cuboid(length, width, height)
    print(f'Curved surface area: {cub.curved_surface_area_calculation()} {unit} square')
    print(f'Total surface area: {cub.total_surface_area_calculation()} {unit} square')
    print(f'Volume: {cub.volume_calculation()} {unit} cube')
    print(f'Boday diagonal: {cub.long_diagonal_calculation()} {unit}')
    if length == width == height:
        print(f'Face diagnals: {cub.short_diagonal_calculation_length_height} { unit}')
    else:
        print(f'Face diagonal with length and width: {cub.short_diagonal_calculation_length_width()} {unit}')
        print(f'Face diagonal with width and height: {cub.short_diagonal_calculation_width_height()} {unit}')
        print(f'Face diagonal with length and height: {cub.short_diagonal_calculation_length_height()} {unit}')
    
def spheres():
    sphere_type: list[str] = ['Solid sphere', 'Hemisphere', 'Hollow sphere', 'Hollow hemisphere']
    s_type = None
    while s_type not in sphere_type:
        s_type = input('Solid sphere / Hemisphere / Hollow sphere / Hollow hemisphere').capitalize()
        pie = math.pi
        if s_type == 'Solid sphere':
            radius = float(input('Radius: '))
            sph = Sphere(pie, radius)
            print(f'Voume: {sph.volume_calculation()} {unit} cube')
            print(f'Area: {sph.area_calculation()} {unit} square')
        elif s_type == 'Hemisphere':
            radius = float(input('Radius: '))
            hemsph = Hemisphere(pie, radius)
            print(f'Volume: {hemsph.volume_hemisphere_calculation()} {unit} cube')
            print(f'Curved surface area {hemsph.curved_surface_area_hemisphere_calculation()} {unit} square')
            print(f'Total surface area {hemsph.total_surface_area_hemisphere_calculation()} {unit} square')
        elif s_type == 'Hollow sphere':
            out_radius = float(input('Outer Radius: '))
            in_radius = float(input('Inner Radius: '))
            hollosph = Hollow_sphere(pie, in_radius, out_radius, 0)
            if out_radius > in_radius:
                print(f'Volume: {hollosph.volume_hollow_sphere_calculation()} {unit} cube')
                print(f'Area: {hollosph.area_hollow_sphere_calculation()} {unit} square')
        elif s_type == 'Hollow hemispher':
            out_radius = float(input('Outer Radius: '))
            in_radius = float(input('Inner Radius: '))
            hollohemi = Hollow_hemisphere(pie, out_radius, in_radius,0)
            if out_radius > in_radius:
                print(f'Volume: {hollohemi.volume_hollow_hemisphere_calculation()} {unit} cube')
                print(f'Curved surface area: {Hemisphere.curved_surface_area_hemisphere_calculation()} {unit} square')
                print(f'Total surface area: {hollohemi.total_hollow_hemisphere_calculation()} {unit} square')
        else:
            print('Please check the speeling or \nprovide a valid input.')

def cylinder():
    cylinder_type: list[str] = ["Cylinder", "Hollow cylinder"]
    c_type = None
    while c_type not in cylinder_type:
        c_type = input('Solid cylinder / Hollow cylinder').capitalize()
        pie = math.pi
        if c_type == 'Solid cylinder':
            radius = float(input('Radius: '))
            height = float(input('Height: '))
            cyl = Cylinder(pie, radius, height)
            print(f'Volume: {cyl.volume_calculation()} {unit} cube')
            print(f'Curved surface area: {cyl.curved_surface_area_calculation()} square')
            print(f'Total surface area: {cyl.total_surface_area_calculation()} {unit} square')
        elif c_type == 'Hollow sphere':
            out_radius = float(input('Outer Radius: '))
            in_radius = float(input('Inner Radius'))
            height = float(input('Height: '))
            hollowcyl = Hollow_cylinder(pie, in_radius, out_radius, 0)
            if out_radius > in_radius:
                print(f'Volume: {hollowcyl.volume_calculation()} {unit} cube')
                print(f'Curved surface area: {hollowcyl.curved_surface_area_calculation()} {unit} square')
                print(f'Total surface area: {hollowcyl.total_surface_area_calculation()} {unit} square')
        else:
            print('Please check the spelling or \nprovide a valid input.')

def cone():
    pie = math.pi
    radius = float(input('Radius: '))
    height = float(input('Height: '))
    con = Cone(pie, radius, height)
    print(f'Volume: {con.volume_calculation()} {unit} cube')
    print(f'Curved surface area: {con.curved_surface_area_calculation()} {unit} square')
    print(f'Total surface area: {con.total_surface_area_calculation()} {unit} square')
    print(f'Slant height: {con.slant_height_calculation()} {unit}')

def frustum():
    pie = math.pi
    small_radius = float(input('Small Radius: '))
    big_radius = float(input('Big Radius: '))
    height = float(input('Height: '))
    frus = Frustum(pie, 0, small_radius, big_radius, height)
    if big_radius > small_radius:
        print(f'Volume: {frus.volume_calculation()} {unit} cube')
        print(f'Total surface area: {frus.total_surface_area_calculation()} {unit} square')
        print(f'Curved suface area: {frus.curved_surface_area()} {unit} square')
        print(f'Slant Height {frus.slant_height_calculation()} {unit}')
        
def main():
    while True:
        try:
            Dimensions: list[str] = ['Two dimensrion', 'Three dimension']
            dimensions = None
            while dimensions not in Dimensions:
                dimensions = input('Two dimension / Three dimension: ').capitalize()
                if dimensions == 'Two dimension':
                    Two_dimension_type: list[str] = ['Quadrilateral', 'Triangle', 'Circle']
                    two_dimension_types = None
                    while two_dimension_types not in Two_dimension_type:
                        two_dimension_types = input('Quadrilateral / Triangle / Circle: ').capitalize()
                        if two_dimension_types == 'Quadrilateral':
                            Quadrilateral_Types: list[str] = ['Quadrilateral', 'Rectangle', 'Trapezium']
                            quadrilateral_types = None
                            while quadrilateral_types not in Quadrilateral_Types:
                                quadrilateral_types = input('Quadrilateral / Rectangle / Trapezium: ').capitalize()

                                if quadrilateral_types == 'Quadrilateral':
                                    quaderilateral()
                                elif quadrilateral_types == 'Rectange':
                                    rectangle()
                                elif quadrilateral_types == 'Trapezium':
                                    trapezium()
                                else:
                                    print('Please check the speeling or\nprovid a vaolid input.')
                            
                        elif two_dimension_types == 'Triagle':
                            triangles()
                        elif two_dimension_types == 'Circle':
                            circle()
                elif dimensions == 'Three dimension':
                    Three_Dimension_Types: list[str] = ["Cuboid", "Sphere", "Cylinder", "Cone", "Frustum"]
                    three_dimension_types = None
                    while three_dimension_types not in Three_Dimension_Types:
                        three_dimension_types = input("Cuboid / Sphere / Cylinder/ Cone / Frustum : ").capitalize()
                        if three_dimension_types == "Cuboid":
                            cuboid()
                        elif three_dimension_types == 'Sphere':
                            spheres()
                        elif three_dimension_types == 'Cylinder':
                            cylinder()
                        elif three_dimension_types == 'Cone':
                            cone()
                        elif three_dimension_types == 'Frustum':
                            frustum()
                        else:
                            print('Please check the seplling or\nprobide a valid input')
                else:
                    print('Please check the seplling or\nprobide a valid input')

        except (AttributeError, TypeError, ArithmeticError):
            print('')
        Again: list[str] = ['Yes', 'Ya', 'Yep', 'Ha']
        again = input('Do you want to do this again? (Yes / No): ').capitalize()
        if again not in Again:
            break

if __name__ == '__main__':
    main()

print('Byeee!!!!!')
