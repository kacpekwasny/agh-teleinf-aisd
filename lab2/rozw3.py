# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath(r".."))

from aidslib.time_measurements import *

SJP_TXT = r"SJP.txt"

"""return list of polish words"""
def load_words(file_path) -> list:
    # after garbage collector clears the file, the .close() method will be called
    return open(file_path, "r", encoding="utf-8").read().splitlines()

def main():
    words_list, t = time_exec_ret(load_words, SJP_TXT)
    print(f"Reading { SJP_TXT.split('/')[-1] } took { t } seconds.")
    
    word_set, t = time_exec_ret(set, words_list)
    print(f"Creating a set from a word list of length {len(words_list)} took {t} seconds.")


    while True:
        inp = input("Please input text in a chosen language: ").strip().lower()
        if inp.lower() == "exit": break
        if " " in inp:
            exit()
        found, t = time_exec_ret( lambda: inp in word_set)
        print(f"Search for the word in a SET took {t} seconds.")
        found, t = time_exec_ret( lambda: inp in words_list)
        print(f"Search for the word in a LIST took {t} seconds.")
        
        print("It is a polish word!" if found  else "Not a polish word!")

if __name__ == "__main__": 
    main()

