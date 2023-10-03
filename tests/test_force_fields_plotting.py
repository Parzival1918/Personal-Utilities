from pu_pjr.force_fields_plotting import utils

import pytest

def test_create_range():
    assert [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 
            0.9999999999999999, 1.0999999999999999, 1.2, 1.3, 1.4, 1.5, 
            1.5999999999999999, 1.7, 1.8, 1.9, 2.0, 2.0999999999999996, 
            2.1999999999999997, 2.3, 2.4, 2.5, 2.6, 2.6999999999999997, 
            2.8, 2.9, 3.0] == \
            utils.create_range()
    assert [0, 1.0] == utils.create_range(0.0, 1.0, 2)
    with pytest.raises(ValueError):
        utils.create_range(1, 0)