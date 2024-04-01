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
me_NOG_test = "data/Test_members_data.txt"
me_NOG_test_filename_path = working_directory / me_NOG_test
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
species1 = "Homo sapiens"
species2 = "Mus musculus"
species3 = "Pan troglodytes"

#find the taxonID of the species
species1_tax_id = fun.find_TaxonID(species1, species_list)
species2_tax_id = fun.find_TaxonID(species2, species_list)
species3_tax_id = fun.find_TaxonID(species3, species_list)
print("species1_tax_id: ", species1_tax_id)
print("species2_tax_id: ", species2_tax_id)
print("species3_tax_id: ", species3_tax_id)

#read the files
members_list = readFile(meNOG_members_filename_path)
listbox = fun.list_all_species(species_list)

#find the orthologs groups of the species using the taxonIDs
Hs_NOGs = fun.NOG_list(species1_tax_id, members_list)
Mm_NOGs = fun.NOG_list(species2_tax_id, members_list)
Pt_NOGs = fun.NOG_list(species3_tax_id, members_list)

#a list of orthologs groups homologous to species 1 and 2
homologs_mus_homo = fun.find_homologs(Hs_NOGs, Mm_NOGs)
#a list of orthologs groups homologous to species 1 and 3
Hs_Pt_Homologs = fun.find_homologs(Hs_NOGs, Pt_NOGs)
#a list of orthologs groups homologous to species 1 and 3 but not 2
nonhomologs = fun.find_nonhomologs(Hs_Pt_Homologs, Mm_NOGs)
print("Number of nonhomologs: ", len(nonhomologs))

#writing the proteins with their corresponding orthologous group to a file
species1_proteins = fun.protein_list(species1_tax_id, nonhomologs, members_list)
output_file_proteins = working_directory / "results/proteins.txt"
writeFile(species1_proteins, output_file_proteins)

#writing the annotations with their corresponding orthologous group to a file
annotations_list = readFile(me_NOG_annotations_filename_path)
anno_list = fun.find_annotations(nonhomologs, annotations_list)
output_file_annotations = working_directory / "results/annotations.txt"    
writeFile(anno_list, output_file_annotations)
