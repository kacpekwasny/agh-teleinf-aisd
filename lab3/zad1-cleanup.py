from distutils.dir_util import copy_tree
from shutil import rmtree

if __name__ == "__main__":
    rmtree("lab3/zadanie1")
    copy_tree("lab3/zadanie1.bqp", "lab3/zadanie1")


