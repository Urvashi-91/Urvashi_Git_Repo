import pandas as pd
data = [
     ("Dexter","Johnsons","dog","shiba inu","red sesame",1.5,35,"m",False,"both",True),
     ("Alfred","Johnsons","cat","mix","tuxedo",4,12,"m",True,"indoor",True),
     ("Petra","Smith","cat","ragdoll","calico",None,10,"f",False,"both",True),
     ("Ava","Smith","dog","mix","blk/wht",12,32,"f",True,"both",False),
     ("Schroder","Brown","cat","mix","orange",13,15,"m",False,"indoor",True),
     ("Blackbeard","Brown","bird","parrot","multi",5,3,"f",False,"indoor",),
    ]
print (data)
labels = ["name","owner","type","breed","color","age","weight","gender","health issues","indoor/outdoor","vaccinated"]
vet_records = pd.DataFrame.from_records(data, columns=labels)
print (vet_records)

'''Dataframe to view large data
head is for first 5 data set, tail is for last 5 data set'''

print(vet_records.head())
print(vet_records.dtypes) #to know data types
print(vet_records.type.count()) # to know number of records of a column, excluding none values, Pandas skips none or nan
print(vet_records.groupby('type').count()) #to groupby a column
print(vet_records.type.value_counts()) #to count number of entries of each entry in a column


'''Slicing Dataframe'''
vet_records_archive = vet_records # archive the original data
print(vet_records_archive)
weight = vet_records['weight'] #sliced out the weight column and doesnt change the vet_records
dog_weight = vet_records.weight[vet_records.type=='dog'] #slicing out content based on a condition
print (dog_weight)
dogs = vet_records[vet_records.type=='dog'] #when I dint specify what type of data is needed from the satisfied condition rows
print(dogs)
print(vet_records.loc[:,["name","owner"]]) #: is for all rows and rest two specify which column is needed
print(vet_records.loc[2:3,["name","owner"]]) #specify row range and column names
print(vet_records.iloc[[2,3],[4,5]]) #specify row indexes and column indexes
print(vet_records[vet_records.name.isin(['Dexter','Blackbeard'])]) #to select data if it is in the record & add '~' for Not true

'''Pivot tables'''
table = pd.pivot_table(vet_records, values=['weight','age'], index=['type', 'breed'], aggfunc=sum) #pivot_tables(data, values to represent, what indexes to use, and function to apply
print (table)
'''aggfunc could be a numpy function such as np.mean'''
print (vet_records.describe()) #only works on number type stats
print (vet_records.isna()) #if there is a mising data
vet_records_value = vet_records.fillna(0) #fill na values with 0
print(vet_records_value)
values = {"age": 12, "vaccinated": False} #Use dictionary to fill in gaps or mising values with the specified value
vet_records_dict = vet_records.fillna(value=values) #filling na with values dictionary
print (vet_records_dict.describe())