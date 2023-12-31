# Test the plotting module
import pytest
import matplotlib.pyplot as plt

from pu_pjr.plotting import xy
from pu_pjr.plotting import stats
from pu_pjr.plotting import utils
from pu_pjr.plotting import multi_file

def test_plot_xy():
    xy.plot_xy('tests/test_files/energy.dat', testing=True)
    xy.plot_xy('tests/test_files/energy.dat', plot_all=True, testing=True)
    xy.plot_xy('tests/test_files/energy.dat', line_type='o-', testing=True)
    xy.plot_xy('tests/test_files/energy.dat', normalise=utils.Normalisation.NONE, 
               testing=True)
    xy.plot_xy('tests/test_files/energy.dat', normalise=utils.Normalisation.STANDARD, 
               testing=True)
    xy.plot_xy('tests/test_files/energy.dat', normalise=utils.Normalisation.ZERO_ONE, 
               testing=True)
    xy.plot_xy('tests/test_files/energy.dat', 
               mathematical_expression='+|20', 
               mathematical_expression_location=utils.MathLocs.Y,
               testing=True)
    
    # Delete all figures
    plt.close('all')
    return

def test_load_data():
    df = utils.load_data('tests/test_files/energy.dat')
    assert df.shape == (1000, 3)

def test_violin_plot():
    stats.violin_plot('tests/test_files/energy.dat', testing=True)
    stats.violin_plot('tests/test_files/energy.dat', testing=True, col=2)

    # Delete all figures
    plt.close('all')
    return

def test_parse_math_expression():
    d = utils.parse_math_expression('+|2, -|3')
    assert d[0] == ('+', 2)
    assert d[1] == ('-', 3)
    d = utils.parse_math_expression('+|2, -|MIN')
    assert d[0] == ('+', 2)
    assert d[1] == ('-', "MIN")
    with pytest.raises(ValueError):
        utils.parse_math_expression('&|2, *|3')

def test_load_many_data():
    dfs, _ = utils.load_many_data('energy_*.dat', dir='tests/test_files/')
    assert dfs[0].shape == (1000, 4)
    assert len(dfs) == 3

def test_plot_multifile():
    multi_file.plot_multifile_xy('energy_*.dat', testing=True, dir="tests/test_files/")
    multi_file.plot_multifile_xy('energy_*.dat', testing=True, dir="tests/test_files/", 
                              xcol=1, ycol=2)
    
    # Delete all figures
    plt.close('all')
    return

def test_plot_multifile_bar():
    multi_file.plot_multifile_bar('energy_*.dat', testing=True, 
                                  dir="tests/test_files/")
    multi_file.plot_multifile_bar('energy_*.dat', testing=True, col=2,
                                  dir="tests/test_files/")
    multi_file.plot_multifile_bar('energy_*.dat', testing=True, col=3,
                                  dir="tests/test_files/", special_val="MEAN")
    multi_file.plot_multifile_bar('energy_*.dat', testing=True, col=1,
                                  dir="tests/test_files/", special_val="MEAN")
    multi_file.plot_multifile_bar('energy_*.dat', testing=True, dir="tests/test_files/",
                                  col=2, special_val="MIN")
    
    # Delete all figures
    plt.close('all')
    return