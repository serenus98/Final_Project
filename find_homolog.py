from pathlib import Path
#import argparse

working_directory = Path(__file__).absolute().parent

#parser = argparse.ArgumentParser()
#parser.add_argument('species1', help='The name of the first species')
#parser.add_argument('species2', help='The name of the first species')
#args = parser.parse_args()
#species1 = args.species1
#species2 = args.species2

filename = "data/eggnog4.species_list.txt"
filename_path = working_directory / filename

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
species_list = readFile(filename_path)
species1 = "Homo sapiens"
species2 = "Mus musculus"
#print(species_list[1:10])

species_tax_id_dict = {}

for element in species_list:
    species = element.split("\t")[0]
    tax_id = element.split("\t")[1]
    species_tax_id_dict[species] = tax_id

print(species_tax_id_dict)