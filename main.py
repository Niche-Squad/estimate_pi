import numpy as np

class Point():
    """
    A point in a 2D (xy) space
    properties:
        x: integer, x-coordinate
        y: integer, y-coordinate
    """

    def __init__(self, xy=None):
        """
        Constructor
        If xy is not provided, randomly generate xy coordiantes.
        xy can be assigned by a tuple (e.g., (2, 3))
        """
        # properties
        self.x = None
        self.y = None

        # assign values to x and y
        if xy is None:
            pass
        else:
            pass

    def __repr__(self):
        """
        Allow the xy-coordinates to be printed when the point is called
        """
        return "Point: %.2f, %.2f" % (self.x, self.y)

    def distance(self, point):
        """
        input: a Point() object
        output: Euclidean distance between self point and the input point
        """
        pass

def estimate_pi(n_points):
    """
    input: number of points to be generated
    output: estimated pi through the simulation
    """
    pass


# estimate pi for 100 iterations
outs = np.zeros((1000, 100))
for i in range(100):
    pass
