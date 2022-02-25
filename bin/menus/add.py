# Script for adding file in the safe folder 

from tkinter.filedialog import askopenfilename
import shutil

def add_file(username):
    print("Choose a file to add in the safe: ")
    filename = askopenfilename()

    print("File chosen: ", filename)

    # Adding escape character for shutil library
    original = "r'" + filename + "'"
    target = "../data/" + ".data_to_protect_" + username
    shutil.copyfile(original, target)
