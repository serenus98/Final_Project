from pathlib import Path
from library.utilities import *
from library import functions as fun

working_directory = Path(__file__).absolute().parent

eggnog4_species_list = "data/eggnog4.species_list.txt"
eggnog4_species_list_filename_path = working_directory / eggnog4_species_list
meNOG_members = "data/meNOG.members.tsv"
meNOG_members_filename_path = working_directory / meNOG_members
me_NOG_test = "data/Test_members_data.txt"
me_NOG_test_filename_path = working_directory / me_NOG_test
me_NOG_annotations = "data/meNOG.annotations.tsv"
me_NOG_annotations_filename_path = working_directory / me_NOG_annotations
 
species_list = readFile(eggnog4_species_list_filename_path)
species1 = "Homo sapiens"
species2 = "Mus musculus"
species3 = "Pan troglodytes"

species1_tax_id = fun.find_TaxonID(species1, species_list)
species2_tax_id = fun.find_TaxonID(species2, species_list)
species3_tax_id = fun.find_TaxonID(species3, species_list)
print("species1_tax_id: ", species1_tax_id)
print("species2_tax_id: ", species2_tax_id)
print("species3_tax_id: ", species3_tax_id)
members_list = readFile(meNOG_members_filename_path)
listbox = fun.list_all_species(species_list)

species1_NOG = fun.NOG_list(species1_tax_id, members_list)
species2_NOG = fun.NOG_list(species2_tax_id, members_list)
species3_NOG = fun.NOG_list(species3_tax_id, members_list)

homologs_mus_homo = fun.find_homologs(species1_NOG, species2_NOG)

Hs_NOGs = fun.NOG_list(species1_tax_id, members_list)
Mm_NOGs = fun.NOG_list(species2_tax_id, members_list)
Pt_NOGs = fun.NOG_list(species3_tax_id, members_list)

Hs_Pt_Homologs = fun.find_homologs(Hs_NOGs, Pt_NOGs)
nonhomologs = fun.find_nonhomologs(Hs_Pt_Homologs, Mm_NOGs)
print("Number of nonhomologs: ", len(nonhomologs))

species1_proteins = fun.protein_list(species1_tax_id, nonhomologs, members_list)
output_file_proteins = working_directory / "results/proteins.txt"
writeFile(species1_proteins, output_file_proteins)

annotations_list = readFile(me_NOG_annotations_filename_path)
anno_list = fun.find_annotations(nonhomologs, annotations_list)
output_file_annotations = working_directory / "results/annotations.txt"    
writeFile(anno_list, output_file_annotations)
