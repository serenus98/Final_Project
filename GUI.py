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
members_list = readFile(meNOG_members_filename_path)
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
#species1 = StringVar()
#species2 = StringVar()
# Create the dropdown menu
#dropdown = OptionMenu(root, selected_option, "Option 1", "Option 2", "Option 3", "Option 4")
#dropdown.pack()
# Run the main event loop

e1 = Entry(root, width=50)
e1.grid(row=5,column=0)
e2 = Entry(root, width=50)
e2.grid(row=6,column=0)

print(e1.get())

def find_TaxonID (species_name, species_list):
    #takes as input, the name of a species and a list of species names with their corresponding 
    #TaxonIDs. The output is the taxonID of that species as a string.
    species_tax_id_dict = {}
    global species_tax_id 
    for element in species_list:
        species = element.split("\t")[0]
        tax_id = element.split("\t")[1]
        species_tax_id_dict[species] = tax_id
    for key in species_tax_id_dict:
        if key == species_name:
            species_tax_id = species_tax_id_dict[key]
    return species_tax_id


def output_homologs(speci1=e1.get(), speci2=e2.get(), species_list=species_list): 
    print("HEREE:" + speci1)
    species1_tax_id = find_TaxonID(speci1, species_list)
    species2_tax_id = find_TaxonID(speci2, species_list)
    species1_NOG = fun.find_NOGs(species1_tax_id,members_list)
    species2_NOG = fun.find_NOGs(species2_tax_id,members_list)
    homologs = fun.find_homologs(species1_NOG, species2_NOG)
    result = Label(root, text= str(len(homologs)))
    result.grid(row=4, column=0)
    return 

get_homologs = Button(root, command=output_homologs, text="calculate number of homologs")
get_homologs.grid(row=3, column=0)


root.mainloop()