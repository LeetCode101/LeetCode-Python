import random


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.position = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection.
        Returns true if the collection did not already
        contain the specified element.
        """
        self.values.append(val)

        if val in self.position:
            self.position[val].add(len(self.values) - 1)
        else:
            self.position[val] = {len(self.values) - 1}

        return len(self.position[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection.
        Returns true if the collection contained the specified element.
        """
        if val not in self.position or not self.position[val]:
            return False

        i, last = self.position[val].pop(), self.values[-1]
        self.values[i] = last

        if self.position[last]:
            self.position[last].add(i)
            self.position[last].remove(len(self.values) - 1)

        self.values.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.values[random.randint(0, len(self.values) - 1)]
