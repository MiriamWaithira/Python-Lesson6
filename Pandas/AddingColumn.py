import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Add a new column
df['salary'] = [50000, 60000, 70000]
print(df)