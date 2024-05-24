import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

# Load the data
data = pd.read_csv('data/train.csv')

# Print the first 5 rows of the dataframe
print(data.head())

# Print the shape of the dataframe
print(data.shape)

# Print the column names of the dataframe
print(data.columns)


