import pandas as pd
import matplotlib.pyplot as plt

permit_info = pd.read_csv('permits_updated.csv')

print(len(permit_info.index))
print(len(permit_info['Address'].unique()))
print(len(permit_info['useful_type'].unique()))

permits_by_address = pd.get_dummies(permit_info.set_index('Address')['useful_type'])

# print(len(permits_by_address.index))

permits_by_address=permits_by_address.groupby('Address').sum()

print(len(permits_by_address.index))

print(permits_by_address.sum(axis=0))
print(permits_by_address.sum(axis=1))

permits_by_address.sum(axis=1).hist()
plt.show()

permits_by_address.to_csv('permits_by_address.csv')


