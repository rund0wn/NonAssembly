import pandas as pd
import os
import sys

filename = sys.argv[1]

# Read the input tsv file
df = pd.read_csv(filename, sep='\t')


# Count the frequency of each GO term
go_counts = df['GO_functions'].value_counts()

# Create a new dataframe with the count of each GO term
go_counts_df = pd.DataFrame({'GO_functions': go_counts.index, 'count': go_counts.values})

# Transpose the dataframe and change the name of the row to the name of the genus
new_df = go_counts_df.set_index('GO_functions').transpose()
genus = os.path.splitext(filename)[0]
new_df = new_df.rename(index={'count': genus})

# Save dataframe to a new file
new_df.to_csv('GO_' + genus + '.tsv', sep = '\t', index = False)
