import pandas as pd

permit_info = pd.read_csv('permits.csv')

# print(permit_info)

# print(permit_info['Permit Type'].unique())
# print(permit_info['Subtype'].unique())

# print(permit_info.groupby(['Subtype']).count())
# print(permit_info.groupby(['Permit Type']).count())
# print(permit_info.count())

print(permit_info[permit_info['Permit Type'] == 'Trade Permit'])

# print(permit_info[permit_info['Permit Type'] == 'Electrical Permit']['Subtype'])

# df[df['A'].str.contains("hello")]

# permit_info[permit_info['Permit Type'].str.contains('Land Disturbance')].to_csv('land_disturbance.csv')

# print(permit_info[permit_info['Permit Type'].str.contains('Land Disturbance')].count())

print(permit_info[permit_info['Permit Type'] == 'Trade Permit']['Subtype'].unique())

# permit_info[permit_info['Subtype'] == 'Electrical Permit']['useful_type'] = 'Electrical Permit'
permit_info.loc[permit_info['Subtype'] == 'Electrical Permit', "useful_type"] = 'Electrical Permit'

# print(permit_info[permit_info['useful_type'] =='Electrical Permit'])
permit_info.loc[permit_info['Subtype'] == 'Mechanical Permit', "useful_type"] = 'Mechanical Permit'

permit_info.loc[permit_info['Subtype'] == 'Plumbing Permit', "useful_type"] = 'Plumbing Permit'
 
permit_info.loc[permit_info['Subtype'] == 'Fire Protection Sprinkler Permit', "useful_type"] = 'Fire Protection Sprinkler Permit'

permit_info.loc[permit_info['Permit Type'].str.contains('Land Disturbance'), "useful_type"] = 'Land Disturbance'

permit_info.loc[permit_info['Permit Type'] == 'Building Permit', "useful_type"] = permit_info['Permit Type'] + " - " + permit_info['Subtype']

# get a count of null values in useful type column
count_of_missing_values=permit_info['useful_type'].isna().sum()

print(count_of_missing_values)
print(len(permit_info.index))

permit_info.loc[permit_info['useful_type'].isna(), "useful_type"] = permit_info['Permit Type']

print(permit_info['useful_type'].isna().sum())
print(len(permit_info.index))


permit_info.to_csv('permits_updated.csv')

