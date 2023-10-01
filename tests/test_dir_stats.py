from pu_pjr.dir_stats import utils

def test_get_dir_size():
    size = utils.get_dir_size('tests/test_files/')
    assert size == 123110
    assert utils.transform_file_size(size) == 'kB'

def test_get_dir_files():
    files,_ = utils.get_dir_files('tests/test_files/')
    assert len(files) == 4
    assert files[0] == 'energy_1000_50.dat'

    files, dirs = utils.get_dir_files('tests', True)
    assert len(files) == 4
    assert len(dirs) == 2

def test_get_file_types():
    files,_ = utils.get_dir_files('tests/test_files/')
    file_types = utils.get_file_types(files)
    assert len(file_types) == 2
    assert file_types['dat'] == 4

    files,_ = utils.get_dir_files('tests/')
    file_types = utils.get_file_types(files)
    assert len(file_types) == 2
    assert file_types['py'] == 3

    files,_ = utils.get_dir_files('tests/')
    file_types = utils.get_file_types(files, ignore_hidden=False)
    assert len(file_types) == 2
    assert file_types['py'] == 3
    assert file_types['none'] == 1