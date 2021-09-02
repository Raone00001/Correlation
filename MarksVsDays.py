# Importing all modules
import csv
import numpy as np

# Function to get the data source
def getDataSource(data_path):

    # Array 1
    marks_in_percentage = []

    # Array 2
    days_present = []

    # Reading the path and reading it as a csv file
    with open(data_path) as csv_file:

        # Read the file
        csv_reader = csv.DictReader(csv_file)

        # For each row in the file
        for row in csv_reader:

            # Append the marks 
            marks_in_percentage.append(float(row["Marks In Percentage"]))

            # Append the days
            days_present.append(float(row["Days Present"]))

    # Return the for loop to make an axis
    return {"x":marks_in_percentage,"y":days_present}

# Function to find correlation
def findCorrelation(datasource):

    # Calculate the correlation
    correlation = np.corrcoef(datasource["x"],datasource["y"])

    # Print the correlation
    print("Correlation Between Marks in Percentage and Days Present: - /n --->",correlation[0,1])

# Function to set the data path
def setup():

    # Passing the data path
    data_path = "./data/Student Marks vs Days Present.csv"

    # Getting the data source
    datasource = getDataSource(data_path)

    # Find the correlation
    findCorrelation(datasource)

setup()