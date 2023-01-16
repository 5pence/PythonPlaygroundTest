from TriadFinder import TriadFinder


def test_triad_finder_no_number():
    inp = TriadFinder([1200, 1333, 999, 333])
    output = inp.find_triad_product()
    assert output is None


def test_triad_finder_has_number():
    inp = TriadFinder([1000, 1333, 120, 900])
    output = inp.find_triad_product()
    answer = 1000 * 120 * 900
    assert output == answer
