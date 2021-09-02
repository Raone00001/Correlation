# Importing all modules
import csv
import numpy as np

# Function to get the data source
def getDataSource(data_path):

    # Array 1
    size_of_tv = []

    # Array 2
    average_time_spent = []

    # Reading the path and reading it as a csv file
    with open(data_path) as csv_file:

        # Read the file
        csv_reader = csv.DictReader(csv_file)

        # For each row in the file
        for row in csv_reader:

            # Append the marks 
            size_of_tv.append(float(row["Size of TV"]))

            # Append the days
            average_time_spent.append(float(row["Average Watching TV"]))

    # Return the for loop to make an axis
    return {"x":size_of_tv,"y":average_time_spent}

# Function to find correlation
def findCorrelation(datasource):

    # Calculate the correlation
    correlation = np.corrcoef(datasource["x"],datasource["y"])

    # Print the correlation
    print("Correlation Between Size of The Tv and Average Time Spent Watching It: - /n --->",correlation[0,1])

# Function to set the data path
def setup():

    # Passing the data path
    data_path = "./data/Size of TV, Average time spent watching TV in a week (hours).csv"

    # Getting the data source
    datasource = getDataSource(data_path)

    # Find the correlation
    findCorrelation(datasource)

setup()