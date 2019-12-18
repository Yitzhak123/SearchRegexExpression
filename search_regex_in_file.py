import os
import sys
import argparse
import re
from colorama import Fore, Back, Style


parser = argparse.ArgumentParser(description='Search regex expression in a file')
parser.add_argument("-r", "--regex", action='store',
                    type=str, dest='regex', required=True,
                    help="This is the regex expression "
                         "to search in the files")
parser.add_argument("-f", "--files", action='store', type=str,
                    dest='files', required=True,
                    help="These are the files where we search "
                         "for the regex expression")
parser.add_argument("-u", "--underscore", action="store_true", required=False,
                    help="Add this parameter to print '^' "
                         "under the matching text")
parser.add_argument("-c", "--color", action='store_true', required=False,
                    help="Add this parameter to highlight the matching text")
parser.add_argument("-m", "--machine", action='store_true', required=False,
                    help="Add this parameter to generate machine readable output")

print(sys.argv)
args = parser.parse_args()
print(sys.argv)
print(args)
print(args.underscore)
print(args.regex, args.files)
print(os.environ['HOME'])
