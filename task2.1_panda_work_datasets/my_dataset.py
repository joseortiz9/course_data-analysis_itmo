import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Dataset Taken from: https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore.csv
# Download link: https://www.kaggle.com/lava18/google-play-store-apps?resource=download/DpSwfHpLM42wPLJJQ8JZ%2Fversions%2Fb3xEnJAJii7SgRS3kQph%2Ffiles%2Fgoogleplaystore.csv&downloadHash=de08bde8dc99bd289419c0b570da2c886c2405cf77c3c5e1956b634cc5275bc8

df = pd.read_csv("googleplaystore.csv")


# 0
# a lot of data should be in other format, so lets make a little of data cleaning
# replace caps locks and spaces in the columns indexes
df.columns = df.columns.str.lower().str.replace(' ', '-')

# Eliminate some chars to transform Installs to numeric
df['size'] = df['size'].map(lambda x: x if x[-1] != 'k' else float(x.replace('k', '')) / 1000)
df['size'] = df['size'].str.replace('M', '')

# price and installs formatting
df['price'] = df['price'].str.replace('$', '')
df['installs'] = df['installs'].str.replace('+', '').str.replace(',', '')

# check type should be 'Free' or 'Paid', else set nan to be deleted later
df['type'] = df['type'].map(lambda x: x if x == 'Free' or x == 'Paid' else np.nan)

# column type casting
df['rating'] = pd.to_numeric(df['rating'], downcast='float')
df['reviews'] = pd.to_numeric(df['reviews'], errors='coerce', downcast='float')
df['installs'] = pd.to_numeric(df['installs'], errors='coerce', downcast='float')
df['price'] = pd.to_numeric(df['price'], errors='coerce', downcast='float')

# last-updated to a handleable date format
df['last-updated'] = pd.to_datetime(df['last-updated'], format='%B %d, %Y', errors='coerce')

# cleaning nan that gave before problems and repeated rows
df = df.drop_duplicates(subset=['app'])
df = df[df['installs'].notna()]
df = df[df['type'].notna()]
df = df.reset_index(drop=True)

# 0.1
print('Size:', df.size)
print('Shape:', df.shape)
print('Data types:\n', df.dtypes)


# 1
# Which is the percentage of free and paid applications?
percentageByType = df['type'].value_counts(normalize=True).mul(100).round(3).astype(str) + '%'
#print('percentage of apps by type:\n', percentageByType)

# how this percentage is related to the category they belong to?
data1 = df.groupby(['category', 'type']).size().unstack()
plot_data1 = data1.apply(lambda x: x*100/sum(x), axis=1)
#print(data1)
#graph1 = plot_data1.plot.barh(rot=0, stacked=True, title="Percentage of Free vs Paid apps by Category")
#graph1.set(xlabel='Percentage by type (%)', ylabel='Category')
#plt.show()


# 2
# Which is the average price and installs of apps by content rating
data2 = df.groupby(['content-rating']).agg({'installs': 'mean', 'price': 'mean'})
#print(data2)
#graph2 = data2.plot.bar(rot=0, subplots=True, title="Average of installs and price by category")
#plt.show()


# 3
# Which is the most popular Genre and which are its top 10 apps
popular_genre3 = tuple(df.groupby('genres')['installs'].sum().apply(['idxmax', 'max']))
print("The most popular genre is:", popular_genre3[0], "with more than", popular_genre3[1], 'installs')
popular_apps3 = df[df['genres'] == popular_genre3[0]][['app', 'installs']].sort_values(by='installs', ascending=False).head(10).reset_index(drop=True)
popular_apps3.index += 1
print("Top ten apps from the most popular genre", popular_apps3)


# 4
# which is the year with more application last updates, represent the number of updates over time
title4 = "Year with most number of apps updated"
most_popular_year4 = tuple(df.groupby(df['last-updated'].dt.year).size().apply(['idxmax', 'max']))
print("The year with most last update is:", most_popular_year4[0], "with more than", most_popular_year4[1], 'apps updated')
plot_data4 = df[df['last-updated'].dt.year == most_popular_year4[0]]['last-updated'].value_counts().sort_values(ascending=True)
plot_df4 = pd.DataFrame({'last-updated': plot_data4.index, 'count': plot_data4.values})
# graph4 = plot_data4.plot.line(xlabel='update dates', ylabel='number of apps', title=title4)
# plt.show()


# 5
# Find the worst app, means that is not free, was last updated before 2016,
# have a rating lower than 2 and is the less installed
worst_app5 = df[df['last-updated'] < "2016-01-01"].query('rating < 2 and type == "Paid"').sort_values(by='reviews').iloc[0]
print(worst_app5)


# 6
# which is the minimum version of android of the categories of the top 100 apps that its content rating is for Everyone
top_apps6 = df[df['content-rating'] == "Everyone"].sort_values(by='installs', ascending=True).head(100).reset_index(drop=True)
plot_data6 = top_apps6.groupby('category')['android-ver'].value_counts().unstack()
graph6 = plot_data6.plot.barh(rot=0, stacked=True, title="min. version of the categ. of top 100 apps")
graph6.set(xlabel='amount of apps', ylabel='Category')
plt.show()


# 7
# how many apps are in each: super light (<2MB) light (2MB;30MB) bulky(30MB>) and 'varies with device'






