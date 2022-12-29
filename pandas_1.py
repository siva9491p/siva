import pandas as pd

mydataset = {'bikes':["honda","splender","scooty"], 'meilage':[40,50,35]}
mydata =pd.DataFrame(mydataset)
#we can also change the index values
#Inder_change = pd.DataFrame(mydataset, index = ['b1','b2','b3'])
#print(Inder_change)
#print(Inder_change.loc['b2'])

print(mydata)
print(mydata.loc[0])

#print(mydata.loc[[0,1]])
print(pd.__version__)

#using pandas Series is used to print the data in column type one by one,[one dimensional array] and it also defines the dtype
a = [1,6,5]
series = pd.Series(a)
print(series)
HAPPY = pd.Series(a, index = [10,20,30])
print(HAPPY) #Lables - it can be used to access a specified value, similiar to our indexes


#we can also locate rows in DataFrames

#comma seperated files
df=pd.read_csv('Data1.txt')
print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())

import numpy as np

import pandas as pd

# Series - Creating a Series by passing a list of values, letting pandas create a default integer index:

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)
print(s[0])

s1 = pd.Series([1, 3, 5, 6, 8])

print(s1)

# Creating a DataFrame by passing a NumPy array, with a datetime index using date_range() and labeled columns:


dates = pd.date_range("20130101", periods=6)

print(dates)

# random float values
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)

# Creating a DataFrame by passing a dictionary of objects that can be converted into a series-like structure:



df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


print(df2)
print(df2.dtypes)


print(df.tail(2))
print("=============")
print(df.head(2))
print("=========")

print(df)


# head and tail
print(df.head(2))

print(df.tail(3))

print(df.index)

print(df.columns)


# while conversion to numpy arrays, compliers omits columns and indexes
print(df.to_numpy())

# with multiple data types,  conversions are expensive

# DataFrame.to_numpy() does not include the index or column labels in the output.

print(df.describe())

print(df2.describe())
# transpose

print(df)

print(df.T)


# sorting

print( df.sort_index(axis=0, ascending=True))


print( df.sort_values(by="B", ascending=False))

# getting values

print(df["A"])

print(df.A)

print(df.B)

# slicing with data frames

print(df[0:3])


# selection - loc() and at()

print(df.loc[dates[0]])

# multi-axis

print(df.loc[:,["A","B"]])

print(df.loc["20130102":"20130104", ["A", "B"]])

print(df.iloc[3:5, 0:2])

print(df.iloc[[1, 2, 4], [0, 2]])

print(df.iloc[:, 1:3])

# Boolean Indexing

print(df[df["A"] > 0])

print(df[df > 0])

print(df)



# is in
df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2["F"] = "1.0"
print( df2 )




df2[df2["E"].isin(["two", "four"])]


# automatic alignment

print(df)

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

print(s1)


df["F"] = s1

print(s1)
print(df)

#Operations

print(df)
print(df.mean())

print (df.mean(1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
df.sub(s, axis="index")
print(s)

# STRING OPERATIONS

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print( s.str.lower())

# concat

df_r = pd.DataFrame(np.random.randn(10, 4))

print(df_r)
print(df_r[:3], df_r[3:7])
print(df_r[7:])

pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)

# join -- works just like sql join

left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)

pd.merge(left, right, on="key")

# Grouping
# Splitting the data into groups based on some criteria
# Applying a function to each group independently
# Combining the results into a data structure

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(df)

df.groupby("A")[["C", "D"]].sum()


print(df.groupby(["A", "B"]).sum())


tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]

df2

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

print(df)

# another complex data
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))


# time series

rng = pd.date_range("1/1/2012", periods=100, freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(ts)

ts.resample("5Min").sum()


import matplotlib.pyplot as plt

plt.close("all")


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

print(ts)

ts.plot();


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

df = df.cumsum()

print(df)

plt.figure();

df.plot();

plt.legend(loc='best');
####################################

import pandas as pd

#df_csv = pd.read_csv('pokemon_data.csv')

df = pd.read_csv("C:/Users/Z004DEYV/PycharmProjects/pythonProject/Pandas/pokemon_data.csv")

print(df)

print(df.tail(5))
# print(df.head(5))

df_xlsx = pd.read_excel('C:/Users/Z004DEYV/PycharmProjects/pythonProject/Pandas/pokemon_data.xlsx')
print(df_xlsx.head(3))

#df_txt = pd.read_csv('C:/Users/Z004DEYV/PycharmProjects/pythonProject/Pandas/pokemon_data.txt', delimiter='\t')

#print(df_txt.head(5))

df['HP']

#### Read Headers
df.columns

## Read each Column
# selection
print(df[['Name', 'Type 1', 'HP']])

## Read Each Row
print(df.iloc[0:4])

for index, row in df.iterrows():
     #print(index, row)

     print(index, row['Name'])

df.loc[df['Type 1'] == "Grass"]

## Read a specific location (R,C)


print(df.iloc[2,1])

# sort
df.sort_values(['Speed'], ascending=True)

df.sort_values(['Type 1', 'Speed'], ascending=[1,0])

# changes to data

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df)

# drop a cloumn from df
df = df.drop(columns=['Total'])
print(df)

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

print(df)

#column operations
cols = list(df.columns)
print(cols)
print(df["Name", "Type 1"])

df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

print(df)
df.head(5)


df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(5)


df.to_csv('D:\\modified.csv', index=False)

df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')

# filter data

print(df['Type 1'] == 'Grass')
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

print(new_df)

new_df.reset_index(drop=True, inplace=True)

new_df

new_df.to_csv('filtered.csv')

# conditional changes


df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

print(df)

df = pd.read_csv('modified.csv')

# aggregate statistics


df = pd.read_csv('modified.csv')

df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']



# working with large amounts of data

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
     results = df.groupby(['Type 1']).count()

     new_df = pd.concat([new_df, results])


pd.dataframe