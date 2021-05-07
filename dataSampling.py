import statistics
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

data_frame = pd.read_csv("C:/Users/sravy/White Hat Jr/Project 110- Data Sampling/medium_data.csv")

#using data of "reading_time"
reading_time_data = data_frame["reading_time"].to_list()
population_mean = statistics.mean(reading_time_data)
print("Mean of population -->", population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(reading_time_data) - 1)
        value = reading_time_data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def plot_graph(mean_list, sample_mean):
    df = mean_list
    mean = (statistics.mean(df))
    chart = ff.create_distplot([df], ["Responses"], show_hist = False, colors = ['#0BA1E3'])
    chart.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "Population Mean", line_color = '#00FA85'))
    chart.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 1], mode = "lines", name = "Sample Mean", line_color = '#B519FA', line = dict(dash = 'dash')))
    chart.update_layout(
                font_family = "Papyrus, Fantasy",
                font_size = 20,
                title_text = 'Mean of Population vs Mean of Sample',
                title_x = 0.5,
                title_font_size = 30,
                title_font_color = "#1F14FF",
                legend_font_size = 20,
                legend_font_color = "#51E30B")
    chart.update_xaxes(color = "#00FA85")
    chart.update_yaxes(color = "#51E30B")
    chart.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    sample_mean = statistics.mean(mean_list)
    print("Mean of samples -->", sample_mean)
    plot_graph(mean_list, sample_mean)

setup()