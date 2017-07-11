import pygount


class LinesOfCodeExtractor(object):
    @staticmethod
    def get_lines_of_code(filename):
        """
        Extracts the number of line of code in the file.

        Note: pygount returns fewer lines than cloc or similar because it does not
        count '}' on its own as a line of code.

        :param filename: the file to check
        :return: number of lines of code
        """
        analysis = pygount.source_analysis(filename, 'group')
        return analysis.code
