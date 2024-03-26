from pathlib import Path
from library.utilities import *
from library import functions as fun
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
me_NOG_annotations = "data/meNOG.annotations.tsv"
meNOG_members_filename_path = working_directory / meNOG_members
me_NOG_test_filename_path = working_directory / me_NOG_test
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
print(listbox[0:10])
#members_list = readFile(me_NOG_test_filename_path)

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
    NOG_list = []

    for line in members_list:
            Nog = line.split("\t")[1]
            TaxonID_ProteinID = line.split("\t")[5]
            if taxon_ID in TaxonID_ProteinID:
                NOG_list.append(TaxonID_ProteinID)
    return NOG_list

def find_NOG_and_proteinID(taxon_ID, members_list = members_list):
    NOG_dict = {}
    NOG_dict_result = {}
    #ID_list = []
    for line in members_list:
            Nog = line.split("\t")[1]
            TaxonID_ProteinID = line.split("\t")[5]
            NOG_dict[Nog] = TaxonID_ProteinID
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

def find_protein_from_NOG(NOG_list, members_list = members_list):
    NOG_proteinID_dict = {}

    return NOG_proteinID_dict

species1_NOG = fun.NOG_list(species1_tax_id, members_list)
species2_NOG = fun.NOG_list(species2_tax_id, members_list)
species3_NOG = fun.NOG_list(species3_tax_id, members_list)
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

Hs_NOGs = NOG_list(species1_tax_id)
Mm_NOGs = NOG_list(species2_tax_id)
Pt_NOGs = NOG_list(species3_tax_id)
#print("Hs: ", Hs_NOGs)
#print("Mm: ", Mm_NOGs)
#print("Pt: ", Pt_NOGs)

Hs_Pt_Homologs = find_homologs(Hs_NOGs, Pt_NOGs)
#print("Hs pT homologs: ", Hs_Pt_Homologs)
nonhomologs = find_nonhomologs(Hs_Pt_Homologs, Mm_NOGs)
#print("nonhomologs: ", nonhomologs)

def protein_list(taxon_ID, nonhomologs = nonhomologs):
    #returns a list of proteinIDs of one species with the corresponding NOG
    #the output is a list of lists like [NOG, ProteinID]
    protein_list = []
    new_list = []
    dict = find_NOG_and_proteinID(taxon_ID)
    #print("dict: ", dict)
    for key in nonhomologs:
        for protein in dict[key]:
            if protein[0] == taxon_ID:
                protein_list.append([key, protein[1]])
    for list in protein_list:
        if list not in new_list:
            new_list.append(list)
    return new_list

species1_proteins = protein_list(species1_tax_id)
#print("species1_proteins: ", len(species1_proteins))
output_file_proteins = working_directory / "results/proteins.txt"
writeFile(species1_proteins, output_file_proteins)

annotations_list = readFile(me_NOG_annotations_filename_path)

def find_annotations(NOG_list, annotations_list = annotations_list):
    annotated_NOGs_list = []
    new_list = []
    for line in annotations_list:
        for nog in NOG_list:
            if nog in line:
                annotated_NOGs_list.append([nog, line.split("\t")[2], line.split("\t")[4], line.split("\t")[5]])
    for line in annotated_NOGs_list:
        if line not in new_list:
            new_list.append(line)
    return new_list

anno_list = find_annotations(nonhomologs)
output_file_annotations = working_directory / "results/annotations.txt"    

writeFile(anno_list, output_file_annotations)
#print("anno: ", find_annotations(nonhomologs))
    
#nonhomologs = find_nonhomologs(species1_NOG, species2_NOG)
#homologs = find_homologs(species3_NOG, nonhomologs )
#print("nonhomologs of species 1 and 2:", len(nonhomologs))
#print("homologs:", len(homologs))

#print("nonhomologs of Hs and Mm in Pt: ", len(nonhomologs))
#print(find_NOG_and_proteinID(species1_tax_id))
#print(NOG_dict_len(species1_tax_id))
#print(NOG_list(species1_tax_id))