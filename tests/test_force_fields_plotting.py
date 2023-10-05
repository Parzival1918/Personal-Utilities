from pu_pjr.force_fields_plotting import utils

import pytest

def test_field_descriptions():
    descriptions, max_length = utils.field_descriptions()
    assert max_length == 9
    assert "lj_cut" in descriptions
    assert "buck" in descriptions
    assert "buck_coul" in descriptions    

def test_create_range():
    assert [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 
            0.9999999999999999, 1.0999999999999999, 1.2, 1.3, 1.4, 1.5, 
            1.5999999999999999, 1.7, 1.8, 1.9, 2.0, 2.0999999999999996, 
            2.1999999999999997, 2.3, 2.4, 2.5, 2.6, 2.6999999999999997, 
            2.8, 2.9, 3.0] == \
            utils.create_range()
    assert [0, 1.0] == utils.create_range(0.0, 1.0, 2)
    assert [0.0, 0.5, 1.0] == utils.create_range(0.0, 1.0, 3)
    with pytest.raises(ValueError):
        utils.create_range(1, 0)

    with pytest.raises(ValueError):
        utils.create_range(1, 1)

def test_remove_extras_from_field_name():
    assert "lj/cut" == utils.remove_extras_from_field_name("lj_cut")
    assert "buck" == utils.remove_extras_from_field_name("buck")
    assert "buck/coul" == utils.remove_extras_from_field_name("buck_coul")

def test_remove_extras_for_class():
    assert "lj_cut" == utils.remove_extras_for_class("lj_cut")
    assert "buck" == utils.remove_extras_for_class("buck")
    assert "buck_coul" == utils.remove_extras_for_class("buck_coul-4")
    assert "lj_cut" == utils.remove_extras_for_class("lj_cut")
    assert "buck" == utils.remove_extras_for_class("buck-6")
    assert "buck_coul" == utils.remove_extras_for_class("buck_coul")

def test_parse_keyargpairs():
    assert {"lj_cut": {"epsilon": 1.0, "sigma": 2.0, "cut": 3.0}} == \
            utils.parse_keyargpairs(["lj_cut", "epsilon=1.0", "sigma=2.0", "cut=3.0"])
    assert {"buck": {"A": 1.0, "rho": 2.0, "C": 3.0}} == \
            utils.parse_keyargpairs(["buck", "A=1.0", "rho=2.0", "C=3.0"])
    assert {"buck_coul": {"A": 1.0, "rho": 2.0, "C": 3.0, "q1": 4.0, "q2": 5.0}} == \
            utils.parse_keyargpairs(["buck_coul", "A=1.0", "rho=2.0", "C=3.0", "q1=4.0",
                                     "q2=5.0"])