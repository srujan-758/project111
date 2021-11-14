from abc import abstractproperty
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_article.csv")
data = df["reading_time"].tolist()
mean=statistics.mean(data)

population_mean=statistics.mean(data)

def random_set_of_mean(counter):
   dataset=[]
   for i in range(0,counter):
     random_index=random.randint(0,len(data))
     value=data[random_index]
     dataset.append(value)   
   mean=statistics.mean(dataset)
   return mean   
   

mean_list=[]
for i in range(0,100):
    set_of_means=random_set_of_mean(30)
    mean_list.append(set_of_means)


new_sample_mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list) 

def  show_fig(mean_list):
  df=mean_list
  fig=ff.create_distplot([df],["reading_time"],show_hist=False)
  fig.show()

first_std_deviation_start, first_std_deviation_end = new_sample_mean-std_deviation, new_sample_mean+std_deviation
second_std_deviation_start, second_std_deviation_end = new_sample_mean-(2*std_deviation), new_sample_mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = new_sample_mean-(3*std_deviation), new_sample_mean+(3*std_deviation)

fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[new_sample_mean, new_sample_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

new_sample_mean=statistics.mean(first_std_deviation_start,first_std_deviation_end,second_std_deviation_start,second_std_deviation_end,third_std_deviation_start,third_std_deviation_end)
print(new_sample_mean)

z_test=(mean-new_sample_mean)/std_deviation
print("z test is:-",z_test)