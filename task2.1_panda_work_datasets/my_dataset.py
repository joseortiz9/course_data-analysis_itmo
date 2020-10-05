import pandas as pd
import matplotlib.pyplot as plt

# Dataset Taken from: https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore.csv
# Download link: https://www.kaggle.com/lava18/google-play-store-apps?resource=download/DpSwfHpLM42wPLJJQ8JZ%2Fversions%2Fb3xEnJAJii7SgRS3kQph%2Ffiles%2Fgoogleplaystore.csv&downloadHash=de08bde8dc99bd289419c0b570da2c886c2405cf77c3c5e1956b634cc5275bc8

df = pd.read_csv("googleplaystore.csv")


# a lot of data should be in other format, so lets make a little of data cleaning
# replace caps locks and spaces in the columns indexes
df.columns = df.columns.str.lower().str.replace(' ', '-')

# Eliminate some chars to transform Installs to numeric
df['size'] = df['size'].map(lambda x: x if x[-1] != 'k' else float(x.replace('k', '')) / 1000)
df['size'] = df['size'].str.replace('M', '')

# price and installs formatting
df['price'] = df['price'].str.replace('$', '')
df['installs'] = df['installs'].str.replace('+', '').str.replace(',', '')

# column type casting
df['rating'] = pd.to_numeric(df['rating'], downcast='float')
df['reviews'] = pd.to_numeric(df['reviews'], errors='coerce', downcast='float')
df['installs'] = pd.to_numeric(df['installs'], errors='coerce', downcast='float')

# last-updated to a handleable date format
df['last-updated'] = pd.to_datetime(df['last-updated'], format='%B %d, %Y', errors='coerce')

# cleaning nan that gave before problems and repeated rows
df = df.drop_duplicates()
df = df[df['installs'].notna()]
df = df.reset_index(drop=True)


# 1
# Which is the percentage of free and paid applications


# 2
# Which is the average price and installs of apps by category


# 3
# Which is the most popular Gender and which are its top 10 apps


# 4
# Which are the most popular categories by number of installs


# 5
# Which apps were last updated before 2016 and have a rating bigger than 4


# 6
# which is the minimum version of android of the top 50 apps that its content rating is for Everyone


# 7
# represent the super light (<2MB) light (2MB;30MB) and bulky(30MB>) by category in a graphic


# 8
#

# 9




