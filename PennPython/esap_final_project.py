# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

"""
**This is what you'll need to submit on Gradescope:**

1. This notebook, completed.
2. Your data in csv form (as noted in the Data Cleaning section below).
3. Any other code you have written for your project.

# Data cleaning

The first step to data analysis is ensuring that you are focussing on the subset of the data that you have complete information about.

1. Having taken a look at your dataset, what columns and rows have you decided to drop from it? Why?

*A valid reason for dropping a column could be lack of information about the column, lack of a clear understanding of the units of measurement, a general feeling that it does not contain any useful information etc*

If you decided to focus on just a subset of your data please describe why you chose that subset and why you feel the other rows do not matter.

2. If you chose to merge on any additional datasets, include the code for that here.

*Answer in this markdown cell. Add more markdown cells if you want.*

## Exploring the data

Using sorting, groupby etc find out some interesting aspects of the data. Even a short fact counts. For instance, if you were working with population data, you could say that 25% of the world lives in South Asia after you do some group by commands.

In this section of your project try to find as many interesting facts as possible.

# Visualizations

Make at least 6 visualizations (if this number is unreasonable please talk to your mentoring TA before reducing it) that reveal something interesting about the data. Try to include at least one scatterplot and one histogram/bar graph (again, if the data does not lend itself to these plots do let us know

Make sure that your visualizations
1. Have things like the axes, titles, units etc
2. Are telling a slightly interesting story. Interesting = something a person who has not seen this data might not be able to just guess.

Write a few lines telling us what your visualization represents and what it reveals. Discuss any potential hypotheses that could result from these visualizations.

_Write your answer in this markdown cell._
"""

data = pd.read("nba2021_advanced.csv")

print(data)
