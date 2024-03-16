from pathlib import Path
#import argparse

working_directory = Path(__file__).absolute().parent

#parser = argparse.ArgumentParser()
#parser.add_argument('species1', help='The name of the first species')
#parser.add_argument('species2', help='The name of the first species')
#args = parser.parse_args()
#species1 = args.species1
#species2 = args.species2

eggnog4_species_list = "data/eggnog4.species_list.txt"
eggnog4_species_list_filename_path = working_directory / eggnog4_species_list
meNOG_members = "data/meNOG.members.tsv"
meNOG_members_filename_path = working_directory / meNOG_members

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
species_list = readFile(eggnog4_species_list_filename_path)
species1 = "Homo sapiens"
species2 = "Mus musculus"
#print(species_list[1:10])

def find_TaxonID (species_name, species_list=species_list):
    species_tax_id_dict = {}
    for element in species_list:
        species = element.split("\t")[0]
        tax_id = element.split("\t")[1]
        species_tax_id_dict[species] = tax_id
    for key in species_tax_id_dict:
        if key == species_name:
            species_tax_id = species_tax_id_dict[key]
    return species_tax_id

species1_tax_id = find_TaxonID(species1)
#species2_tax_id = find_TaxonID(species2)

members_list = readFile(meNOG_members_filename_path)
species1_NOG_list = []

for element in members_list:
    if species1_tax_id in element.split("\t")[5]:
        species1_NOG = element.split("\t")[1]
        species1_NOG_list.append(species1_NOG)
#print(members_list[49:51])
print(species1_NOG_list[:10])
print(len(species1_NOG_list))