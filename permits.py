import pandas as pd
''' first cleanup script second in pipeline is permit_analysis.py and this script outputs permits_updated.csv
'''
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

# change Building Permit (Commercial/Multi-Family),Building Permit (Residential)

permit_info.loc[permit_info['Permit Type'] == 'Building Permit (Residential)','Permit Type'] = 'Building Permit'

permit_info.loc[permit_info['Permit Type'] == 'Building Permit (Commercial/Multi-Family)','Permit Type'] = 'Building Permit'

permit_info.loc[(permit_info['Permit Type'] == 'Building Permit') & ( ~permit_info['Subtype'].isin(['Additions','New Construction','Alterations/Repairs']) ) ,'Subtype' ] = 'Other'
                
'''Building Permit - Additions,Building Permit - Alterations/Repairs,Building Permit - New Construction'''


# permit_info.loc[permit_info['Permit Type'] == 'Building Permit', "useful_type"] = permit_info['Permit Type'] + " - " + permit_info['Subtype']

permit_info.loc[permit_info['Permit Type'] == 'Building Permit', "useful_type"] = permit_info['Permit Type'] + " - " + permit_info['Subtype']

#these are wrong
# Zoning - Site Plan Approval (Land Use Certificate),Zoning - Site Plan Approval( Land Use Certificate),Zoning - Verification Request,Zoning Verification Request Other - ARB Certificate of Appropriateness,Other - Certificate of Appropriateness,Other - Mortgage Acceptance Letter,Other- ARB Certificate of Appropriateness, ARB Certificate of Appropriateness, Certificate of Appropriateness

#condensing all "certificate of appropriatness"
permit_info.loc[permit_info['Permit Type'] == 'Other- ARB Certificate of Appropriateness','Permit Type'] = 'Certificate of Appropriateness'

permit_info.loc[permit_info['Permit Type'] == 'Other - ARB Certificate of Appropriateness','Permit Type'] = 'Certificate of Appropriateness'


permit_info.loc[permit_info['Permit Type'] == 'Other - Certificate of Appropriateness','Permit Type'] = 'Certificate of Appropriateness'


permit_info.loc[permit_info['Permit Type'] == 'ARB Certificate of Appropriateness','Permit Type'] = 'Certificate of Appropriateness'


#zoning clean up

permit_info.loc[permit_info['Permit Type'] == 'Zoning Verification Request','Permit Type'] = 'Zoning - Verification Request'


permit_info.loc[permit_info['Permit Type'] == 'Zoning - Site Plan Approval( Land Use Certificate)','Permit Type'] = 'Zoning - Site Plan Approval (Land Use Certificate)'

# get a count of null values in useful type column
count_of_missing_values=permit_info['useful_type'].isna().sum()

print(count_of_missing_values)
print(len(permit_info.index))

permit_info.loc[permit_info['useful_type'].isna(), "useful_type"] = permit_info['Permit Type']

print(permit_info['useful_type'].isna().sum())
print(len(permit_info.index))


permit_info.to_csv('permits_updated.csv')

