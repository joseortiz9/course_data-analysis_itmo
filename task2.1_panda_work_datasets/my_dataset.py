import pandas as pd
import matplotlib.pyplot as plt

# Dataset Taken from: https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore.csv
# Download link: https://www.kaggle.com/lava18/google-play-store-apps?resource=download/DpSwfHpLM42wPLJJQ8JZ%2Fversions%2Fb3xEnJAJii7SgRS3kQph%2Ffiles%2Fgoogleplaystore.csv&downloadHash=de08bde8dc99bd289419c0b570da2c886c2405cf77c3c5e1956b634cc5275bc8

data = pd.read_csv("googleplaystore.csv")

print(data)


