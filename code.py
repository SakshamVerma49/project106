import plotly.express as px
import csv
import numpy as np

with open("data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
    fig.show()

coffee = []
sleep = []

with open("data.csv") as f:
    df = csv.DictReader(f)
    for row in df:
        coffee.append(float(row["Coffee in ml"]))
        sleep.append(float(row["sleep in hours"]))

correlation = np.corrcoef(coffee, sleep)
print(correlation[0, 1])