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

    def add_location_constraint(self, constraint_str, target_str):
        try:
            constraint_parts = constraint_str.split(" ")
            positions = constraint_parts[0].split("-")
            char = constraint_parts[1]
            count = 0
            for position in positions:
                position = int(position)
                if position > len(target_str) or position < 1:
                    raise ValueError("position is not valid")
                if target_str[int(position) - 1] == char:
                    count += 1
            if count == 1:
                self.valid_count += 1
        except ValueError as e:
            print(f"Error: {e}")
            return

    def get_valid_count(self):
        return self.valid_count
