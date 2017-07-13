class HotSpotCompiler(object):
    @staticmethod
    def merge_raw_data(commits, lines_of_code):
        """
        Creates a list of the files sorted primarily by the number of changes and secondly
        by the number of lines of code.

        :param commits: a dict of file names and the number of commits
        :param lines_of_code: a dict of file names and the number of lines of code
        :return: a sorted list of tuple (name, changes, lines)
        """
        data = []
        for k, v in commits.items():
            data.append((k, v, lines_of_code[k]))
        # Sort on secondary key
        data = sorted(data, key=lambda x: x[2], reverse=True)
        # Sort on primary key - this gives sorted by first value then by second value
        return sorted(data, key=lambda x: x[1], reverse=True)
