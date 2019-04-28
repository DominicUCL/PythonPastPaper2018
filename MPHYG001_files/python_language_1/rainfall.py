# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
from collections import defaultdict
import json
import matplotlib.pyplot as plt
import numpy as np
calendar_dict=defaultdict(list)
with open('C:\\Users\\Domin\\Documents\\MPHYG001-2018\\MPHYG001_files\\MPHYG001_files\\python_language_1\\python_language_1_data.csv', 'r') as f:
    reader = csv.reader(f)
    rownum=0
    for row in reader:
        if rownum!=0:
            calendar_dict[row[0]].append(row[2])
        rownum+=1
with open('C:\\Users\\Domin\\Documents\\MPHYG001-2018\\MPHYG001_files\\MPHYG001_files\\python_language_1\\python_language_1_data.json', 'w') as f:
    json.dump(calendar_dict,f)
    
def json_plotter(file_path,year,line_colour="black"):
    with open(file_path, 'r') as f:
        rainfall_dict = json.load(f)
        if int(year)%4==0:
            xdata=[i+1 for i in range(364)]
        else:
            xdata=[i+1 for i in range(365)]
        ydata=[float(i) for i in rainfall_dict[year]]
        plt.xlim(1, 365)
        plt.xlabel("day of year")
        plt.ylabel("rainfall (mm/day)")
        plt.plot(xdata,ydata,color=line_colour)        
        plt.savefig('timeseries.png')


    return 0
json_plotter('C:\\Users\\Domin\\Documents\\MPHYG001-2018\\MPHYG001_files\\MPHYG001_files\\python_language_1\\python_language_1_data.json',"1998","green")
def json_plotter2(file_path,year1,year2):
    xdata=[]
    ydata=[]
    with open(file_path, 'r') as f:
        rainfall_dict = json.load(f)
        for year in range(year1,year2+1):
            xdata.append(year)
            temp_array=[float(i) for i in rainfall_dict[str(year)]]
            ydata.append(sum(temp_array)/len(temp_array))
        plt.xlabel("year")
        plt.ylabel("average rainfall (mm/day)")
        plt.plot(xdata,ydata)        
        plt.savefig('timeseries2.png')
json_plotter2('C:\\Users\\Domin\\Documents\\MPHYG001-2018\\MPHYG001_files\\MPHYG001_files\\python_language_1\\python_language_1_data.json',1988,2000)

def rainfall_correct_for(year_rain_list):
    """ Using a for loop allows for higher readabilty and smoother ease of change for instance it would be easy yo add another nested loop """
    return_list=[]
    for day in year_rain_list:
        return_list.append(day*1.2**(2.0**0.5))
    return return_list

def rainfall_correct_listcomp(year_rain_list):
    """ list comprehension is generally faster because it uses fast byte code for appending and is optimized for the python intepreter """
    return_list=[day*1.2**(2.0**0.5) for day in year_rain_list]        
    return return_list

        