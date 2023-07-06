import pandas as pd

with open("./140_genes.txt") as file:
    total_gene_list = []
    for line in file:
        total_gene_list.append(line.strip())

data = pd.read_csv("./genes_to_represent.csv",sep=";")

string_db_list = []

for gene in total_gene_list:

    for row in data.iterrows():
        row_object = row[1]
        list_name = row_object["description"]
        gene_hits = row_object["gene_hits"]
        gene_list = gene_hits.split(";")
        if gene in gene_list:
            string_db_list.append(gene)

# The set method removes duplicate elements from a list
processed_string_db_list = [*set(string_db_list)]
print(processed_string_db_list)
print(len(processed_string_db_list))



with open("./genes_for_stringDB.txt", mode="w") as file:
    for item in processed_string_db_list:
        file.write(f"{item}\n")

