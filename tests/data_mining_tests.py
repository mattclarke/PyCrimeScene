import unittest
from data_miner import DataMiner


class DataMiningGitLogTests(unittest.TestCase):
    def correctly_extracts_number_of_commits_from_git_log(self):
        """
        Used with output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat
        """
        raw_data = """
        [74f6bbf] mjc23 2017-07-10 Added first unit test
        12      0       tests/data_mining_tests.py

        [1dbf879] mjclarke01 2017-07-10 Create README.md
        2       0       README.md

        [9d18261] mjclarke01 2017-07-10 Initial commit
        101     0       .gitignore
        29      0       LICENSE
        """

        data_miner = DataMiner()
        num = data_miner.extract_number_commits(raw_data)
        self.assertEqual(3, num)
