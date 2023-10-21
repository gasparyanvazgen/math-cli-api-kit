"""This module provides classes for algebraic and geometric operations,
offering a set of basic math calculations.
"""

from typing import Union

from math_cli_api_kit.core.constants import PI, E
from math_cli_api_kit.core.validation import validate_int_or_float, \
    validate_factorial


class Algebra:
    """Provides algebraic operations: `addition`, `subtraction`,
    `multiplication`, `division`, and `powers`.

    This class focuses on basic algebraic operations and may not cover
    advanced topics. For more complex algebraic tasks, consider
    specialized libraries or frameworks.
    """

    def __init__(self):
        pass

    def sum(
            self, x: Union[int, float], y: Union[int, float]
    ) -> Union[int, float]:
        """Return the sum of x and y."""
        if validate_int_or_float(x, y):
            return x + y

    def sub(
            self, x: Union[int, float], y: Union[int, float]
    ) -> Union[int, float]:
        """Return the subtraction of x by y."""
        if validate_int_or_float(x, y):
            return x - y

    def mul(
            self, x: Union[int, float], y: Union[int, float]
    ) -> Union[int, float]:
        """Return the multiplication of x by y."""
        if validate_int_or_float(x, y):
            return x * y

    def div(
            self, x: Union[int, float], y: Union[int, float]
    ) -> Union[int, float]:
        """Return the division of x by y."""
        if validate_int_or_float(x, y):
            return x / y

    def pow(
            self, x: Union[int, float], y: Union[int, float]
    ) -> Union[int, float]:
        """Return x**y (x to the power of y)."""
        if validate_int_or_float(x, y):
            return x ** y

    def square_root(self, x: Union[int, float]) -> Union[int, float, complex]:
        """Return the square root of x."""
        return self.pow(x, 0.5)

    def factorial(self, x: int) -> int:
        """Find x!. Raises a ValueError if x is negative or
        non-integral."""
        if validate_factorial(x):
            if x in (0, 1):
                return 1
            else:
                return x * self.factorial(x - 1)

    def exp(self, x: Union[int, float]) -> Union[int, float]:
        """Return e raised to the power of x."""
        return self.pow(E, x)


class Geometry:
    """Provides geometric operations: surface of a `square`, `circle`,
    `triangle`, `trapezoid`, and `hypotenuse`.

    This class focuses on basic geometric operations and may not cover
    advanced topics. For more complex geometric tasks, consider
    specialized libraries or frameworks.
    """

    def __init__(self):
        self.__algebra = Algebra()

    def surface_of_square(self, a: Union[int, float]) -> Union[int, float]:
        """Return the surface of square."""
        return self.__algebra.pow(a, 2)

    def surface_of_circle(self, r: Union[int, float]) -> Union[int, float]:
        """Return the surface of a circle."""
        return PI * self.__algebra.pow(r, 2)

    def surface_of_triangle(
            self, b: Union[int, float], h: Union[int, float]
    ) -> Union[int, float]:
        """Return the surface of a triangle."""
        return self.__algebra.div(self.__algebra.mul(b, h), 2)

    def surface_of_trapezoid(
            self, a: Union[int, float],
            b: Union[int, float], h: Union[int, float]
    ) -> Union[int, float]:
        """Return the surface of a trapezoid."""
        return self.__algebra.mul(
            self.__algebra.div(self.__algebra.sum(a, b), 2), h
        )

    def hypotenuse(
            self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """The square of the hypotenuse is equal to the sum of the areas
        of the squares on the other two sides. Return the hypotenuse of
        a triangle.
        """
        return self.__algebra.square_root(
            self.__algebra.sum(
                self.__algebra.pow(a, 2), self.__algebra.pow(b, 2)
            )
        )
