# Oscar Avina
# 04/19/2026
# Module 4.2 Assignment
# This program is edited from the original sitka_highs.py file for our M4.2 assignment.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], [] # add lows list to store low temperatures for assignment
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6]) # added low variable to read low temperatures from the file for assignment
        lows.append(low) # added low temperatures to the lows list for assignment

while True: # added while loop to allow user to choose which graph to view for assignment
    print("Menu")
    print("Please type 'high' to view the high temperatures graph.")
    print("Please type 'low' to view the low temperatures graph.")
    print("Please type 'exit' to quit the program.")

    user_input = input("Please enter your choice: ").lower()

    if user_input == 'high': # plots the high temperatures when based on orinal code
        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif user_input == 'low': # added option to plot low temperatures graph for assignment
        # Plot the low temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif user_input == 'exit': # added option to exit the program for assignment
        print("Exiting the program.")
        break

    else:
        print("Invalid input. Please try again.")