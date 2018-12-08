
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

f=open("PyPollOutput.txt","w")
f.write("Election Results\n")
f.write("-----------------------------------------\n")
f.write(f'Total Votes: {total}\n')
f.write("-----------------------------------------\n")
for index, row in candidates.iterrows():
    f.write('{0}'.format(row['Last Name'])+": "+'{0}'.format(row['Percent'])+"% (" + '{0}'.format(row['Candidate'])+")\n")
f.write("-----------------------------------------\n")
f.write(f'Winner: {candidates["Candidate"].idxmax()}\n')
f.write("-----------------------------------------\n")