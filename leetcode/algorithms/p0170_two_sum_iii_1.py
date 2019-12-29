class TwoSum:
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        mapping = {}

        for index, v in enumerate(self.nums):
            if value - v in mapping:
                return True
            else:
                mapping[v] = index

        return False
