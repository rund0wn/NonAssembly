import glob
import pandas as pd

# Get a list of all filenames in the directory that start with 'GO_'
file_list = glob.glob('/ibex/scratch/tawfiqre/Mangrove_16S_refs/deepgo_out/filtered/GO/GO_GO_*.tsv')

# Initialize an empty list to store the dataframes
dfs = []

# Loop over the list of filenames and read in each tsv file
for filename in file_list:
    print(filename)
    # Extract the genus name from the filename
    genus = filename.split('/')[-1][3:-4]
    
    # Read in the tsv file and add a 'GO' column with the genus name
    df = pd.read_table(filename)
    df.insert(loc=0, column='GO', value=genus)
    
    # Append the dataframe to the list
    dfs.append(df)

# Concatenate all dataframes in the list
merged = pd.concat(dfs)
merged.fillna(0, inplace=True)
merged.to_csv('merged_data.csv', index=False)

# Remove all common GO functions
sums = merged.sum(axis = 0)
mask = sums == merged.shape[0]

df2 = merged.drop(columns=mask[mask].index)
df2.to_csv('merged_data_nocommon.csv', index=False)

# Create an empty dataframe for the next step
row_names = ['BS1', 'BS2', 'BS3', 'BS4', 'BS5', 'ER1', 'ER2', 'ER3', 'ER4', 'ER5', 'L1', 'L2', 'L3', 'L4', 'L5', 'RP1', 'RP2', 'RP3', 'RP4', 'RP5', 'RS1', 'RS2', 'RS3', 'RS4', 'RS5']

setupdf = pd.DataFrame(columns = df2.columns, index = row_names)
setupdf = setupdf.drop('GO', axis = 1)
setupdf.to_csv('setup_df.csv')
