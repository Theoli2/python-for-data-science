import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI for each height/weight pair.

    Args:
        height: List of heights in meters
        weight: List of weights in kilograms

    Raises:
        TypeError: If height or weight values are not int or float
        ValueError: If lists have different lengths or contain non-positive
         values

    Returns:
        List of BMI values (weight / height²)
    """
    if any(type(h) not in (int, float)
           for h in height):
        raise TypeError("Height values must be int or float")

    if any(type(w) not in (int, float)
           for w in weight):
        raise TypeError("Weight values must be int or float")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have same length")

    if any(h <= 0 for h in height):
        raise ValueError("Height values must be positive")

    if any(w <= 0 for w in weight):
        raise ValueError("Weight values must be positive")

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check which BMI values exceed a limit.

    Args:
        bmi: List of BMI values
        limit: The threshold to compare against

    Raises:
        TypeError: If limit is not an int or bmi contains non-numeric values

    Returns:
        List of booleans indicating if each BMI exceeds the limit
    """
    if type(limit) is not int:
        raise TypeError("Limit value must be int")

    if any(type(elem) not in (int, float)
           for elem in bmi):
        raise TypeError("List values must be int or float")

    return (np.array(bmi) > limit).tolist()
