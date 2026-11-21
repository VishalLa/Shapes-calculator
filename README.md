# Shapes Calculator

A desktop app (Python + Tkinter) that calculates area, perimeter, volume, surface area,
heights, diagonals and more for common 2D and 3D shapes.

> **This was the first program I ever wrote.** I built it when I started learning to
> program, and later rewrote it with type hints, a clean structure, tests and a GUI.
> The original console version is kept in [`legacy/`](legacy/) so you can see how far it has come.

## Features

| 2D | 3D |
|----|----|
| Cyclic quadrilateral, Rectangle / Square, Trapezium | Cuboid / Cube |
| Equilateral, Isosceles and any triangle (3 sides) | Sphere, Hollow sphere |
| Circle | Hemisphere, Hollow hemisphere |
| | Cylinder, Hollow cylinder |
| | Cone, Frustum |

- Choose the unit: meter, centimeter or foot (results use the right m / m² / m³ exponent)
- Input validation with clear error messages (invalid triangles, negative numbers, wrong radii, ...)
- Automatic shape detection (square, cube, equilateral / isosceles / scalene, ...)
- Press **Enter** to calculate

## Run it

Requires Python 3.9+. Tkinter ships with Python on Windows and macOS; on Debian/Ubuntu
install it with `sudo apt install python3-tk`.

```bash
git clone https://github.com/VishalLa/shapes-calculator.git
cd shapes-calculator
python -m shapes_calculator
```

No third-party dependencies.

## Project structure

```
shapes_calculator/
├── shapes.py    # typed, validated shape models + registry (no UI code)
├── units.py     # unit names and formatting
├── gui.py       # Tkinter interface, built from the shape registry
└── __main__.py  # python -m shapes_calculator
tests/           # pytest suite
legacy/          # my original first version
```

Each shape is a frozen `dataclass` that validates itself on creation and returns a list of
`Measurement(label, value, dimension)`. The GUI reads the `SHAPES` registry to build its input
form, so adding a new shape means writing one class and adding one registry line, with no UI changes.

## Development

```bash
pip install pytest mypy
python -m pytest
python -m mypy --strict shapes_calculator
```

## What changed from the original

Rewriting this was a good code review of my past self. Besides typing and structure, the
original had several maths and logic bugs that are now fixed:

- Trapezium area and diagonal formulas were wrong (and one used `** 4` instead of `** 2`)
- Equilateral height was `(s/2)² + s²` instead of `(√3/2)·s`
- Isosceles area was missing its square root
- Cone curved surface area included the base; frustum total area was wrong
- Several menu typos (`'Rectange'`, `'Triagle'`, `'Hollow hemispher'`, ...) meant some options could never be selected
- Methods were printed instead of called (`quad.parameter_calculation` without `()`)

## License

MIT
