import pandas as pd
from itertools import combinations

file = pd.read_csv('Analysis_E_T//PIC Approach1.csv')

df = file.iloc[:, 1:]
ratios = pd.concat([df[a].div(df[b]).rename(f'{a}/{b}') 
                    for a, b in combinations(df.columns, 2)], 1)


upregulated_count = (ratios > 2).sum()
downregulated_count = (ratios < 0.5).sum()


total_ratios = len(ratios)
upregulated_percentage = (upregulated_count / total_ratios) * 100
downregulated_percentage = (downregulated_count / total_ratios) * 100


result_df = pd.DataFrame({
    'Upregulated Count': upregulated_count,
    'Upregulated Percentage': upregulated_percentage,
    'Downregulated Count': downregulated_count,
    'Downregulated Percentage': downregulated_percentage
})


result_df.to_csv("Ratio Counts and Percentages PIC_1.csv", index=True)
