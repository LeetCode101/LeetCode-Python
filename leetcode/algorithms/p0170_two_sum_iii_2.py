class TwoSum:
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for v in self.nums:
            diff = value - v

            if diff in self.nums and (diff != v or self.nums[diff] > 1):
                return True

        return False
