import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine: str, note: str):
    # Write your code here
    mag = magazine.split(" ")
    notee = note.split(" ")
    
    mag_map = Counter(mag)
    note_map = Counter(notee)
    mag_set = set(mag_map.keys())
    note_set = set(note_map.keys())

    shared_keys = mag_set.intersection(note_set)
    diff_keys = note_set.difference(mag_set)
    # print(diff_keys)
    if len(diff_keys) == 0:
        for i in shared_keys:
            count_mag = mag_map[i]
            count_note = note_map[i]
            if count_mag < count_note:
                print("No")
                exit()
            elif count_mag == count_note:
                print("Yes")
    else:
        print("No")

magazine = "h ghq g xxy wdnr anjst xxy wdnr h h anjst wdnr"
note = "hdd ghq"
checkMagazine(magazine, note)

