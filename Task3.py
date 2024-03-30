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
species1 = "Rattus norvegicus"
species2 = "Mus musculus"

species1_tax_id = fun.find_TaxonID(species1, species_list)
species2_tax_id = fun.find_TaxonID(species2, species_list)
print("species1_tax_id: ", species1_tax_id)
print("species2_tax_id: ", species2_tax_id)
members_list = readFile(meNOG_members_filename_path)
#members_list = readFile(me_NOG_test_filename_path)
Rn_NOGs = fun.NOG_list(species1_tax_id, members_list)
Mm_NOGs = fun.NOG_list(species2_tax_id, members_list)

Rn_Mm_Homologs = fun.find_homologs(Rn_NOGs, Mm_NOGs)
#print(Rn_Mm_Homologs)
#Rn_Mm_NOG = fun.find_NOG_and_all_proteinIDs(Rn_Mm_Homologs, members_list)
proteinsss = fun.protein_list_2species(["10116","10090"],Rn_Mm_Homologs, members_list)
print(proteinsss)
annotations_list = readFile(me_NOG_annotations_filename_path)
annos = fun.add_func_cat(proteinsss, annotations_list)
print(annos)
output_file_annotations = working_directory / "results/task3_annotated_data.txt"    
writeFile(annos, output_file_annotations)