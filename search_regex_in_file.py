import os
import sys
import argparse
import re
from colorama import Fore, Back, Style
from regex_expression_searcher import RegexExpressionSearcher, \
    RegexExpressionSearchAndUnderscore


parser = argparse.ArgumentParser(
    description="Search regex expression in file/s. Get the arguments: "
                "'regex', 'files', 'underscore', 'color', 'machine'. "
                "Notice that you can choose only one of the 3 arguments:"
                "'underscore', 'color', 'machine'")
parser.add_argument("-r", "--regex", action='store',
                    type=str, dest='regex', required=True,
                    help="This is the regex expression "
                         "to search in the files")
parser.add_argument("-f", "--files", action='store', type=str,
                    nargs='*', dest='files', required=False,
                    help="These are the files where we search "
                         "for the regex expression")
# You can choose only one of the 3 arguments below
parser.add_argument("-u", "--underscore", action="store_true", required=False,
                    help="Add this parameter to print '^' "
                         "under the matching text")
parser.add_argument("-c", "--color", action='store_true', required=False,
                    help="Add this parameter to highlight the matching text")
parser.add_argument("-m", "--machine", action='store_true', required=False,
                    help="Add this parameter to generate machine readable output")

print(sys.argv)
args = parser.parse_args()
print(args.underscore)
print(args.regex, args.files)
print(os.environ['HOME'])

additional_arguments = [args.underscore, args.color, args.machine]
if additional_arguments.count(True) > 1:
    print(Fore.RED + "you can choose only one of the 3 arguments: "
          "'underscore', 'color', 'machine'. Please try again" + Style.RESET_ALL)
    sys.exit(1)


if not any(additional_arguments):
    regex_searcher = RegexExpressionSearcher(args.regex, args.files)
    if args.files:
        regex_searcher.search_regex_in_files()
    else:
        print("Enter the lines to search for the regex. Press Q to quit:")
        lines = []
        line = sys.stdin.readline()
        while line != 'Q\n':
            lines.append(line)
            line = sys.stdin.readline()

        regex_searcher.search_regex_in_custom_lines(lines)

elif args.underscore:
    r = RegexExpressionSearchAndUnderscore(args.regex, args.files)
    r.search_regex_in_files()
    print("-u")
