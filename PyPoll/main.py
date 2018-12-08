
import pandas as pd

election_df= pd.read_csv("election_data.csv")


total = len(election_df)

list = election_df["Candidate"].value_counts()
candidates = pd.DataFrame(list)

percent = (candidates["Candidate"]/total)*100
candidates["Percent"]=round(percent)

list_candidates=candidates.index
candidates["Last Name"]=list_candidates

print("Election Results")
print("-----------------------------------------")
print(f'Total Votes: {total}')
print("-----------------------------------------")
for index, row in candidates.iterrows():
    print('{0}'.format(row['Last Name'])+": "+'{0}'.format(row['Percent'])+"% (" + '{0}'.format(row['Candidate'])+")")
print("-----------------------------------------")
print(f'Winner: {candidates["Candidate"].idxmax()}')
print("-----------------------------------------")