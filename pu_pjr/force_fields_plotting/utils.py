from enum import Enum

class Fields(Enum):
    LJ_CUT = 'lj/cut'

def create_range(
    start: float = 0.1, end: float = 3.0, items: int = 30
) -> list[float]:
    """Return a float range between 'start' and 'end'"""
    # Check end is bigger than start
    if start > end:
        raise ValueError("start value is bigger than end value")
    
    # Check that items is bigger than 1
    if items <= 1:
        raise ValueError("items value must be bigger than 1")

    step_val = (end - start) / (items - 1)
    range_vals = []
    for i in range(items):
        range_vals.append(start + step_val*i)

    return range_vals

def lj_cut(
    points: list[float], epsilon: float, sigma: float, cut: float
) -> list[float | None]:
    """Lennard-Jones potential with a cut-off at `cut`"""

    values = []
    for r in points:
        if r < cut:
            values.append(4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6))
        else:
            values.append(None)

    return values