"""
Module containing every available simulation type.
"""

from enum import Enum, auto


class Simulations(Enum):
    """Represent every available simulation."""
    LORENZ_ATTRACTOR = auto()
    RANDOM_WALK = auto()
