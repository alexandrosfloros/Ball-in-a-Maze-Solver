from simulation import *
from graphics import *

# initialising path nodes

nodes = [
    [16.0, 21.5],
    [5.50, 21.5],
    [5.50, 16.0],
    [7.00, 16.0],
    [7.00, 10.5],
    [1.00, 10.5],
    [1.00, 5.00],
    [8.00, 5.00],
    [8.00, 8.50],
    [11.5, 8.50],
    [11.5, 4.00],
    [13.5, 4.00],
    [13.5, 10.5],
    [11.0, 10.5],
    [11.0, 13.0],
    [9.50, 13.0],
    [9.50, 19.5],
    [12.5, 19.5],
    [12.5, 17.5],
    [19.0, 17.5],
    [19.0, 20.0],
    [26.5, 20.0],
    [26.5, 16.0],
    [21.5, 16.0],
    [21.5, 14.0],
    [19.0, 14.0],
    [19.0, 12.5],
    [17.5, 12.5],
    [17.5, 9.50],
    [20.0, 9.50],
    [20.0, 4.00],
    [21.5, 4.00],
    [21.5, 1.00],
    [10.5, 1.00],
]

# initialising holes

holes = [
    [3.00, 18.3],
    [8.20, 15.7],
    [5.50, 12.7],
    [5.50, 8.60],
    [3.10, 6.30],
    [5.60, 3.40],
    [10.3, 6.80],
    [17.2, 6.80],
    [14.9, 11.0],
    [12.5, 14.2],
    [8.20, 18.4],
    [15.0, 19.0],
    [21.6, 17.5],
    [17.2, 14.2],
    [23.9, 14.2],
    [23.9, 5.60],
]

if __name__ == "__main__":
    # initialising ball position

    x, y = nodes[0]
    ball = Ball([x, y])

    # initialising graphics

    model = Graphics(ball, nodes, holes)

    # initialising simulation

    animate_model(model)
