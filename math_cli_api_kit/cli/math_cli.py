"""This module defines a command-line interface (CLI) for performing
math operations.

It provides both algebraic and geometric operations.
"""

import click

from math_cli_api_kit.core.math_operations import Algebra, Geometry
from math_cli_api_kit.core.validation import all_not_none_and_numeric

_algebra = Algebra()
_geometry = Geometry()


# algebra commands
@click.group("algebra")
def algebra():
    """Provides algebraic operations: `addition`, `subtraction`,
    `multiplication`, `division`, and `powers`.
    """


@algebra.command("sum", help="Return the sum of x and y.")
@click.option("-x", help="Calculate the sum by 'y'")
@click.option("-y", help="Calculate the sum by 'x'")
def sum(x: str, y: str) -> None:
    if all_not_none_and_numeric(x, y):
        print(_algebra.sum(float(x), float(y)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@algebra.command("sub", help="Return the subtraction of x by y.")
@click.option("-x", help="Calculate the subtraction by 'y'")
@click.option("-y", help="Calculate the subtraction by 'x'")
def sub(x: str, y: str) -> None:
    if all_not_none_and_numeric(x, y):
        print(_algebra.sub(float(x), float(y)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@algebra.command("mul", help="Return the multiplication of x by y.")
@click.option("-x", help="Calculate the multiplication by 'y'")
@click.option("-y", help="Calculate the multiplication by 'x'")
def mul(x: str, y: str) -> None:
    if all_not_none_and_numeric(x, y):
        print(_algebra.mul(float(x), float(y)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@algebra.command("div", help="Return the division of x by y.")
@click.option("-x", help="Calculate the division by 'y'")
@click.option("-y", help="Calculate the division by 'x'")
def div(x: str, y: str) -> None:
    if all_not_none_and_numeric(x, y):
        print(_algebra.div(float(x), float(y)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@algebra.command("pow", help="Return x**y (x to the power of y).")
@click.option("-x", help="Calculate x to the power of 'y'")
@click.option("-y", help="Calculate 'x' to the power of its")
def pow(x: str, y: str) -> None:
    if all_not_none_and_numeric(x, y):
        print(_algebra.pow(float(x), float(y)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@algebra.command("square_root", help="Return the square root of x.")
@click.option("-x", help="Calculate its square root")
def square_root(x: str) -> None:
    if all_not_none_and_numeric(x):
        print(_algebra.square_root(float(x)))
    else:
        print("You did not enter parameter or the parameter is not 'int'"
              " or 'float'")


@algebra.command("factorial", help="Find x! Raises a ValueError if x is"
                                   " negative or non-integral.")
@click.option("-x", help="Calculate its factorial")
def factorial(x: str) -> None:
    if all_not_none_and_numeric(x):
        print(_algebra.factorial(int(x)))
    else:
        print("You did not enter parameter or the parameter is not 'int'")


@algebra.command("exp", help="Return e raised to the power of x.")
@click.option("-x", help="Calculate 'e' raised to the power of its")
def exp(x: str) -> None:
    if all_not_none_and_numeric(x):
        print(_algebra.exp(float(x)))
    else:
        print("You did not enter parameter or the parameter is not 'int' or"
              " 'float'")


# geometry commands
@click.group("geometry")
def geometry():
    """Provides geometric operations: surface of a `square`, `circle`,
    `triangle`, `trapezoid`, and `hypotenuse`.
    """


@geometry.command("surface_of_square", help="Return the surface of square.")
@click.option("-a", help="Calculate the surface of a square")
def surface_of_square(a: str) -> None:
    if all_not_none_and_numeric(a):
        print(_geometry.surface_of_square(float(a)))
    else:
        print("You did not enter parameter or the parameter is not 'int' or"
              " 'float'")


@geometry.command("surface_of_circle", help="Return the surface of a circle.")
@click.option("-r", help="Calculate the surface of a circle by radius")
def surface_of_circle(r: str) -> None:
    if all_not_none_and_numeric(r):
        print(_geometry.surface_of_circle(float(r)))
    else:
        print("You did not enter parameter or the parameter is not 'int' or"
              " 'float'")


@geometry.command("surface_of_triangle", help="Return the surface of a"
                                              " triangle.")
@click.option("-b", help="Calculate the surface of a triangle by its base")
@click.option("-h", help="Calculate the surface of a triangle by its height")
def surface_of_triangle(b: str, h: str) -> None:
    if all_not_none_and_numeric(b, h):
        print(_geometry.surface_of_triangle(float(b), float(h)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@geometry.command("surface_of_trapezoid", help="Return the surface of a"
                                               " trapezoid.")
@click.option("-a", help="Calculate the surface of a trapezoid by base 1")
@click.option("-b", help="Calculate the surface of a trapezoid by base 2")
@click.option("-h", help="Calculate the surface of a trapezoid by its height")
def surface_of_trapezoid(a: str, b: str, h: str) -> None:
    if all_not_none_and_numeric(a, b, h):
        print(_geometry.surface_of_trapezoid(float(a), float(b), float(h)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")


@geometry.command("hypotenuse", help="The square of the hypotenuse is equal to"
                                     " the sum of the areas of the squares on"
                                     " the other two sides. Return the"
                                     " hypotenuse of a triangle.")
@click.option("-a", help="Calculate the hypotenuse by the size of the base")
@click.option("-b", help="Calculate the hypotenuse by the size of the"
                         " altitude")
def hypotenuse(a: str, b: str) -> None:
    if all_not_none_and_numeric(a, b):
        print(_geometry.hypotenuse(float(a), float(b)))
    else:
        print("You did not enter parameter(s) or the parameter(s) is not 'int'"
              " or 'float'")
