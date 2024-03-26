# Import the Tkinter library for GUI development
from tkinter import *
from library import functions as fun
from pathlib import Path
from library.utilities import *

working_directory = Path(__file__).absolute().parent

eggnog4_species_list = "data/eggnog4.species_list.txt"
eggnog4_species_list_filename_path = working_directory / eggnog4_species_list
meNOG_members = "data/meNOG.members.tsv"
me_NOG_test = "data/Test_members_data.txt"
me_NOG_annotations = "data/meNOG.annotations.tsv"
meNOG_members_filename_path = working_directory / meNOG_members
me_NOG_test_filename_path = working_directory / me_NOG_test
me_NOG_annotations_filename_path = working_directory / me_NOG_annotations

species_list = readFile(eggnog4_species_list_filename_path)
# If you're using Python 2, you would import it as:
# import Tkinter as tk
# Create the main application window
root = Tk()
# Additional libraries can be imported as needed for your specific project
# For example, if you plan to work with dropdown menu options, you might import tkinter.ttk
# import tkinter.ttk as ttk

# Create the main application window
# Set the window title
root.title("Final Project")
# Set the window dimensions (width x height)
root.geometry("500x500")
# You can also specify a minimum window size (optional)
root.minsize(300, 200)
# You can specify a maximum window size (optional)
root.maxsize(800, 600)
# Create a StringVar to hold the selected option
species1 = StringVar()
species2 = StringVar()
# Create the dropdown menu
#dropdown = OptionMenu(root, selected_option, "Option 1", "Option 2", "Option 3", "Option 4")
#dropdown.pack()
# Run the main event loop

listbox1 = Listbox(root)
listbox1.grid(row=0, column=0, pady=0, padx=10)
listbox2 = Listbox(root)
listbox2.grid(row=0, column=1, pady=20, padx=10)

species_listbox = fun.list_all_species(species_list)

for species in species_listbox:
    listbox1.insert(END, species)
    listbox2.insert(END, species)

selection1 = Label(root, text= "none")
selection1.grid(row=2, column=0)
selection2 = Label(root, text= "none")
selection2.grid(row=2, column=1)

def show1(selection1=selection1, listbox1=listbox1):
    species1 = listbox1.get(ANCHOR)
    selection1 = Label(root, text="")
    selection1 = Label(root, text=species1)
    selection1.grid(row=2, column=0)
    return species1
def show2(selection2=selection2, listbox2=listbox2):
    species2 = listbox2.get(ANCHOR)
    selection2 = Label(root, text="")
    selection2 = Label(root, text=species2)
    selection2.grid(row=2, column=1)
    return species2


select_species1 = Button(root, command=show1, text="select species1")
select_species2 = Button(root, command=show2, text="select species2")
select_species1.grid(row=1, column=0)
select_species2.grid(row=1, column=1)

get_homologs = Button(root, command=fun.find_homologs)

root.mainloop()