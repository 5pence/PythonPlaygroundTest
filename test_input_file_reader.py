from InputFileReader import InputFileReader


def test_read_numbers():
    inp = InputFileReader()
    output = inp.read_numbers()
    assert len(output) == 200
    assert type(output) == list


def test_read_n_constraint():
    inp = InputFileReader('assets/txt/input2.txt')
    output = inp.read_n_constraint()
    assert len(output) == 1000
    assert type(output) == list



