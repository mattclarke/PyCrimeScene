import os
import pygount


class LinesOfCodeExtractor(object):
    @staticmethod
    def get_lines_of_code(filename):
        """
        Gets the number of lines of code in the specified file.

        Note: pygount returns fewer lines than cloc or similar because it does not
        count '}' on its own as a line of code.

        :param filename: the file to check
        :return: number of lines of code
        :raises FileNotFoundError: if file is not found
        """
        if os.path.isfile(filename):
            analysis = pygount.source_analysis(filename, 'group')
            return analysis.code
        else:
            raise FileNotFoundError("Could not find file {0}".format(filename))

    @staticmethod
    def get_lines_of_code_for_directory(directory):
        """
        Gets the number of lines of code for all code files in a directory.

        :param directory: the path to the directory
        :return: dictionary of files with their number of lines
        """
        files = {}

        for f in os.listdir(directory):
            full_path = os.path.join(directory, f)
            if os.path.isfile(full_path):
                ans = LinesOfCodeExtractor.get_lines_of_code(full_path)
                files[full_path] = ans
        return files
