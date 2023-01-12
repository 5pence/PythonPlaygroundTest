class NumberReader:
    """
    Reads given filename (default to input1.txt) and builds int array
    If a line cannot be converted to int throws ValueError
    """
    def __init__(self, filepath='input1.txt'):
        self.filepath = filepath
        self.numbers = []

    def read_numbers(self):
        with open(self.filepath) as f:
            lines = f.readlines()
            for line in lines:
                try:
                    number = int(line)
                    self.numbers.append(number)
                except ValueError:
                    print("Invalid whole number in file: " + line)
            return self.numbers

