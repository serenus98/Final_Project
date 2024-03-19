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
me_NOG_test = "data/Test_members_data.txt"
meNOG_members_filename_path = working_directory / meNOG_members
me_NOG_test_filename_path = working_directory / me_NOG_test

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
species_list = readFile(eggnog4_species_list_filename_path)
species1 = "Homo sapiens"
species2 = "Mus musculus"
species3 = "Pan troglodytes"
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
species2_tax_id = find_TaxonID(species2)
species3_tax_id = find_TaxonID(species3)
print(species1_tax_id)
print(species2_tax_id)
print(species3_tax_id)
#members_list = readFile(meNOG_members_filename_path)

members_list = readFile(me_NOG_test_filename_path)

#def find_NOGs (taxon_ID, members_list = members_list):
#    NOG_dict = {}
#
#    for line in members_list:
#        Nog = line.split("\t")[1]
#        TaxonID_ProteinID = line.split("\t")[5]
#        if taxon_ID in TaxonID_ProteinID:
#            NOG_dict[Nog] = TaxonID_ProteinID
#    return NOG_dict

def find_NOGs (taxon_ID, members_list = members_list):
    NOG_set = []

    for line in members_list:
            Nog = line.split("\t")[1]
            TaxonID_ProteinID = line.split("\t")[5]
            if taxon_ID in TaxonID_ProteinID:
                NOG_set.append(TaxonID_ProteinID)
    return NOG_set

def find_NOG_and_proteinID(taxon_ID, members_list = members_list):
    NOG_dict = {}
    NOG_dict_result = {}
    ID_list = []
    for line in members_list:
            Nog = line.split("\t")[1]
            TaxonID_ProteinID = line.split("\t")[5]
            NOG_dict[Nog] = TaxonID_ProteinID
            #if taxon_ID in TaxonID_ProteinID:
            #    NOG_dict.append(TaxonID_ProteinID)
    for key in NOG_dict:
        new_protein_list = []
        NOG_dict[key] = NOG_dict[key].split(",")
        for protein in NOG_dict[key]:
            new_protein_list.append(protein.split(".")) 
        NOG_dict[key] = new_protein_list
    for key in NOG_dict:
        for protein in NOG_dict[key]:
            if protein[0] == taxon_ID:
                NOG_dict_result[key] =NOG_dict[key]
    return NOG_dict_result

def NOG_dict_len(taxon_ID):
    dict = find_NOG_and_proteinID(taxon_ID)
    return len(dict)

def NOG_list(taxon_ID):
    NOGs_list = []
    dict = find_NOG_and_proteinID(taxon_ID)
    for key in dict:
        NOGs_list.append(key)
    return NOGs_list

species1_NOG = find_NOGs(species1_tax_id)
species2_NOG = find_NOGs(species2_tax_id)
species3_NOG = find_NOGs(species3_tax_id)
print("species1_NOGs: ", len(species1_NOG))
print("species2_NOGs: ", len(species2_NOG))
print("species3_NOGs: ", len(species3_NOG))

def find_homologs(species1_NOG, species2_NOG):
    homologs = []
    for nog1 in species1_NOG:
        if nog1 in species2_NOG:
            homologs.append(nog1)
    return homologs

homologs_mus_homo = find_homologs(species1_NOG, species2_NOG)

def find_nonhomologs(species1_NOG, species2_NOG):
    nonhomologs = []
    for nog1 in species1_NOG:
        if nog1 not in species2_NOG:
            nonhomologs.append(nog1)
    return nonhomologs

Hs_Pt_Homologs = find_homologs(species1_NOG, species3_NOG)
Mm_Pt_Homologs = find_homologs(species2_NOG, species3_NOG)
nonhomologs = find_nonhomologs(Mm_Pt_Homologs, Hs_Pt_Homologs)

#nonhomologs = find_nonhomologs(species1_NOG, species2_NOG)
#homologs = find_homologs(species3_NOG, nonhomologs )
#print("nonhomologs of species 1 and 2:", len(nonhomologs))
#print("homologs:", len(homologs))

print("nonhomologs of Hs and Mm in Pt: ", len(nonhomologs))
print(find_NOG_and_proteinID(species1_tax_id))
print(NOG_dict_len(species1_tax_id))
print(NOG_list(species1_tax_id))