import sys
import pandas as pd

f1 = "Ref_mapping.tsv"
f2 = "merged_data_nocommon.csv"
f3 = "setup_df.csv"

abd = pd.read_csv(f1, sep = '\t')
fct = pd.read_csv(f2, sep = ',')
final = pd.read_csv(f3, sep = ',')

OTUs = fct["GO"].tolist()
sample = abd.columns.values.tolist()
GO = fct.columns.values.tolist()

sample.pop(0)
GO.pop(0)
#print(OTUs, sample, GO)

fct = fct.set_index('GO').transpose()
final = final.set_index('samples').transpose()
abd = abd.set_index('Genus')

#print(final.loc[['GO:0051119']])

for col in final:
    #final_score = 0 
    for f in GO: 
        final_score = 0
        di = {}
        tmp_row = fct.loc[[f]]
        #print(tmp_row)
        #for idx, val in tmp_row.items():
            #di[idx] = val
        get_abundance = []
        for kol, koldata in tmp_row.items(): 
            #print(col, kol)
            if koldata.values > 0:
                get_abundance.append(kol)
        #print(f, col, get_abundance) #GO, sampleID, list of OTUs w/ that GO annotation
        for ot in get_abundance:  
            #print(abd.loc[ot, col])
            final_score += abd.loc[ot, col]
            #print(f, col, final_score) #GO, sampleID, final score of that GO annotation based on abundance of OTUs
        #print(final, f, col, final_score)
        final.loc[f, col] = final_score
        #print(final.loc[f, col])



final.to_csv('edited_' + f3, sep = '\t')
