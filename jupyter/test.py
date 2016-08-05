import csv
import numpy as np
import matplotlib.pyplot as plt
#from ipywidgets import widgets
from matplotlib.font_manager import FontProperties

filepath = "data/random-10000-data"
#input_graph_queries = widgets.Text()
def handle_input_queries(sender):
    # Find queries
    filtered_queries = [] # 2D row.column includes header clinic name
    header = []
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        queries_to_find = sender.value.split(",")
        for row in reader:
            if not header:
                header = row
            if row[0] in queries_to_find:
                filtered_queries.append([int(i) for i in row]);
                                
    # Prepare graph values
    columns = [[] for i in header[1:]]
    for row in filtered_queries:
        for i, column in enumerate(row[1:]):
            columns[i].append(column)
    
    # Draw graph
    #%matplotlib inline
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.4
    print(columns)
    colors = ["r", "g", "b", "y", "brown"]
    for i, column in enumerate(columns[1:]): # Skip year
        print(i, column)
        if 0:
            plt.bar(columns[0], column, bar_width,
                    color=colors[i],
                    label=header[i + 2]) # Skip year and query_id
        else:
            plt.errorbar(columns[0], column, color=colors[i], label=header[i + 2], fmt="b.-")
    
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Clinic graph: ' + sender.value)
    #plt.xticks(columns[0])
    plt.legend(bbox_to_anchor=(1.25, 1.05))

    #plt.tight_layout()
    plt.show() # Used for new graph    
    
    
#input_graph_queries.on_submit(handle_input_queries)
#input_graph_queries
class A:
    value = "1,2"
handle_input_queries(A())
class B:
    value = "4,5,6"
handle_input_queries(B())