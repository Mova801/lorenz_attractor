"""
Module that run the lorenz attractor simulation.
Provided by Mova801 (http://www.github.com/Mova801)
"""
from src.sim.simulator import start_simulation
from src.sim.simulations import Simulations


def main() -> int:
    start_simulation(Simulations.LORENZ_ATTRACTOR)
    return 0


if __name__ == "__main__":
    main()
