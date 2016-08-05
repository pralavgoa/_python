#!/usr/bin/python3


import csv
import numpy as np
import matplotlib.pyplot as plt
#from ipywidgets import widgets

filepath = "data/random-10000-data"
print("Use 'x-y' for range(end including) and 'x,y,z...' for list")
#input_graph_queries = widgets.Text()
def handle_input_queries(sender):
    # Parse input range or list
    if("-" in sender.value):
        queries_to_find = sender.value.split("-")
        queries_to_find = [int(i) for i in queries_to_find]
        queries_to_find = [str(i) for i in range(queries_to_find[0], queries_to_find[1]+1)]
    else:
        queries_to_find = sender.value.split(",")

    # Filter queries from data
    filtered_queries = [] # 2D row.column
    header = []
    for query_id in queries_to_find:
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if not header:
                    header = row
                if row[0] == query_id and row[1] == "2016":
                    filtered_queries.append([int(i) for i in row]);

    # Translate row.column into column.row
    columns = [[] for i in header]
    for row in filtered_queries:
        for i, column in enumerate(row):
            columns[i].append(column)
    print(columns)
    # Draw graph
    #%matplotlib inline
    fig, ax = plt.subplots(figsize=(12, 6))
    bar_width = 0.35
    opacity = 0.4
    #print(columns)
    colors = ["r", "g", "b", "y", "brown"]
    for i, column in enumerate(columns[2:]): # Skip query_id and year
        #print(i, column)
        if 0:
            plt.bar(columns[0], column, bar_width,
                    color=colors[i],
                    label=header[i + 2]) # Skip year and query_id
        else:
            plt.errorbar(columns[0], column, color=colors[i], label=header[i + 2], fmt="b.-")

    plt.xlabel('Query-ID')
    plt.ylabel('Count')
    plt.title('Clinic graph: %s' % sender.value)
    plt.xticks(columns[0])
    plt.legend(bbox_to_anchor=(1.13, 1.05))

    #plt.tight_layout()
    plt.show() # Used for new graph


class A:
    value = "1-10"
handle_input_queries(A())