import numpy as np


class LorenzAttractor:
    """
    Lorenz Attractor System
    a, r, b = constants

    dx/dt = a(y-x)
    dy/dt = rx - xz - y
    dz/dt = xy - bz
    """

    def __init__(self, a: float, r: float, b: float, timestep: float = 0.01) -> None:
        self.a: float = a
        self.r: float = r
        self.b: float = b
        self.timestep: float = timestep
        self.position = np.array((0., 1., 1.05))

    def update(self) -> np.array:
        """
        Update the system position.
        :return: new system position.
        """
        x, y, z = self.position.copy()

        dt: float = self.timestep
        dx: float = (self.a * (y - x)) * dt
        dy: float = ((self.r * x) - (x * z) - y) * dt
        dz: float = ((x * y) - (self.b * z)) * dt

        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz

        return self.position
