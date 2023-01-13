import re


class InputFileReader:
    """
    Reads given filename (default to input1.txt) and builds int array
    If a line cannot be converted to int throws ValueError
    """
    def __init__(self, filepath='assets/txt/input1.txt'):
        self.filepath = filepath
        self.result = []

    def read_numbers(self):
        with open(self.filepath) as f:
            lines = f.readlines()
            for line in lines:
                try:
                    number = int(line)
                    self.result.append(number)
                except ValueError:
                    print("Invalid whole number in file: " + line)
            return self.result

    def read_n_constraint(self):
        # Regular expression pattern to match the specified line format n-n c: str
        pattern = re.compile(r"^\d+-\d+\s[a-zA-Z]:\s.+$")

        valid_lines = []
        with open(self.filepath, "r") as file:
            for line in file:
                if pattern.match(line):
                    line = line.rstrip('\n')
                    valid_lines.append(line)
                else:
                    print(f"Invalid line format: {line}")

        return valid_lines
