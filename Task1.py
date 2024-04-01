# Import the Tkinter library for GUI development
from tkinter import *
from library import functions as fun
from pathlib import Path
from library.utilities import *
from tkinter import messagebox
from sys import exit
working_directory = Path(__file__).absolute().parent
# If you're using Python 2, you would import it as:
# import Tkinter as tk
# Create the main application window
root = Tk()
# Additional libraries can be imported as needed for your specific project
# For example, if you plan to work with dropdown menu options, you might import tkinter.ttk
# import tkinter.ttk as ttk
eggnog4_species_list = "data/eggnog4.species_list.txt"
eggnog4_species_list_filename_path = working_directory / eggnog4_species_list
meNOG_members = "data/meNOG.members.tsv"
me_NOG_test = "data/Test_members_data.txt"
me_NOG_annotations = "data/meNOG.annotations.tsv"
meNOG_members_filename_path = working_directory / meNOG_members
me_NOG_test_filename_path = working_directory / me_NOG_test
me_NOG_annotations_filename_path = working_directory / me_NOG_annotations

paths = [meNOG_members_filename_path, me_NOG_test_filename_path, me_NOG_annotations_filename_path]

for path in paths:
    obj = Path(path)
    if obj.exists() == False:
        retry = messagebox.showerror("ERROR", f"{path} not found") 

species_list = readFile(eggnog4_species_list_filename_path)
members_list = readFile(meNOG_members_filename_path)
listbox = fun.list_all_species(species_list)



# Create the main application window
# Set the window title
root.title("Final Project - Task 1")
# Set the window dimensions (width x height)
root.geometry("200x200")
# You can also specify a minimum window size (optional)
root.minsize(300, 200)
# You can specify a maximum window size (optional)
root.maxsize(800, 600)

prompt = Label(root, text="Please enter two species names")
prompt.grid(row=0,column=0)
value1 = StringVar()
value2 = StringVar()
value1.set("")
value2.set("")
e1 = Entry(root, textvariable = value1, width=50)
e1.grid(row=1,column=0)
e2 = Entry(root, textvariable = value2, width=50)
e2.grid(row=2,column=0)

def output_homologs(e1=e1, e2=e2, species_list=species_list, members_list=members_list, listbox=listbox): 
    speci1 = e1.get()
    speci2 = e2.get()
    if speci1 == "" and speci2 == "":
        return None
    elif speci1 not in listbox or speci2 not in listbox:
        retry = messagebox.askretrycancel("ERROR", "At least one of the species names you chose is not listed in the DB.\n\n Please also check for spelling errors.") 
        if retry == True:
            value1.set("")
            value2.set("")
            e1 = Entry(root, textvariable = value1, width=50)
            e2 = Entry(root, textvariable = value2, width=50)
            return None
        else:
            exit()
    else:    
        species1_tax = fun.find_TaxonID(speci1, species_list)
        species2_tax = fun.find_TaxonID(speci2, species_list)
        species1_NOG = fun.find_NOGs(species1_tax,members_list)
        species2_NOG = fun.find_NOGs(species2_tax,members_list)
        homologs = fun.find_homologs(species1_NOG, species2_NOG)
        result = Label(root, text= "The number of homologs in the selected species is: " + str(len(homologs)))
        result.grid(row=5, column=0)
        return result

get_homologs = Button(root, command=output_homologs, text="calculate number of homologs")
get_homologs.grid(row=3, column=0)

root.mainloop()