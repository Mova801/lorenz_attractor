import matplotlib.pyplot as plt
import numpy as np


def plot3d(xyzs: np.array, plot_title: str = "", axis: bool = True) -> None:
    """
    Plot the passed 3D coordinates array.
    :param xyzs: coordinates array (x,y,z).
    :param plot_title: displayed plot title.
    :param axis: axis are displayed if True, not displayed is False; default: True.
    :return: None.
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d', facecolor=(.35, .35, .35))
    ax.axis(axis)
    ax.plot(*xyzs.T, lw=0.4)
    ax.set_title(plot_title, weight='bold', style='italic')
    plt.show()


def plot3d_animated(xyzs: np.array, plot_title: str = "", deltatime: float = 0.01) -> None:
    NotImplementedError()
