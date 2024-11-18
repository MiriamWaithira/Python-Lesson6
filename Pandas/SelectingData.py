import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Select a single column
print(df['name'])

# Select multiple columns
print(df[['name', 'age']])

# Select rows by index
print(df.loc[0])

# Select rows by condition
print(df[df['age']>= 30])