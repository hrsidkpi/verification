import matplotlib.pyplot as plt
from abstract_domains.box import Box
from abstract_domains.interval import Interval
import numpy as np


def main():
    box = Box([Interval(0,2), Interval(1,3)])

    points = np.array(box.get_vertices())
    x = points[:,0]
    y = points[:,1]
    plt.scatter(x, y, c='blue')

    points = np.array(box.get_affine_transform(np.array([[2, -1], [0, 1]]), np.array([0,0])).get_vertices())
    x = points[:,0]
    y = points[:,1]
    plt.scatter(x, y, c='red')

    plt.show()


if __name__ == "__main__":
    main()