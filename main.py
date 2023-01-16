from InputFileReader import InputFileReader
from PairFinder import PairFinder
from TriadFinder import TriadFinder
from ConstraintChecker import ConstraintChecker

if __name__ == '__main__':
    # get the number array
    number_reader = InputFileReader()
    number_array = number_reader.read_numbers()

    # Problem 1a
    pair_finder = PairFinder(number_array)
    product_of_pair = pair_finder.find_pair_product()
    print('========================')
    print('Finding Product of Pair')
    print(f'Answer: {product_of_pair}')
    print('========================\n')

    # Problem 1b
    triad_finder = TriadFinder(number_array)
    product_of_triad = triad_finder.find_triad_product()
    print('========================')
    print('Finding Product of Triad')
    print(f'Answer: {product_of_triad}')
    print('========================\n')

    # Get the string array
    string_reader = InputFileReader('assets/txt/input2.txt')
    string_array = string_reader.read_n_constraint()

    # Problem 2a
    validator1 = ConstraintChecker()
    for string in string_array:
        elements = string.split(':')
        validator1.add_constraint(elements[0], elements[1])

    print('========================')
    print('Number of Valid Strings 2a')
    print(f'Answer: {validator1.get_valid_count()}')
    print('========================\n')

    # Problem 2b
    validator2 = ConstraintChecker()
    for string in string_array:
        elements = string.split(':')
        validator2.add_location_constraint(elements[0], elements[1])

    print('========================')
    print('Number of Valid Strings 2b')
    print(f'Answer: {validator2.get_valid_count()}')
    print('========================\n')