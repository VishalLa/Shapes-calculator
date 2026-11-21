"""Unit handling for displaying results."""

from __future__ import annotations

from .shapes import Dimension

UNITS: dict[str, str] = {"Meter": "m", "Centimeter": "cm", "Foot": "ft"}
DEFAULT_UNIT = "Meter"

_EXPONENTS: dict[Dimension, str] = {
    Dimension.LENGTH: "",
    Dimension.AREA: "²",
    Dimension.VOLUME: "³",
}


def format_unit(unit_name: str, dimension: Dimension = Dimension.LENGTH) -> str:
    """Return e.g. ``"cm²"`` for ``("Centimeter", Dimension.AREA)``."""
    return UNITS[unit_name] + _EXPONENTS[dimension]
