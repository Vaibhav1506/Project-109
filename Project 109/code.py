from decimal import DivisionByZero
import random
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import csv


df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
print("The mean is " + str(mean))

median = statistics.median(data)
print("The median is " + str(median))

mode = statistics.mode(data)
print("The mode is " + str(mode))

str_dev = statistics.stdev(data)
print("The Standard Deviation is " + str(str_dev))

firstStdDevStart, firstStdDevEnd = mean-str_dev, mean+str_dev
list_of_data_within_1_str_dev = [result for result in data if result > firstStdDevStart and result < firstStdDevEnd]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_str_dev)*100.0/len(data))) 

secondStdDevStart, secondStdDevEnd = mean-(2*str_dev), mean+ (2*str_dev)
list_of_data_within_2_str_dev = [result for result in data if result > secondStdDevStart and result < secondStdDevEnd]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_str_dev)*100.0/len(data))) 

thirdStdDevStart, thirdStdDevEnd = mean-(3*str_dev), mean+ (3*str_dev)
list_of_data_within_3_str_dev = [result for result in data if result > thirdStdDevStart and result < thirdStdDevEnd]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_str_dev)*100.0/len(data))) 

fig = ff.create_distplot([data], ["RESULT"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[firstStdDevStart, firstStdDevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[firstStdDevEnd, firstStdDevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[secondStdDevStart, secondStdDevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2")) 
fig.add_trace(go.Scatter(x=[secondStdDevEnd, secondStdDevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()