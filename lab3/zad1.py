
from distutils.dir_util import copy_tree
from glob import glob
from os import mkdir, getcwd
from shutil import move




def get_filenames():
    return [n.split("\\")[-1] for n in glob("lab3/zadanie1/*")]

def starting_letters(ls: list):
    return set([l[0] for l in ls])

def create_dirs(starting_letters: list):
    for letter in starting_letters:
        mkdir("lab3/zadanie1/" + letter)

def move_files(file_names: list[str]):
    for fn in file_names:
        move(f"lab3/zadanie1/{fn}", f"lab3/zadanie1/{fn[0]}/{fn}")

def backup():
    copy_tree("lab3/zadanie1", "lab3/zadanie1.bqp")
    #try:
    #except:


def main():
    fnames = get_filenames()
    # safety check
    if not fnames or fnames[0] != "BKBQLTII":
        raise FileNotFoundError("you are not in the correct directory, you should have lab3/zadanie1/ in your running directory.")
    
    sl = starting_letters(fnames)
    try:
        create_dirs(sl)
        move_files(fnames)
    except FileNotFoundError:
        print("Files not found.")

if __name__ == "__main__":
    main()
