class TriadFinder:
    """
    This approach has a time complexity of O(n^2) as it is iterating through
    the array once and performing constant time operations (comparing numbers and
    changing pointers) for each element.  Sorting the array first will add
    O(n*log(n)) in the time complexity.
    There is a quicker way using a trie though it's quite complicated and memory
    hungry and not necessarily quicker as it depends on number of elements and the
    number of digits in each element. That would have a O(elements * digits) -
    so would be five times quicker in this test instance as  200 elements of 4
    digits apiece (800 vs 40,000)
    So given time I would a trie class and after reading the input txt determine
    which algorthim would be appropriate (assuming I had plenty of memory processing
    power).
    """
    def __init__(self, number_array):
        self.number_array = number_array

    def find_triad_product(self):
        self.number_array.sort()
        target = 2020
        for i in range(len(self.number_array) - 2):
            left = i + 1
            right = len(self.number_array) - 1
            while left < right:
                current_sum= self.number_array[i] + self.number_array[left] + self.number_array[right]
                if current_sum == target:
                    return self.number_array[i] * self.number_array[left] * self.number_array[right]
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
