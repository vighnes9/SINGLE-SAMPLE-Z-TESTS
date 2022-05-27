import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()
def random_set_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_mean(100)
    mean_list.append(set_of_mean)
mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("mean = ", mean)
print("Std_dev = ",stdev )
mean2 = statistics.mean(mean_list)
stdev2 = statistics.stdev(mean_list)
print("mean2 = ", mean2)
print("Std_dev2 = ",stdev2 )

first_stdev_start,first_stdev_end = mean - stdev,mean+stdev
second_stdev_start,second_stdev_end = mean -(2*stdev),mean+(2*stdev)
third_stdev_start,third_stdev_end = mean - (3*stdev),mean+(3*stdev)
print("std1 = ",first_stdev_start,first_stdev_end)
print("std2 = ", second_stdev_start,second_stdev_end)
print("std3 = ",third_stdev_start,third_stdev_end)
fig = ff.create_distplot([mean_list], ["Math scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [first_stdev_start,first_stdev_start],y=[0,0.17], mode = "lines", name = "std1"))
fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end],y=[0,0.17], mode = "lines", name = "std1"))
fig.add_trace(go.Scatter(x = [second_stdev_start,second_stdev_start],y=[0,0.17], mode = "lines", name = "std2"))
fig.add_trace(go.Scatter(x = [second_stdev_end,second_stdev_end],y=[0,0.17], mode = "lines", name = "std2"))
fig.add_trace(go.Scatter(x = [third_stdev_start,third_stdev_start],y=[0,0.17], mode = "lines", name = "std3"))
fig.add_trace(go.Scatter(x = [third_stdev_end,third_stdev_end],y=[0,0.17], mode = "lines", name = "std3"))



fig.show()