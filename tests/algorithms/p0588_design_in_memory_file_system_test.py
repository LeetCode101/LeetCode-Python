import unittest
from leetcode.algorithms.p0588_design_in_memory_file_system import FileSystem


class TestDesignInMemoryFileSystem(unittest.TestCase):
    def test_design_in_memory_file_system(self):
        file_system = FileSystem()

        self.assertListEqual([], file_system.ls('/'))

        file_system.mkdir('/a/b/c')
        file_system.addContentToFile('/a/b/c/d', 'hello')

        self.assertListEqual(['a'], file_system.ls('/'))
        self.assertEqual('hello', file_system.readContentFromFile('/a/b/c/d'))
        self.assertListEqual([], file_system.ls('/m/q'))
        self.assertListEqual(['d'], file_system.ls('/a/b/c/d'))
