from file_util import read_lines_as_int
import numpy as np
from skimage.segmentation import watershed
from skimage.measure import regionprops
from skimage.feature import peak_local_max


def task1(numbers: list[list[int]]):
    padded = np.pad(numbers, ((1, 1), (1, 1)), 'constant', constant_values=9)
    coords = peak_local_max(-padded)
    return np.sum(padded[tuple(coords.T)] + 1)


def task2(numbers: list[list[int]]):
    watershedded = watershed(numbers, mask=numbers != 9)
    regional_props = regionprops(watershedded)
    return np.prod(sorted([prop.area for prop in regional_props])[-3:])


if __name__ == "__main__":
    parsed = np.array(read_lines_as_int())
    print(task1(parsed))
    print(task2(parsed))
