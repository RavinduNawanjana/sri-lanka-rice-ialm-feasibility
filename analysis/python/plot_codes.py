"""Parse and validate compact experimental plot identifiers.

The public outcome table uses codes such as ``L1IR2F3R1``.  Parsing them
programmatically prevents manual copy/paste errors and keeps factor extraction
auditable.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

_PATTERN = re.compile(r"^(L[12])(IR[12])(F[1-4])(R[12])$")


@dataclass(frozen=True)
class PlotCode:
    plot_code: str
    tillage_code: str
    irrigation_code: str
    fertilizer_code: str
    replicate_code: str


def parse_plot_code(value: str) -> PlotCode:
    """Return the four experimental factors encoded in *value*.

    Raises
    ------
    ValueError
        If the identifier is missing or falls outside the documented
        ``L[12] x IR[12] x F[1-4] x R[12]`` code grid.
    """
    code = (value or "").strip()
    match = _PATTERN.fullmatch(code)
    if not match:
        raise ValueError(
            f"Invalid plot code {value!r}; expected L[12]IR[12]F[1-4]R[12]."
        )
    return PlotCode(code, *match.groups())


def expected_plot_codes() -> set[str]:
    return {
        f"{l}{ir}{f}{r}"
        for l in ("L1", "L2")
        for ir in ("IR1", "IR2")
        for f in ("F1", "F2", "F3", "F4")
        for r in ("R1", "R2")
    }
