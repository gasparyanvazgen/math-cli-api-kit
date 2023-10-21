"""This module defines the command-line interface (CLI) for the math operations'
calculator. It allows users to perform algebraic and geometric calculations through the CLI.
"""

import click

from .math_cli import algebra, geometry


@click.group()
def cli():
    pass


cli.add_command(algebra)
cli.add_command(geometry)

if __name__ == '__main__':
    cli()
