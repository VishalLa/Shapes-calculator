from __future__ import annotations

import math
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from enum import IntEnum


class ShapeError(ValueError):
    """Raised when the given dimensions do not describe a valid shape."""


class Dimension(IntEnum):
    """Physical dimension of a measurement (used to pick the unit exponent)."""

    LENGTH = 1
    AREA = 2
    VOLUME = 3


@dataclass(frozen=True)
class Measurement:
    """A single labelled result, e.g. ``Measurement("Area", 12.5, Dimension.AREA)``."""
    label: str
    value: float
    dimension: Dimension


def _length(label: str, value: float) -> Measurement:
    return Measurement(label, value, Dimension.LENGTH)


def _area(label: str, value: float) -> Measurement:
    return Measurement(label, value, Dimension.AREA)


def _volume(label: str, value: float) -> Measurement:
    return Measurement(label, value, Dimension.VOLUME)


def _require_positive(**values: float) -> None:
    for name, value in values.items():
        if not math.isfinite(value) or value <= 0:
            pretty = name.replace("_", " ").capitalize()
            raise ShapeError(f"{pretty} must be a positive number.")


def _require_triangle(a: float, b: float, c: float) -> None:
    if a + b <= c or a + c <= b or b + c <= a:
        raise ShapeError(
            "Invalid triangle: the sum of any two sides must be greater "
            "than the third side."
        )


def _require_outer_larger(outer: float, inner: float) -> None:
    if outer <= inner:
        raise ShapeError("Outer radius must be larger than inner radius.")


def _heron(a: float, b: float, c: float) -> float:
    """Area of a triangle from its three sides (Heron's formula)."""
    s = (a + b + c) / 2
    return math.sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))


class Shape(ABC):
    """Base class for every shape."""

    @abstractmethod
    def measurements(self) -> list[Measurement]:
        """Return every value this shape can calculate."""

    def description(self) -> str:
        """Optional human-readable note (e.g. "Square" or "Isosceles")."""
        return ""


@dataclass(frozen=True)
class CyclicQuadrilateral(Shape):
    """Quadrilateral from four consecutive sides, assuming it is cyclic.

    A quadrilateral is not fixed by its four sides alone, so (like the
    original program) this uses Brahmagupta's formula, which assumes all four
    corners lie on one circle. Diagonals follow from Ptolemy's theorem.
    """

    side_1: float
    side_2: float
    side_3: float
    side_4: float

    def __post_init__(self) -> None:
        _require_positive(side_1=self.side_1, side_2=self.side_2, side_3=self.side_3, side_4=self.side_4)
        sides = (self.side_1, self.side_2, self.side_3, self.side_4)
        if max(sides) >= sum(sides) - max(sides):
            raise ShapeError(
                "Invalid quadrilateral: the longest side must be shorter "
                "than the sum of the other three."
            )

    def perimeter(self) -> float:
        return self.side_1 + self.side_2 + self.side_3 + self.side_4

    def area(self) -> float:
        s = self.perimeter() / 2
        product = (
            (s - self.side_1) * (s - self.side_2)
            * (s - self.side_3) * (s - self.side_4)
        )
        return math.sqrt(max(0.0, product))

    def diagonals(self) -> tuple[float, float]:
        a, b, c, d = self.side_1, self.side_2, self.side_3, self.side_4
        p = math.sqrt((a * c + b * d) * (a * d + b * c) / (a * b + c * d))
        q = math.sqrt((a * c + b * d) * (a * b + c * d) / (a * d + b * c))
        return p, q

    def description(self) -> str:
        a, b, c, d = self.side_1, self.side_2, self.side_3, self.side_4
        if a == b == c == d:
            return "Square"
        if a == c and b == d:
            return "Rectangle"
        return "Cyclic quadrilateral"

    def measurements(self) -> list[Measurement]:
        diagonal_1, diagonal_2 = self.diagonals()
        return [
            _area("Area", self.area()),
            _length("Perimeter", self.perimeter()),
            _length("Diagonal 1", diagonal_1),
            _length("Diagonal 2", diagonal_2),
        ]


@dataclass(frozen=True)
class Rectangle(Shape):
    length: float
    width: float

    def __post_init__(self) -> None:
        _require_positive(length=self.length, width=self.width)

    def description(self) -> str:
        return "Square" if self.length == self.width else "Rectangle"

    def measurements(self) -> list[Measurement]:
        return [
            _area("Area", self.length * self.width),
            _length("Perimeter", 2 * (self.length + self.width)),
            _length("Diagonal", math.hypot(self.length, self.width)),
        ]


@dataclass(frozen=True)
class Trapezium(Shape):
    """Trapezium (trapezoid) from its two parallel sides and its two legs."""

    base_1: float
    base_2: float
    leg_1: float
    leg_2: float

    def __post_init__(self) -> None:
        _require_positive(base_1=self.base_1, base_2=self.base_2, leg_1=self.leg_1, leg_2=self.leg_2)
        if self.base_1 == self.base_2:
            raise ShapeError(
                "The parallel sides must differ in length (equal parallel "
                "sides make a parallelogram, whose height cannot be found "
                "from the side lengths alone)."
            )
        _require_triangle(abs(self.base_1 - self.base_2), self.leg_1, self.leg_2)

    @property
    def height(self) -> float:
        diff = abs(self.base_1 - self.base_2)
        return 2 * _heron(diff, self.leg_1, self.leg_2) / diff

    def diagonals(self) -> tuple[float, float]:
        long_base = max(self.base_1, self.base_2)
        short_base = min(self.base_1, self.base_2)
        diff = long_base - short_base
        # Horizontal offset of the top-left corner from the bottom-left corner.
        offset = (diff**2 + self.leg_1**2 - self.leg_2**2) / (2 * diff)
        return (
            math.hypot(offset + short_base, self.height),
            math.hypot(long_base - offset, self.height),
        )

    def measurements(self) -> list[Measurement]:
        diagonal_1, diagonal_2 = self.diagonals()
        return [
            _area("Area", (self.base_1 + self.base_2) / 2 * self.height),
            _length("Perimeter", self.base_1 + self.base_2 + self.leg_1 + self.leg_2),
            _length("Height", self.height),
            _length("Diagonal 1", diagonal_1),
            _length("Diagonal 2", diagonal_2),
        ]


@dataclass(frozen=True)
class EquilateralTriangle(Shape):
    side: float

    def __post_init__(self) -> None:
        _require_positive(side=self.side)

    def measurements(self) -> list[Measurement]:
        return [
            _area("Area", math.sqrt(3) / 4 * self.side**2),
            _length("Perimeter", 3 * self.side),
            _length("Height", math.sqrt(3) / 2 * self.side),
        ]


@dataclass(frozen=True)
class IsoscelesTriangle(Shape):
    equal_side: float
    base: float

    def __post_init__(self) -> None:
        _require_positive(equal_side=self.equal_side, base=self.base)
        _require_triangle(self.equal_side, self.equal_side, self.base)

    def measurements(self) -> list[Measurement]:
        height_on_base = math.sqrt(self.equal_side**2 - (self.base / 2) ** 2)
        area = self.base * height_on_base / 2
        return [
            _area("Area", area),
            _length("Perimeter", 2 * self.equal_side + self.base),
            _length("Height on the base", height_on_base),
            _length("Height on an equal side", 2 * area / self.equal_side),
        ]


@dataclass(frozen=True)
class Triangle(Shape):
    """Any triangle from its three sides (equilateral / isosceles / scalene)."""

    side_1: float
    side_2: float
    side_3: float

    def __post_init__(self) -> None:
        _require_positive(side_1=self.side_1, side_2=self.side_2, side_3=self.side_3)
        _require_triangle(self.side_1, self.side_2, self.side_3)

    def description(self) -> str:
        a, b, c = self.side_1, self.side_2, self.side_3
        if a == b == c:
            return "Equilateral triangle"
        if a == b or b == c or a == c:
            return "Isosceles triangle"
        return "Scalene triangle"

    def measurements(self) -> list[Measurement]:
        area = _heron(self.side_1, self.side_2, self.side_3)
        return [
            _area("Area", area),
            _length("Perimeter", self.side_1 + self.side_2 + self.side_3),
            _length("Height on side 1", 2 * area / self.side_1),
            _length("Height on side 2", 2 * area / self.side_2),
            _length("Height on side 3", 2 * area / self.side_3),
        ]


@dataclass(frozen=True)
class Circle(Shape):
    radius: float

    def __post_init__(self) -> None:
        _require_positive(radius=self.radius)

    def measurements(self) -> list[Measurement]:
        return [
            _area("Area", math.pi * self.radius**2),
            _length("Circumference", 2 * math.pi * self.radius),
            _length("Diameter", 2 * self.radius),
        ]


@dataclass(frozen=True)
class Cuboid(Shape):
    length: float
    width: float
    height: float

    def __post_init__(self) -> None:
        _require_positive(length=self.length, width=self.width, height=self.height)

    def description(self) -> str:
        return "Cube" if self.length == self.width == self.height else "Cuboid"

    def measurements(self) -> list[Measurement]:
        l, w, h = self.length, self.width, self.height
        return [
            _volume("Volume", l * w * h),
            _area("Lateral surface area", 2 * h * (l + w)),
            _area("Total surface area", 2 * (l * w + w * h + l * h)),
            _length("Body (space) diagonal", math.sqrt(l**2 + w**2 + h**2)),
            _length("Face diagonal (length × width)", math.hypot(l, w)),
            _length("Face diagonal (width × height)", math.hypot(w, h)),
            _length("Face diagonal (length × height)", math.hypot(l, h)),
        ]


@dataclass(frozen=True)
class Sphere(Shape):
    radius: float

    def __post_init__(self) -> None:
        _require_positive(radius=self.radius)

    def measurements(self) -> list[Measurement]:
        return [
            _volume("Volume", 4 / 3 * math.pi * self.radius**3),
            _area("Surface area", 4 * math.pi * self.radius**2),
        ]


@dataclass(frozen=True)
class HollowSphere(Shape):
    outer_radius: float
    inner_radius: float

    def __post_init__(self) -> None:
        _require_positive(outer_radius=self.outer_radius, inner_radius=self.inner_radius)
        _require_outer_larger(self.outer_radius, self.inner_radius)

    def measurements(self) -> list[Measurement]:
        big, small = self.outer_radius, self.inner_radius
        return [
            _volume("Material volume", 4 / 3 * math.pi * (big**3 - small**3)),
            _area("Outer surface area", 4 * math.pi * big**2),
            _area("Inner surface area", 4 * math.pi * small**2),
            _area("Total surface area", 4 * math.pi * (big**2 + small**2)),
        ]


@dataclass(frozen=True)
class Hemisphere(Shape):
    radius: float

    def __post_init__(self) -> None:
        _require_positive(radius=self.radius)

    def measurements(self) -> list[Measurement]:
        r = self.radius
        return [
            _volume("Volume", 2 / 3 * math.pi * r**3),
            _area("Curved surface area", 2 * math.pi * r**2),
            _area("Total surface area", 3 * math.pi * r**2),
        ]


@dataclass(frozen=True)
class HollowHemisphere(Shape):
    outer_radius: float
    inner_radius: float

    def __post_init__(self) -> None:
        _require_positive(outer_radius=self.outer_radius, inner_radius=self.inner_radius)
        _require_outer_larger(self.outer_radius, self.inner_radius)

    def measurements(self) -> list[Measurement]:
        big, small = self.outer_radius, self.inner_radius
        curved = 2 * math.pi * (big**2 + small**2)
        ring = math.pi * (big**2 - small**2)
        return [
            _volume("Material volume", 2 / 3 * math.pi * (big**3 - small**3)),
            _area("Curved surface area", curved),
            _area("Total surface area", curved + ring),
        ]


@dataclass(frozen=True)
class Cylinder(Shape):
    radius: float
    height: float

    def __post_init__(self) -> None:
        _require_positive(radius=self.radius, height=self.height)

    def measurements(self) -> list[Measurement]:
        r, h = self.radius, self.height
        return [
            _volume("Volume", math.pi * r**2 * h),
            _area("Curved surface area", 2 * math.pi * r * h),
            _area("Total surface area", 2 * math.pi * r * (r + h)),
        ]


@dataclass(frozen=True)
class HollowCylinder(Shape):
    outer_radius: float
    inner_radius: float
    height: float

    def __post_init__(self) -> None:
        _require_positive(
            outer_radius=self.outer_radius,
            inner_radius=self.inner_radius,
            height=self.height,
        )
        _require_outer_larger(self.outer_radius, self.inner_radius)

    def measurements(self) -> list[Measurement]:
        big, small, h = self.outer_radius, self.inner_radius, self.height
        curved = 2 * math.pi * h * (big + small)
        ends = 2 * math.pi * (big**2 - small**2)
        return [
            _volume("Material volume", math.pi * h * (big**2 - small**2)),
            _area("Curved surface area (outer + inner)", curved),
            _area("Total surface area", curved + ends),
        ]


@dataclass(frozen=True)
class Cone(Shape):
    radius: float
    height: float

    def __post_init__(self) -> None:
        _require_positive(radius=self.radius, height=self.height)

    def slant_height(self) -> float:
        return math.hypot(self.radius, self.height)

    def measurements(self) -> list[Measurement]:
        r, h, slant = self.radius, self.height, self.slant_height()
        return [
            _volume("Volume", math.pi * r**2 * h / 3),
            _area("Curved surface area", math.pi * r * slant),
            _area("Total surface area", math.pi * r * (r + slant)),
            _length("Slant height", slant),
        ]


@dataclass(frozen=True)
class Frustum(Shape):
    """Frustum of a cone (a cone with its tip cut off)."""

    small_radius: float
    big_radius: float
    height: float

    def __post_init__(self) -> None:
        _require_positive(
            small_radius=self.small_radius,
            big_radius=self.big_radius,
            height=self.height,
        )
        if self.big_radius <= self.small_radius:
            raise ShapeError("Big radius must be larger than small radius.")

    def slant_height(self) -> float:
        return math.hypot(self.height, self.big_radius - self.small_radius)

    def measurements(self) -> list[Measurement]:
        small, big, h = self.small_radius, self.big_radius, self.height
        curved = math.pi * (small + big) * self.slant_height()
        return [
            _volume("Volume", math.pi * h / 3 * (small**2 + big**2 + small * big)),
            _area("Curved surface area", curved),
            _area("Total surface area", curved + math.pi * (small**2 + big**2)),
            _length("Slant height", self.slant_height()),
        ]


TWO_D = "Two-dimensional"
THREE_D = "Three-dimensional"
CATEGORIES: tuple[str, ...] = (TWO_D, THREE_D)


@dataclass(frozen=True)
class ShapeSpec:
    """Describes a shape for the UI: its name, category and input fields.

    The order of ``fields`` must match the constructor arguments of ``factory``.
    """

    name: str
    category: str
    fields: tuple[str, ...]
    factory: Callable[..., Shape]

    def create(self, *values: float) -> Shape:
        return self.factory(*values)


SHAPES: tuple[ShapeSpec, ...] = (
    ShapeSpec("Cyclic quadrilateral", TWO_D, ("Side 1", "Side 2", "Side 3", "Side 4"), CyclicQuadrilateral),
    ShapeSpec("Rectangle", TWO_D, ("Length", "Width"), Rectangle),
    ShapeSpec("Trapezium", TWO_D, ("Parallel side 1", "Parallel side 2", "Leg 1", "Leg 2"), Trapezium),
    ShapeSpec("Equilateral triangle", TWO_D, ("Side",), EquilateralTriangle),
    ShapeSpec("Isosceles triangle", TWO_D, ("Equal side", "Base"), IsoscelesTriangle),
    ShapeSpec("Triangle (3 sides)", TWO_D, ("Side 1", "Side 2", "Side 3"), Triangle),
    ShapeSpec("Circle", TWO_D, ("Radius",), Circle),
    ShapeSpec("Cuboid / Cube", THREE_D, ("Length", "Width", "Height"), Cuboid),
    ShapeSpec("Sphere", THREE_D, ("Radius",), Sphere),
    ShapeSpec("Hollow sphere", THREE_D, ("Outer radius", "Inner radius"), HollowSphere),
    ShapeSpec("Hemisphere", THREE_D, ("Radius",), Hemisphere),
    ShapeSpec("Hollow hemisphere", THREE_D, ("Outer radius", "Inner radius"), HollowHemisphere),
    ShapeSpec("Cylinder", THREE_D, ("Radius", "Height"), Cylinder),
    ShapeSpec("Hollow cylinder", THREE_D, ("Outer radius", "Inner radius", "Height"), HollowCylinder),
    ShapeSpec("Cone", THREE_D, ("Radius", "Height"), Cone),
    ShapeSpec("Frustum", THREE_D, ("Small radius", "Big radius", "Height"), Frustum),
)


def shapes_in(category: str) -> list[ShapeSpec]:
    """Return every registered shape that belongs to ``category``."""
    return [spec for spec in SHAPES if spec.category == category]
