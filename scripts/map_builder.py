import numpy as np
import matplotlib.pyplot as plt

class MapBuilder:

    def __init__(self):
        self.points = []

    def update(self, pose):
        self.points.append(pose)

    def generate_map(self):
        pts = np.array(self.points)

        plt.scatter(pts[:,0], pts[:,1], s=2)
        plt.title("Corrected Map")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.show()