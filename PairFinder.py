class PairFinder:
    """
    This approach has a time complexity of O(n) because I am iterating through
    the array once and performing constant time operations (inserting into the
    hash set and looking up elements in the hash set) for each element.
    """
    def __init__(self, number_array):
        self.number_array = number_array
        self.number_hash_set = {}

    def find_pair_product(self, chosen_summed_amount=2020):
        for index_value, number in enumerate(self.number_array):
            remainder = chosen_summed_amount - number
            if remainder in self.number_hash_set:
                return number * remainder
            self.number_hash_set[number] = index_value
