import re
import colorama


def find_regex_positions_in_line(regex, line):
    return [(m.start(), m.end()) for m in re.finditer(regex, line)]


def close_files(files):
    try:
        for file in files:
            file.close()
    except IOError as e:
        print(e.message)


def open_files(filenames):
    files = []
    try:
        for fname in filenames:
            files.append(open(fname))
    except IOError as e:
        print(e.message)
    return files


class RegexExpressionSearcher:
    """ the class is used to search a regex in a list of files,
    or against custom input lines.
    Args:
        regex (str): the regex to search.
        filenames (list): list of files to search for the regex.
    """

    def __init__(self, regex, filenames=[]):
        self._regex = regex
        self._filenames = filenames

    def print_line_with_regex(self, line, line_i, positions=[], filename=''):
        if filename:
            print("fine name {}, line number {}".format(filename, line_i))
        else:
            print("line number: {}".format(line_i))

    def search_regex_in_files(self):
        """ Search the regex in the file names that were provided and print the
        file names, and the line numbers were the regex has found.
        """
        files = open_files(self._filenames)
        # Go over the files and search for the regex
        for file in files:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                positions = find_regex_positions_in_line(self._regex, line)
                if positions:
                    self.print_line_with_regex(line, i, positions, file.name)

        close_files(files)

    def search_regex_in_custom_lines(self, lines):
        """ Search the regex in the lines and print the
        line numbers were the regex has found.
        """
        for i, line in enumerate(lines, 1):
            positions = find_regex_positions_in_line(self._regex, line)
            if positions:
                self.print_line_with_regex(line, i, positions)


class RegexExpressionSearchAndUnderscore(RegexExpressionSearcher):
    def print_line_with_regex(self, line, line_i, positions=[], filename=''):
        """Generate a new line under the line with the regex, which have
        the char '^' in the positions we had found the regex. So in hte end of
        the process it will print '^' under the regex occurrences.
        """
        pos_indexes = []
        for pos in positions:
            pos_indexes.extend(range(pos[0], pos[1]))
        clean_line_with_underscores = [' '] * (len(line))
        for i in pos_indexes:
            clean_line_with_underscores[i] = '^'

        prefix = "filename {}, line {}: ".format(filename, line_i)
        print(prefix + line, end='')
        prefix2 = ' ' * len(prefix)
        print(prefix2 + ''.join(clean_line_with_underscores))


class RegexExpressionSearchAndHighlight(RegexExpressionSearcher):
    def print_line_with_regex(self, line, line_i, positions=[], filename=''):
        list_with_regex_highlighted = []
        i = 0
        for pos in positions:
            list_with_regex_highlighted.append(line[i:pos[0]])
            list_with_regex_highlighted.append(line[pos[0]: pos[1]])
            i = pos[1]
