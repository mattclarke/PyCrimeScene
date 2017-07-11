import re


class DataMiner(object):
    def extract_number_commits(self, raw_data):
        """
        Returns the number of commits contained in the data.

        Used with prettified output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat

        :param raw_data: the output of the git log
        :return: number of commits in the output
        """
        num_commits = 0
        lines = raw_data.strip().split('\n')
        for line in lines:
            if line.strip().startswith("["):
                num_commits += 1
        return num_commits

    def extract_number_authors(self, raw_data):
        """
        Returns the number of authors who have committed commits.

        Used with prettified output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat

        :param raw_data: the output of the git log
        :return: number of committing authors
        """
        authors = set()
        lines = raw_data.strip().split('\n')
        for line in lines:
            # Something like:
            # [cef94a2] mjc23 2017-07-10 Added DataMiner class
            # As names can contain spaces we need to match up to the date
            m = re.match(r"\s*\[\w*\]\s(\S[\S\s]*\S)\s\d\d\d\d-\d\d-\d\d.*", line)
            if m is not None:
                authors.add(m.groups()[0])
        return len(authors)

    def extract_number_entities_changed(self, raw_data):
        """
        Returns the number of times files have been changed.

        Used with prettified output from:
            git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat

        :param raw_data: the output of the git log
        :return: number of times files changed
        """
        num_changes = 0
        lines = raw_data.strip().split('\n')
        for line in lines:
            # Something like:
            # 3       0       data_miner.py
            # or:
            # -       -       some.png
            m = re.match(r"\s*[\d|-].*", line)
            if m is not None:
                num_changes += 1
        return num_changes

    def extract_number_entities(self, raw_data):
        """
        Returns the number of files that have been changed at least once.

        :param raw_data: the output of the git log
        :return: number of files changed
        """
        files = set()
        lines = raw_data.strip().split('\n')
        for line in lines:
            # Something like:
            # 3       0       data_miner.py
            # or:
            # -       -       some.png
            m = re.match(r"\s*[\d|-]+\s*[\d|-]+\s*(\S*)", line)
            if m is not None:
                files.add(m.groups()[0])
        return len(files)
