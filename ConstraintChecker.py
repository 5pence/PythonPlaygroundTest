class ConstraintChecker:
    def __init__(self):
        self.valid_count = 0

    def add_constraint(self, constraint_str, target_str):
        constraint_parts = constraint_str.split(" ")
        low, high = map(int, constraint_parts[0].split("-"))
        char = constraint_parts[1]
        count = target_str.count(char)
        if low <= count <= high:
            self.valid_count += 1

    def get_valid_count(self):
        return self.valid_count
