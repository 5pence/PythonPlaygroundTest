from NumberReader import NumberReader
from PairFinder import PairFinder
from TriadFinder import TriadFinder

if __name__ == '__main__':
    # get the number array
    number_reader = NumberReader()
    number_array = number_reader.read_numbers()

    # Now trigger the PairFinder
    pair_finder = PairFinder(number_array)
    product_of_pair = pair_finder.find_pair_product()
    print('========================')
    print('Finding Product of Pair')
    print(f'Answer: {product_of_pair}')
    print('========================\n')

    # Now the TriadFinder
    triad_finder = TriadFinder(number_array)
    product_of_triad = triad_finder.find_triad_product()
    print('========================')
    print('Finding Product of Triad')
    print(f'Answer: {product_of_triad}')
    print('========================\n')
