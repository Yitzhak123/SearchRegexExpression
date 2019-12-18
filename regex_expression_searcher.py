import re
import colorama


def find_regex_positions_in_line(regex, line, line_i):
    return [(line_i, m.start(), m.end()) for m in re.finditer(regex, line)]


class RegexExpressionSearcher:
    matches = {}

    def __init__(self, regex, filenames=[], lines=[]):
        self._regex = regex
        self._filenames = filenames
        self._lines = lines

    def search_regex_in_files(self):
        files = []
        try:
            for fname in self._filenames:
                files.append(open(fname))
        except IOError as e:
            print(e.message)

        for file in files:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                self.matches[file.name] = find_regex_positions_in_line(self._regex, line, i)

    def search_regex_in_text(self):
        for i, line in enumerate(self._lines, 1):
            self.matches['stdin'] = find_regex_positions_in_line(self._regex, line)
