"""
Geometry functions
Layher Scaffolding Generator
"""

import math


class Point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z


def scaffold_grid(bays_x, bays_y, bay_length, bay_width):
    """
    Create grid points for scaffold standards.
    """

    points = []

    for x in range(bays_x + 1):
        for y in range(bays_y + 1):
            points.append(
                Point3D(
                    x * bay_length,
                    y * bay_width,
                    0.0
                )
            )

    return points# Geometry functions for the Scaffolding Plug-in
