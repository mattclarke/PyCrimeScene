import unittest
from hotspot_compiler import merge_raw_data, remove_files_with_no_code


class HotSpotCompilerTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_given_number_of_commit_and_lines_count_then_ordered_by_highest_number_of_commits(
        self
    ):
        commits = {"File1": 5, "File2": 15, "File3": 10}
        loc = {"File1": 123, "File2": 321, "File3": 1000}
        ans = merge_raw_data(commits, loc)
        self.assertEqual("File2", ans[0][0])
        self.assertEqual("File3", ans[1][0])
        self.assertEqual("File1", ans[2][0])

    def test_given_number_of_commits_equal_then_ordered_by_highest_number_of_lines(
        self
    ):
        commits = {"File1": 5, "File2": 5, "File3": 5}
        loc = {"File1": 123, "File2": 321, "File3": 1000}
        ans = merge_raw_data(commits, loc)
        self.assertEqual("File3", ans[0][0])
        self.assertEqual("File2", ans[1][0])
        self.assertEqual("File1", ans[2][0])

    def test_files_with_no_code_are_removed(self):
        commits = {"File1": 5, "File2": 5, "File3": 5}
        loc = {"File1": 123, "File2": 0, "File3": 1000}
        remove_files_with_no_code(commits, loc)
        self.assertEqual(2, len(commits))
        self.assertFalse("File2" in commits)

    def test_files_that_no_longer_exist_are_removed(self):
        commits = {"File1": 5, "File2": 5, "File3": 5}
        loc = {"File1": 123, "File3": 1000}
        remove_files_with_no_code(commits, loc)
        self.assertEqual(2, len(commits))
        self.assertFalse("File2" in commits)
