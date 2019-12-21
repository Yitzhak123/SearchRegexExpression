#!/bin/bash


regex='..am'
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt -u
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt -c
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt -m
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt -c -u
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt -c -u -m
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt -c -m
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt bad_filename.txt -u
python search_regex_in_file.py -r $regex -f temp.txt bad_filename.txt temp2.txt  temp3.txt -u
python search_regex_in_file.py -r $regex -f temp.txt temp2.txt temp3.txt -u

# Now test with user input
python search_regex_in_file.py -r $regex -f
python search_regex_in_file.py -r $regex
python search_regex_in_file.py -r $regex -u
python search_regex_in_file.py -r $regex -c
python search_regex_in_file.py -r $regex -m
python search_regex_in_file.py -r $regex -u -c
python search_regex_in_file.py -r $regex -u -m
python search_regex_in_file.py -r $regex -f -c -u -m
