import math

import pytest

from shapes_calculator.shapes import (
    SHAPES, Circle, Cone, CyclicQuadrilateral, Cuboid, Frustum, HollowCylinder,
    Rectangle, Shape, ShapeError, Sphere, Triangle, Trapezium,
)


def value(shape: Shape, label: str) -> float:
    return next(m.value for m in shape.measurements() if m.label == label)


def test_rectangle() -> None:
    rect = Rectangle(3, 4)
    assert value(rect, "Area") == 12
    assert value(rect, "Perimeter") == 14
    assert value(rect, "Diagonal") == 5


def test_circle() -> None:
    assert value(Circle(2), "Area") == pytest.approx(4 * math.pi)


def test_cyclic_quadrilateral_square() -> None:
    quad = CyclicQuadrilateral(2, 2, 2, 2)
    assert quad.description() == "Square"
    assert value(quad, "Area") == pytest.approx(4)
    assert value(quad, "Diagonal 1") == pytest.approx(math.sqrt(8))


def test_trapezium_isosceles() -> None:
    trap = Trapezium(5, 1, math.sqrt(5), math.sqrt(5))
    assert trap.height == pytest.approx(1)
    assert value(trap, "Area") == pytest.approx(3)
    assert value(trap, "Diagonal 1") == pytest.approx(math.sqrt(10))


def test_triangle_3_4_5() -> None:
    tri = Triangle(3, 4, 5)
    assert tri.description() == "Scalene triangle"
    assert value(tri, "Area") == pytest.approx(6)
    assert value(tri, "Height on side 3") == pytest.approx(2.4)


def test_invalid_triangle() -> None:
    with pytest.raises(ShapeError):
        Triangle(1, 2, 10)


@pytest.mark.parametrize("bad", [0, -1, float("nan"), float("inf")])
def test_rejects_bad_numbers(bad: float) -> None:
    with pytest.raises(ShapeError):
        Circle(bad)


def test_cube_detection() -> None:
    assert Cuboid(2, 2, 2).description() == "Cube"
    assert value(Cuboid(1, 2, 3), "Volume") == 6


def test_sphere_volume() -> None:
    assert value(Sphere(3), "Volume") == pytest.approx(36 * math.pi)


def test_hollow_cylinder() -> None:
    cyl = HollowCylinder(3, 2, 10)
    assert value(cyl, "Material volume") == pytest.approx(50 * math.pi)
    with pytest.raises(ShapeError):
        HollowCylinder(2, 3, 10)


def test_cone_slant() -> None:
    assert value(Cone(3, 4), "Slant height") == pytest.approx(5)


def test_frustum_volume() -> None:
    assert value(Frustum(1, 3, 2), "Volume") == pytest.approx(26 * math.pi / 3)


SAMPLES: dict[str, tuple[float, ...]] = {
    "Cyclic quadrilateral": (3, 4, 5, 4),
    "Rectangle": (3, 4),
    "Trapezium": (6, 3, 4, 4),
    "Equilateral triangle": (3,),
    "Isosceles triangle": (5, 6),
    "Triangle (3 sides)": (3, 4, 5),
    "Circle": (2,),
    "Cuboid / Cube": (1, 2, 3),
    "Sphere": (2,),
    "Hollow sphere": (3, 2),
    "Hemisphere": (2,),
    "Hollow hemisphere": (3, 2),
    "Cylinder": (2, 5),
    "Hollow cylinder": (3, 2, 5),
    "Cone": (3, 4),
    "Frustum": (1, 3, 2),
}


@pytest.mark.parametrize("spec", SHAPES, ids=lambda s: s.name)
def test_every_registered_shape_works(spec) -> None:  # type: ignore[no-untyped-def]
    values = SAMPLES[spec.name]
    assert len(values) == len(spec.fields)
    results = spec.create(*values).measurements()
    assert results and all(m.value > 0 for m in results)
