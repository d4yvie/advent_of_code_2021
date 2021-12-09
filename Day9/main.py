from file_util import read_lines_as_int
import numpy as np
from skimage.segmentation import watershed
from skimage.measure import regionprops
from skimage.feature import peak_local_max


def task1(numbers: list[list[int]]) -> int:
    padded = np.pad(numbers, ((1, 1), (1, 1)), 'constant', constant_values=9)
    # https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_peak_local_max.html
    local_maxima = peak_local_max(-padded)
    return np.sum(padded[tuple(local_maxima.T)] + 1)


def task2(numbers: list[list[int]]) -> int:
    # https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_watershed.html
    after_watershed_segmentation = watershed(numbers, mask=numbers != 9)
    # https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_regionprops.html
    measured_properties = regionprops(after_watershed_segmentation)
    return np.prod(sorted([prop.area for prop in measured_properties])[-3:])


if __name__ == "__main__":
    parsed = np.array(read_lines_as_int())
    print(f"Sum of risk level of all low points: {task1(parsed)}")
    print(f"Multiplied sizes of three largest basins: {task2(parsed)}")
