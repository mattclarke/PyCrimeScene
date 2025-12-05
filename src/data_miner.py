import re


class DataMiner:
    @staticmethod
    def extract_number_commits(raw_data):
        """
        Returns the number of commits contained in the data.

        Used with prettified output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat

        :param raw_data: the output of the git log
        :return: number of commits in the output
        """
        num_commits = 0
        lines = raw_data.strip().split("\n")
        for line in lines:
            if line.strip().startswith("["):
                num_commits += 1
        return num_commits

    @staticmethod
    def extract_number_authors(raw_data):
        """
        Returns the number of authors who have committed commits.

        Used with prettified output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat

        :param raw_data: the output of the git log
        :return: number of committing authors
        """
        authors = set()
        lines = raw_data.strip().split("\n")
        for line in lines:
            # Something like:
            # [cef94a2] mjc23 2017-07-10 Added DataMiner class
            # As names can contain spaces we need to match up to the date
            m = re.match(r"\s*\[\w*\]\s(\S[\S\s]*\S)\s\d\d\d\d-\d\d-\d\d.*", line)
            if m is not None:
                authors.add(m.groups()[0])
        return len(authors)

    @staticmethod
    def extract_number_entities_changed(raw_data):
        """
        Returns the number of times files have had changes committed.

        Used with prettified output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat

        :param raw_data: the output of the git log
        :return: number of times files changed
        """
        files = DataMiner.extract_changes_per_file(raw_data)
        num_changes = 0

        for k, v in files.items():
            num_changes += v

        return num_changes

    @staticmethod
    def extract_number_entities(raw_data):
        """
        Returns the number of files that have been changed at least once.

        :param raw_data: the output of the git log
        :return: number of files changed
        """
        files = DataMiner.extract_changes_per_file(raw_data)
        return len(files)

    @staticmethod
    def extract_changes_per_file(raw_data):
        """
        Returns the number of times each file has changed.

        :param raw_data: the output of the git log
        :return: dict of filename containing number of changes
        """
        files = {}
        lines = raw_data.strip().split("\n")
        for line in lines:
            # Something like:
            # 3       0       data_miner.py
            # or:
            # -       -       some.png
            m = re.match(r"\s*[\d|-]+\s*[\d|-]+\s*(\S*)", line)
            if m is not None:
                name = m.groups()[0]
                if name in files:
                    files[name] += 1
                else:
                    files[name] = 1
        return files
