from PairFinder import PairFinder


def test_find_pair_product_no_pair():
    inp = PairFinder([1000, 1200])
    output = inp.find_pair_product()
    assert output is None


def test_find_pair_product_pair():
    inp = PairFinder([1000, 1020])
    output = inp.find_pair_product()
    assert output == 1020000
