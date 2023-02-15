"""
Module that contain the sim to simulate the lorenza attractor.
Provided by Mova801 (http://www.github.com/Mova801)
"""
import numpy as np

from src.sim import lorenz
from src.sim import plot
from src.sim import simulations


def lorenz_attractor(steps: int) -> bool:
    """
    Solve and plot the lorenz attractor.
    :param steps: steps in time to solve.
    :return: True if no error occurred, False otherwise.
    """
    attractor = lorenz.LorenzAttractor(a=10.0, r=28.0, b=(8.0 / 3.0))
    # array of 'steps + 1' triple values
    xyzs = np.empty((steps, 3))
    # produce xyz values
    for i in range(steps):
        xyzs[i] = attractor.update()
    # plot xyz values
    plot.plot3d(xyzs, "Lorenz Attractor", axis=False)
    return True


def start_simulation(simulation_type: simulations.Simulations) -> bool:
    """
    Start the selected simulation.
    :param simulation_type: simulation to start.
    :return: True if a valid simulation is passed, False otherwise.
    """
    match simulation_type:
        case simulations.Simulations.LORENZ_ATTRACTOR:
            lorenz_attractor(10000)
            return True
        case _:
            return False
