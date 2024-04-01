def find_TaxonID (species_name, species_list):
    #takes as input, the name of a species and a list of species names with their corresponding 
    #TaxonIDs. The output is the taxonID of that species as a string.
    species_tax_id_dict = {}
    for element in species_list:
        species = element.split("\t")[0]
        tax_id = element.split("\t")[1]
        species_tax_id_dict[species] = tax_id
    for key in species_tax_id_dict:
        if key == species_name:
            species_tax_id = species_tax_id_dict[key]
    return species_tax_id

def list_all_species(species_list):
    #takes as input, the name of a species and a list of species names with their corresponding 
    #TaxonIDs. The output is the taxonID of that species as a string.
    output_list = []
    for element in species_list:
        species = element.split("\t")[0]
        species = str(species)
        species = species[0].upper() + species[1:]
        output_list.append(species)
        sorted_output = sorted(output_list[1:])
    return sorted_output

def find_NOGs (taxon_ID, members_list):
    #takes the taxonID as input and returns a list of taxonID.ProteinIDs
    NOG_list = []
    for line in members_list:
            Nog = line.split("\t")[1]
            TaxonID_ProteinID = line.split("\t")[5]
            if taxon_ID in TaxonID_ProteinID:
                NOG_list.append(TaxonID_ProteinID)
    return NOG_list

def find_NOG_and_proteinID(taxon_ID, members_list):
    # takes the taxonID as input and returns a dictionary of NOGs as keys and corresponding proteinIDs as values
    # all proteins belong to said taxonID
    NOG_dict = {}
    NOG_dict_result = {}
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

def NOG_list(taxon_ID, members_list):
    # takes the taxonID as input and returns a list of dictionary of NOGs as keys and corresponding proteinIDs as values
    # all proteins belong to said taxonID
    NOGs_list = []
    dict = find_NOG_and_proteinID(taxon_ID, members_list)
    for key in dict:
        for protein in dict[key]:
            if protein[0] == taxon_ID:
                NOGs_list.append(key)
    return NOGs_list

def find_homologs(species1_NOG, species2_NOG):
    # takes two lists of NOGS as input and returns a list of NOGs that appear in both lists
    homologs = []
    for nog1 in species1_NOG:
        if nog1 in species2_NOG:
            homologs.append(nog1)
    return homologs

def find_annotations(NOG_list, annotations_list):
    # takes a list of NOGs as input and returns a list of lists containing the NOG and its corresponding annotations
    # namely, annotation, functional category, and number of proteins
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

def protein_list(taxon_ID, nonhomologs, members_list):
    #returns a list of proteinIDs of one species with the corresponding NOG
    #the output is a list of lists like [NOG, ProteinID]
    protein_list = []
    new_list = []
    dict = find_NOG_and_proteinID(taxon_ID, members_list)
    #print("dict: ", dict)
    for key in nonhomologs:
        for protein in dict[key]:
            if protein[0] == taxon_ID:
                protein_list.append([key, protein[1]])
    for list in protein_list:
        if list not in new_list:
            new_list.append(list)
    return new_list

def find_nonhomologs(species1_NOG, species2_NOG):
    # takes two lists of NOGS as input and returns a list of NOGs that appear only in the first list
    nonhomologs = []
    for nog1 in species1_NOG:
        if nog1 not in species2_NOG:
            nonhomologs.append(nog1)
    return nonhomologs

def find_NOG_and_all_proteinIDs(Homolog_NOG_list, members_list):
    # custom function for Task 3: takes as input the list of homologous NOGs and 
    # returns a list of lists containing the NOG with the corresponding proteinIDs
    NOG_dict = {}
    NOG_dict_result = {}
    newNOGs = {}
    rat_mus_IDs = ["10090", "10116"]
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
    for item in Homolog_NOG_list:
        if item in NOG_dict:
            NOG_dict_result[item] = NOG_dict[item]
    for pro in NOG_dict_result:
        for protein in NOG_dict_result[pro]:
            if protein[0] not in rat_mus_IDs:
                NOG_dict_result[pro] = ""
    for pro in NOG_dict_result:
        if NOG_dict_result[pro] != "":
            newNOGs[pro] = NOG_dict_result[pro]
    return newNOGs

def protein_list_2species(taxon_ID, Homolog_NOG_list, members_list):
    #returns a list of proteinIDs of one species with the corresponding NOG
    #the output is a list of lists like [NOG, ProteinID]
    protein_list = []
    new_list = []
    dict = find_NOG_and_all_proteinIDs(Homolog_NOG_list, members_list)
    for key in dict:
        for protein in dict[key]:
            if protein[0] in taxon_ID:
                protein_list.append([key, protein[1]])
    for list in protein_list:
        if list not in new_list:
            new_list.append(list)
    return new_list

def add_func_cat(Protein_ID_list, annotations_list):
    #takes as input a list of Protein IDs and NOGs and adds the corresponding annotation to that list
    annotated_NOGs_list = []
    new_list = []
    for line in annotations_list:
        for lin in Protein_ID_list:
            if lin[0] in line:
                annotated_NOGs_list.append([lin[0], lin[1], line.split("\t")[4]])
    for line in annotated_NOGs_list:
        if line not in new_list:
            new_list.append(line)
        else:
            new_list.append("\n")
    return new_list