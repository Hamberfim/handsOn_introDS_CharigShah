# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:22:43 2021

@author: adhamlin
"""
from operator import itemgetter

rate_dict = {"GEICO": [4.7, 8.3, 9.2],
             "Progressive": [7.4, 6.7, 8.9], "USAA": [3.8, 6.3, 8.1]}

scores = []  # list of tuples


for k, v in rate_dict.items():
    average = k, ((sum(v))/3)  # create a tuple of key and avg
    scores.append(average)  # tuple

print("Average Scores: " + str(scores) + "\n")

print("Highest rated insurance is "
      # gets key item index (1) of each to find the max num, [0] is its name
      + str(max(scores, key=itemgetter(1))[0])
      + " with a average rating of "
      # gets key item index (1) of each to find the max num, [1] is its num
      # rounding it to 2 dec. points
      + str(round(max(scores, key=itemgetter(1))[1], 2)))
