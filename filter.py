import sys
import pandas as pd

filename = sys.argv[1]

# Read the tsv file into a pandas DataFrame
df = pd.read_csv(filename + '.tsv', sep='\t', header=None)

# Print the number of rows before filtering
print('Number of rows before filtering:', len(df))

# Filter the rows based on the last value
filtered_df = df[df.iloc[:, -1] >= 0.3]

# Print the number of rows after filtering
print('Number of rows after filtering:', len(filtered_df))

# Write the filtered rows to a new tsv file
filtered_df.to_csv('filtered_' + filename + '.tsv', sep='\t', index=False, header=False)
