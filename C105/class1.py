import csv

with open('class1.csv', newline='') as f:
     reader = csv.reader(f)
     file_data = list(reader)

# Remove headers
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
     total_marks = total_marks + float(marks[1])

mean = total_marks / total_entries

#print("Mean - Average is : " + str(mean))
print("Mean - Average is : " , mean)

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

graph = px.scatter(df, x="Student Number", y = "Marks")

graph.update_layout(shapes = [ dict( type = 'line', y0 = mean, y1 = mean, x0 = 0, x1 = total_entries ) ])
graph.show()
