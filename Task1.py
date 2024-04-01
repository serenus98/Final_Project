# Import the Tkinter library for GUI development
from tkinter import *
from tkinter import messagebox
#import libraries with custom functions
from library import functions as fun
from library.utilities import *
#import packages for file management
from pathlib import Path
from sys import exit
#define working directory --> relative paths
working_directory = Path(__file__).absolute().parent

# Create the main application window
root = Tk()
#define filepaths for datafiles
eggnog4_species_list = "data/eggnog4.species_list.txt"
meNOG_members = "data/meNOG.members.tsv"
me_NOG_annotations = "data/meNOG.annotations.tsv"
meNOG_members_filename_path = working_directory / meNOG_members
eggnog4_species_list_filename_path = working_directory / eggnog4_species_list
me_NOG_annotations_filename_path = working_directory / me_NOG_annotations

#test if files/directories exist, if not show errormessage and terminate application
paths = [meNOG_members_filename_path, eggnog4_species_list_filename_path, me_NOG_annotations_filename_path]

for path in paths:
    obj = Path(path)
    if obj.exists() == False:
        retry = messagebox.showerror("ERROR", f"{path} not found") 

#read the files
species_list = readFile(eggnog4_species_list_filename_path)
members_list = readFile(meNOG_members_filename_path)
listbox = fun.list_all_species(species_list)

# Set the window title
root.title("Final Project - Task 1")
# Set the window dimensions (width x height)
root.geometry("310x200")

#set the application window with two entry fields
prompt = Label(root, text="Please enter two species names")
prompt.grid(row=0,column=0)
value1 = StringVar()
value2 = StringVar()
value1.set("Homo sapiens")
value2.set("Mus musculus")
e1 = Entry(root, textvariable = value1, width=50)
e1.grid(row=1,column=0)
e2 = Entry(root, textvariable = value2, width=50)
e2.grid(row=2,column=0)

def output_homologs(e1=e1, e2=e2, species_list=species_list, members_list=members_list, listbox=listbox):
    #this function takes two species names as input and outputs the number of homologs these two
    #species have. It checks if the speciesnames are in the eggnog-file and displays an error message if not
    #the user can then either cancel his attempt of retry. The entr fields a cleared prior to a new attempt.   
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
        print(species1_NOG)
        homologs = fun.find_homologs(species1_NOG, species2_NOG)
        result = Label(root, text= "The number of homologs in the selected species is: " + str(len(homologs)))
        result.grid(row=5, column=0)
        return result

#the button that calls the output_homologs function
get_homologs = Button(root, command=output_homologs, text="calculate number of homologs")
get_homologs.grid(row=3, column=0)

root.mainloop()