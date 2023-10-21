"""This module provides functions for validating attributes used in
math operations.

It includes checks for data types, such as integers and floats, as well
as functions for validating strings that represent numbers.
"""

from typing import Union, Any


def get_object_type_name(obj: Any) -> str:
    """Return the type name of an object as a string."""
    return type(obj).__name__


def validate_int_or_float(x: Union[int, float], y: Union[int, float]) -> bool:
    """Validate the attributes x and y and raise an error if they are
    not valid.
    """

    if (get_object_type_name(x) not in ("int", "float")) or \
            (get_object_type_name(y) not in ("int", "float")):
        raise TypeError(f"unsupported operand type(s) for operands x and y: "
                        f"'{get_object_type_name(x)}' and"
                        f"'{get_object_type_name(y)}'. Expected int or float.")
    return True


def validate_factorial(x: int) -> bool:
    """Validate the attribute x and raise an error if it is
    not valid.
    """
    if not isinstance(x, int):
        raise TypeError(f"unsupported operand type(s) for x!: "
                        f"'{get_object_type_name(x)}'. Expected int.")
    if x < 0:
        raise ValueError(f"{x} is negative or non-integral.")
    return True


def is_numeric_string(s: str) -> bool:
    """Check if the number in the string is valid."""
    s = s.strip()
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_integer_string(s: str) -> bool:
    """Check if the number in the string is an integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False


def all_not_none_and_numeric(*args: str) -> bool:
    """Check that the values in the arguments are not None and
    are numeric.
    """
    return all(arg is not None and is_numeric_string(arg) for arg in args)


def all_not_none_and_integer(*args: str) -> bool:
    """Check that the values in the arguments are not None and
    are integers.
    """
    return all(arg is not None and is_integer_string(arg) for arg in args)
