import csv
import numpy as np
from scipy import stats
import json

filename = 'febdata.csv'
hours = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
days = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
feature_names = ["acousticness", "danceability", "energy", "tempo", "valence", "loudness", "insturmentalness", "speechiness"]


def get_cdf(hours, currhour, feature_ind):
  # calulate median of this hour
  median = np.median(np.array([float(j[feature_ind]) for j in hours[currhour]]))
  # get feature across all hours and calculate cdf
  x = []
  for hour in hours:
    for i in hour:
      x.append(float(i[feature_ind]))

  x = np.array(x)
  cdf = stats.norm.cdf(median, np.mean(x), np.std(x))

  return [round(cdf, 2),round(median, 2)]

def get_top_3(hours, i, item_ind):
  items = np.array([j[item_ind] for j in hours[i]])
  top3 = []
  for k in range(3):
    mode = stats.mode(items)
    top3.append(mode[0][0])
    items = np.delete(items, np.argwhere(items==mode[0][0]))
  return top3

def getRawData(filename):
  rawData = []
  with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[5] != 'Time':
          day = int(row[4].split('-')[1])
          if (day <= 28):
            hour = (int(row[5].split(':')[0]) + 16) % 24 # time zone adjustment 
            data = {
              "Artist": row[0],
              "Track": row[2],
              "Day": day,
              "Time": hour,
              "Acousticness": float(row[6]),
              "Danceability": float(row[7]),
              "Energy": float(row[8]),
              "Tempo": float(row[9]),
              "Valence": float(row[10]),
              "Loudness": float(row[11]),
              "Insturmentalness": float(row[12]),
              "Speechiness": float(row[13])
            }
            rawData.append(data)
            hours[hour].append(row)
            days[day - 1].append(row)
  
def getDailyData():
  entries = []  
  for j in range(len(feature_names)):
    for i in range(len(hours)): 
      # this format is weirder, but fits d3 better (each measure and hour has its own entry)
        if hours[i]:
          entry = {
          "Measure": str(feature_names[j]),
          "Time": str(i) + ":" + "00",
          "ScaledAverage": get_cdf(hours, i, j + 6)[0],
          "RealAverage": get_cdf(hours, i, j + 6)[1],
          "TopSongs": get_top_3(hours, i, 2),
          "TopArtists": get_top_3(hours, i, 0)
          }
        else: 
          entry = {
          "Measure": str(feature_names[j]),
          "Time": str(i) + ":" + "00",
          "ScaledAverage": "N/A",
          "RealAverage": "N/A",
          "TopSongs": [],
          "TopArtists": []
          }
        entries.append(entry)

  with open("dailydata.json", "w") as outfile:
      json.dump(entries, outfile)

def getMonthlyData():
  entries = []  
  for j in range(len(feature_names)):
    for i in range(len(days)): 
      # this format is weirder, but fits d3 better (each day and hour has its own entry)
        if days[i]:
          entry = {
          "Measure": str(feature_names[j]),
          "Time": str(i + 1), # days start from 1
          "ScaledAverage": get_cdf(days, i, j + 6)[0],
          "RealAverage": get_cdf(days, i, j + 6)[1],
          "TopSongs": get_top_3(days, i, 2),
          "TopArtists": get_top_3(days, i, 0)
          }
        else: 
          entry = {
          "Measure": str(feature_names[j]),
          "Time": str(i + 1),
          "ScaledAverage": "N/A",
          "RealAverage": "N/A",
          "TopSongs": [],
          "TopArtists": []
          }
        entries.append(entry)

  with open("monthlydata.json", "w") as outfile:
    json.dump(entries, outfile)

### code 
getRawData(filename)
getDailyData()
getMonthlyData()
