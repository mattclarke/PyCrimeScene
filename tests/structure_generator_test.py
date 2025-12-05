import unittest
from structure_generator import generate_structure


class GenerateStructureTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_given_one_file_get_simple_structure(self):
        files = [("test/src/file.java", 1.0, 10)]
        top_node = generate_structure(files)

        self.assertEqual("root", top_node["name"])
        child = top_node["children"][0]
        self.assertEqual("test", child["name"])
        child = child["children"][0]
        self.assertEqual("src", child["name"])
        child = child["children"][0]
        self.assertEqual("file.java", child["name"])

    def test_given_two_file_in_different_directories(self):
        files = [("test/src/file.java", 1.0, 10), ("doc/rst/readme.txt", 1.0, 10)]
        top_node = generate_structure(files)

        self.assertEqual("root", top_node["name"])

        # First file
        child = top_node["children"][0]
        self.assertEqual("test", child["name"])
        child = child["children"][0]
        self.assertEqual("src", child["name"])
        child = child["children"][0]
        self.assertEqual("file.java", child["name"])

        # Second file
        child = top_node["children"][1]
        self.assertEqual("doc", child["name"])
        child = child["children"][0]
        self.assertEqual("rst", child["name"])
        child = child["children"][0]
        self.assertEqual("readme.txt", child["name"])

    def test_given_two_file_in_same_directory(self):
        files = [("test/src/file1.java", 1.0, 10), ("test/src/file2.java", 1.0, 10)]
        top_node = generate_structure(files)

        self.assertEqual("root", top_node["name"])

        child = top_node["children"][0]
        self.assertEqual("test", child["name"])
        child = child["children"][0]
        self.assertEqual("src", child["name"])
        child1 = child["children"][0]
        child2 = child["children"][1]
        # First file
        self.assertEqual("file1.java", child1["name"])

        # Second file
        self.assertEqual("file2.java", child2["name"])

    def test_given_two_file_in_same_directory_structure(self):
        files = [("test/src/file1.java", 1.0, 10), ("test/file2.java", 1.0, 10)]
        top_node = generate_structure(files)

        self.assertEqual("root", top_node["name"])

        child = top_node["children"][0]
        self.assertEqual("test", child["name"])
        child = child["children"][0]
        self.assertEqual("src", child["name"])
        child = child["children"][0]
        # First file
        self.assertEqual("file1.java", child["name"])

        # Second file
        child = top_node["children"][0]
        self.assertEqual("test", child["name"])
        child = child["children"][1]
        self.assertEqual("file2.java", child["name"])
