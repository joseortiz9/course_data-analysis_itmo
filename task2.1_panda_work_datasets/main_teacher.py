import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime

# 1
data = pd.read_csv("Aids2.csv")  # , parse_dates=['death'], date_parser=custom_date_parser)
# data['death'] = data.loc['death'].apply(lambda x: datetime.fromtimestamp(x))#.astype('datetime64[ns]')


# 2
print('Size:', data.size)
print('Shape:', data.shape)
print('Data types:\n', data.dtypes)

# 3
countBySex = data['sex'].value_counts()
percentageBySex = data['sex'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'
print('number of persons by sex:\n', countBySex)
print('percentage of persons by sex:\n', percentageBySex)

# 4
percentage4 = len(data.query('age < 45 and sex == "M" and status == "A"')) / len(data.query('sex == "M"'))
print('Percentage of alive men under age of 45: ', str(round(percentage4 * 100, 3)) + '%')

# 5
title5 = 'relation age-death, age > 14 over time of death using '
# data5 = data.query('age > 14 and status == "D"').sort_values(by='death')
# line51 = data5.plot.line(x='death', y='age', title=title5+'pandas.plot.line')
# plt.show()

# line52 = px.line(data5, x='death', y='age', title=title5+'pandas.plot.line')
# line52.show()


# 6
title6 = 'Dead people under 30 by state using '
# data6 = data.query('age < 30 and status == "D"')
# valuesByState = data6['state'].value_counts()
# line61 = valuesByState.plot.pie(y='state', startangle=90, autopct='%1.1f%%', title=title6+'pandas.plot.pie')
# plt.show()

# plt.pie(valuesByState.values, labels=valuesByState.axes[0], startangle=90, autopct='%1.1f%%')
# plt.title(title6+'matplotlib.pyplot.pie')
# plt.axis('equal')
# plt.show()


# 7



# 8
data81 = data.query('status == "D"').groupby('state')['age'].max()
print("oldest reported age of people that died by region: \n", data81)
data82 = data.query('status == "D"').groupby('state')['age'].min()
print("youngest reported age of people that died by region: \n", data82)

# averages8 = data.groupby('state')['age'].mean()
# print(averages8[averages8])
# print("regions where infections average was bigger than the old people (from 55): ", 1)

# print("regions where infections average was bigger than the young people (till 55): ", 1)

# print("regions where infections average was bigger than the adult people (31;54): ", 1)

# 9


# 10
