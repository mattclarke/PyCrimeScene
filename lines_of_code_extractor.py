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
        :raises NotADirectoryError: if directory does not exist
        """
        loc_files = {}

        if not os.path.isdir(directory):
            raise NotADirectoryError("Could not find directory {0}".format(directory))

        for root, dirs, files in os.walk(directory):
            # Ignore hidden files etc.
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']

            for file in files:
                full_path = os.path.join(root, file)
                ans = LinesOfCodeExtractor.get_lines_of_code(full_path)

                # Remove the supplied directory as the git log won't have this
                full_path = os.path.relpath(full_path, directory)

                loc_files[full_path] = ans

        return loc_files
