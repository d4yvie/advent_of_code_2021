from file_util import read_lines
from scipy.signal import convolve2d
import numpy as np


if __name__ == '__main__':
    lines = read_lines()
    enhancement = np.array(list(lines[0])) == "#"
    grid = np.array(list(map(list, lines[2:]))) == "#"
    kernel = 2 ** np.arange(9).reshape((3, 3))
    for i in range(50):
        # enhance that image! https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html
        grid = enhancement[convolve2d(grid, kernel, fillvalue=i % 2)]
        if i in (1, 49):
            print(grid.sum())
