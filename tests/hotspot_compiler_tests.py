import unittest
from hotspot_compiler import HotSpotCompiler


class HotSpotCompilerTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_given_number_of_commit_and_lines_count_then_ordered_by_highest_number_of_commits(
        self
    ):
        commits = {"File1": 5, "File2": 15, "File3": 10}
        loc = {"File1": 123, "File2": 321, "File3": 1000}
        ans = HotSpotCompiler.merge_raw_data(commits, loc)
        self.assertEqual("File2", ans[0][0])
        self.assertEqual("File3", ans[1][0])
        self.assertEqual("File1", ans[2][0])

    def test_given_number_of_commits_equal_then_ordered_by_highest_number_of_lines(
        self
    ):
        commits = {"File1": 5, "File2": 5, "File3": 5}
        loc = {"File1": 123, "File2": 321, "File3": 1000}
        ans = HotSpotCompiler.merge_raw_data(commits, loc)
        self.assertEqual("File3", ans[0][0])
        self.assertEqual("File2", ans[1][0])
        self.assertEqual("File1", ans[2][0])
