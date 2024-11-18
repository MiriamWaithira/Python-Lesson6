import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Minnesota'],
        'salary': [50000, 60000, 70000, 40000]}

df = pd.DataFrame(data)

# Group by age and get the average salary for each group
grouped = df.groupby('age')['salary'].mean()
print(grouped)