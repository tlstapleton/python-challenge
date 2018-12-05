
import pandas as pd

election_data = "election_data.csv"

election_df= pd.read_csv(election_data)

election_df.head()

total = len(election_df)

election_df["Candidate"].unique()

list = election_df["Candidate"].value_counts()
candidates = pd.DataFrame(list)

percent = (candidates["Candidate"]/total)*100
percent = round(percent,3)
candidates["Percent"]=percent

candidates["Candidate"][0]

list_candidates=candidates.index

candidates["Last Name"]=list_candidates



print("Election Results")
print("-----------------------------------------")
print(f'Total Votes: {total}')
print("-----------------------------------------")
for index, row in candidates.iterrows():
    print('{0}'.format(row['Last Name'])+": "+'{0}'.format(row['Percent'])+"% (" + '{0}'.format(row['Candidate'])+")")



