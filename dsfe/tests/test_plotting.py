""" Test plotting routines
"""

import numpy as np

from dsfe.plotting import count_bar


def test_plot_square2():
    arr = [0, 1, 1, 1, 2, 3, 4, 3, 4, 5]
    bar0 = count_bar(arr)
    out_counts = np.bincount(arr)
    assert np.all(bar0.datavalues == out_counts)
    assert np.all(out_counts == [p.get_height() for p in bar0.patches])
