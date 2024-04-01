#import packages for file management
from pathlib import Path
from tkinter import messagebox
#import libraries with custom functions
from library.utilities import *
from library import functions as fun
#define working directory --> relative paths
working_directory = Path(__file__).absolute().parent
# define filepaths for datafiles
eggnog4_species_list = "data/eggnog4.species_list.txt"
eggnog4_species_list_filename_path = working_directory / eggnog4_species_list
meNOG_members = "data/meNOG.members.tsv"
meNOG_members_filename_path = working_directory / meNOG_members
me_NOG_annotations = "data/meNOG.annotations.tsv"
me_NOG_annotations_filename_path = working_directory / me_NOG_annotations

#test if files/directories exist, if not show errormessage and terminate application
paths = [meNOG_members_filename_path, eggnog4_species_list_filename_path, me_NOG_annotations_filename_path]

for path in paths:
    obj = Path(path)
    if obj.exists() == False:
        retry = messagebox.showerror("ERROR", f"{path} not found") 
#read the files
species_list = readFile(eggnog4_species_list_filename_path)
#define species names to be used. hard coded since the task was limited and specific 
species1 = "Rattus norvegicus"
species2 = "Mus musculus"

#find the taxonID of the species
species1_tax_id = fun.find_TaxonID(species1, species_list)
species2_tax_id = fun.find_TaxonID(species2, species_list)
print("species1_tax_id: ", species1_tax_id)
print("species2_tax_id: ", species2_tax_id)
members_list = readFile(meNOG_members_filename_path)
Rn_NOGs = fun.NOG_list(species1_tax_id, members_list)
Mm_NOGs = fun.NOG_list(species2_tax_id, members_list)

Rn_Mm_Homologs = fun.find_homologs(Rn_NOGs, Mm_NOGs)
proteinsss = fun.protein_list_2species(["10116","10090"],Rn_Mm_Homologs, members_list)
new_list = []
for protein in proteinsss:
    if protein[0] not in new_list:
        new_list.append(protein[0])

print("Number of NOGs common only to R. norvegicus and M. musculus: ", len(new_list))
annotations_list = readFile(me_NOG_annotations_filename_path)
annos = fun.add_func_cat(proteinsss, annotations_list)
output_file_annotations = working_directory / "results/task3_annotated_data.txt"    
writeFile(annos, output_file_annotations)