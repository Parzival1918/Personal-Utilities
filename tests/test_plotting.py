# Test the plotting module

from pu_pjr.plotting import xy
from pu_pjr.plotting import utils

def test_plot_xy():
    xy.plot_xy('tests/test_files/energy.dat', testing=True)
    return

def test_load_data():
    df = utils.load_data('tests/test_files/energy.dat')
    assert df.shape == (1000, 3)