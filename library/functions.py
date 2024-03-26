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
    NOG_list = []

    for line in members_list:
            Nog = line.split("\t")[1]
            TaxonID_ProteinID = line.split("\t")[5]
            if taxon_ID in TaxonID_ProteinID:
                NOG_list.append(TaxonID_ProteinID)
    return NOG_list

def find_NOG_and_proteinID(taxon_ID, members_list):
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

def NOG_list(taxon_ID, members_list):
    NOGs_list = []
    dict = find_NOG_and_proteinID(taxon_ID, members_list)
    for key in dict:
        for protein in dict[key]:
            if protein[0] == taxon_ID:
                NOGs_list.append(key)
    return NOGs_list