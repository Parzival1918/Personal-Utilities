# Test the changing_dirs module

from pu_pjr.changing_dirs import utils
from pu_pjr.changing_dirs import quickcd

def test_get_dir():
    assert utils.get_cwd() == '/Users/parzival1918/Documents/GitHub/Personal-Utilities'

def test_change_dir():
    utils.change_cwd('/Users/parzival1918')
    assert utils.get_cwd() == '/Users/parzival1918'

    # Change back to the original directory
    utils.change_cwd('/Users/parzival1918/Documents/GitHub/Personal-Utilities')
    assert utils.get_cwd() == '/Users/parzival1918/Documents/GitHub/Personal-Utilities'

def test_get_home_dir():
    assert utils.get_home_dir() == '/Users/parzival1918'

# def test_check_saves_dir():
#     assert utils.check_saves_dir() is True

def test_create_saves_dir():
    if utils.check_saves_dir():
        assert utils.check_saves_dir() is True
    else:
        utils.create_saves_dir()
        assert utils.check_saves_dir() is True

def test_create_saves_file():
    quickcd.create_saves_file()
    assert utils.check_saves_dir() is True

def test_add_entry():
    quickcd.add_entry('cwd-1', utils.get_cwd())
    entries = quickcd.list_entries()
    assert entries['cwd-1'] == utils.get_cwd()

def test_remove_entry():
    quickcd.remove_entry('cwd-1')
    entries = quickcd.list_entries()
    assert 'cwd-1' not in entries.keys()

def test_change_to_entry():
    quickcd.add_entry('cwd-1', '/Users/parzival1918')
    quickcd.change_to_entry('cwd-1')
    assert utils.get_cwd() == quickcd.list_entries()['cwd-1']

    # Change back to the original directory
    utils.change_cwd('/Users/parzival1918/Documents/GitHub/Personal-Utilities')
    assert utils.get_cwd() == '/Users/parzival1918/Documents/GitHub/Personal-Utilities'

    quickcd.remove_entry('cwd-1')
    entries = quickcd.list_entries()
    assert 'cwd-1' not in entries.keys()
