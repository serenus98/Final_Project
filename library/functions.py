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