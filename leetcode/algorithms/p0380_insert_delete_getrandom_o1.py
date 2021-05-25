import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.position = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        """
        if val in self.position:
            return False

        self.values.append(val)
        self.position[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val not in self.position:
            return False

        i, last = self.position[val], self.values[-1]
        self.values[i], self.position[last] = last, i
        self.values.pop()
        self.position.pop(val)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.values[random.randint(0, len(self.values) - 1)]
