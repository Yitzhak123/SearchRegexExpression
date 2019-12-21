import re
from colorama import Fore, Style


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

    def print_line_with_regex(self, line, line_i, pos_tuples=[], filename=''):
        if filename:
            print("finename {}, line number {}".format(filename, line_i))
        else:
            print("line number {}".format(line_i))

    def search_regex_in_files(self):
        """ Search the regex in the file names that were provided and print the
        file names, and the lines were the regex has found according
        to the method 'print_line_with_regex'.
        """
        files = open_files(self._filenames)
        # Go over the files and search for the regex
        for file in files:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                pos_tuples = find_regex_positions_in_line(self._regex, line)
                if pos_tuples:
                    self.print_line_with_regex(line, i, pos_tuples, file.name)

        close_files(files)

    def search_regex_in_custom_lines(self, lines):
        """ Search the regex in the lines and print the
        line numbers were the regex has found.
        """
        for i, line in enumerate(lines, 1):
            pos_tuples = find_regex_positions_in_line(self._regex, line)
            if pos_tuples:
                self.print_line_with_regex(line, i, pos_tuples)


class RegexExpressionSearchAndUnderscore(RegexExpressionSearcher):
    def print_line_with_regex(self, line, line_i, pos_tuples=[], filename=''):
        """Generate a new line under the line with the regex, which have
        the char '^' in the positions we had found the regex. So in the end of
        the process it will print '^' under the regex occurrences.
        """
        indexes_between_pos_tuples = []
        for pos_t in pos_tuples:
            indexes_between_pos_tuples.extend(range(pos_t[0], pos_t[1]))
        clean_line_with_underscores = [' '] * (len(line))
        for i in indexes_between_pos_tuples:
            clean_line_with_underscores[i] = '^'

        if filename:
            prefix = "filename {}, line {}: ".format(filename, line_i)
        else:
            prefix = "line {}: ".format(line_i)
        print(prefix + line, end='')
        prefix2 = ' ' * len(prefix)
        print(prefix2 + ''.join(clean_line_with_underscores))


class RegexExpressionSearchAndHighlight(RegexExpressionSearcher):
    def print_line_with_regex(self, line, line_i, pos_tuples=[], filename=''):
        """ Split the words in the line by the position tuples and add them to
        a new list. Every word that between the position tuple(the regex), we
        highlight the word. In the end we join the list and print the new line.
        """
        list_with_regex_highlighted = []
        i = 0
        for pos_t in pos_tuples:
            list_with_regex_highlighted.append(line[i:pos_t[0]])
            regex = Fore.RED + line[pos_t[0]: pos_t[1]] + Style.RESET_ALL
            list_with_regex_highlighted.append(regex)
            i = pos_t[1]
        list_with_regex_highlighted.append(line[i:])

        if filename:
            prefix = "filename {}, line {}: ".format(filename, line_i)
        else:
            prefix = "line {}: ".format(line_i)
        print(prefix + ''.join(list_with_regex_highlighted), end='')


class RegexExpressionSearchAndGenerateMachineOutput(RegexExpressionSearcher):
    def print_line_with_regex(self, line, line_i, pos_tuples=[], filename=''):
        """ generate a machine output in the format:
        'filename:line_number:start_pos:matched_text'
        """
        for pos_t in pos_tuples:
            regex = line[pos_t[0]: pos_t[1]]
            line_output = "{}:{}:{}:{}".format(filename, line_i, pos_t[0], regex)
            if not filename:
                line_output = line_output[1:]
            print(line_output)
