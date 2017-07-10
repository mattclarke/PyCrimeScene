import unittest


class DataMiningGitLogTests(unittest.TestCase):
    def correctly_extracts_number_of_commits_from_git_log(self):
        """
        Used with output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat
        """
        data_miner = DataMiner()
        num = data_miner.extract_number_commits()
        self.assertEqual(3, num)
