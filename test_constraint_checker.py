from ConstraintChecker import ConstraintChecker


def test_add_location_constraint():
    inp = ConstraintChecker()
    inp.add_location_constraint("2-5 t", "qwertyuiuytre")
    output = inp.get_valid_count()
    assert output == 1


def test_add_location_constraint_zero():
    inp = ConstraintChecker()
    inp.add_location_constraint("2-5 t", "qwerqyuiuytre")
    output = inp.get_valid_count()
    assert output == 0


def test_add_constraint():
    inp = ConstraintChecker()
    inp.add_location_constraint("2-5 t", "qwertyuiuytre")
    inp.add_location_constraint("2-5 t", "qwertyuiuytre")
    inp.add_location_constraint("2-5 t", "qweryuiuyre")
    output = inp.get_valid_count()
    assert output == 2