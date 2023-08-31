import random

# Path to the input FASTA file
input_file_path = 'uniprotkb_taxonomy_id_2_AND_reviewed_tr_2023_08_31.fasta'

# Path to the output file for selected sequences
output_file_path = 'random_proteins.fasta'

# Number of sequences to select
num_sequences_to_select = 3000

# Read the input FASTA file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Split the lines into sequence records based on the '>' headers
sequence_records = []
current_record = []
for line in lines:
    if line.startswith('>'):
        if current_record:
            sequence_records.append(current_record)
            current_record = []
    current_record.append(line)
# Append the last record
if current_record:
    sequence_records.append(current_record)

# Randomly select sequence records
selected_records = random.sample(sequence_records, num_sequences_to_select)

# Write selected sequences to the output file
with open(output_file_path, 'w') as output_file:
    for record in selected_records:
        output_file.writelines(record)

print(f"{num_sequences_to_select} random sequences have been copied to '{output_file_path}'.")
