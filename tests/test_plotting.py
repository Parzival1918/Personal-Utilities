# Test the plotting module

from pu_pjr.plotting import xy
from pu_pjr.plotting import stats
from pu_pjr.plotting import utils

def test_plot_xy():
    xy.plot_xy('tests/test_files/energy.dat', testing=True)
    return

def test_load_data():
    df = utils.load_data('tests/test_files/energy.dat')
    assert df.shape == (1000, 3)

def test_violin_plot():
    stats.violin_plot('tests/test_files/energy.dat', testing=False)
    # stats.violin_plot('tests/test_files/energy.dat', testing=False, col=2)
    return