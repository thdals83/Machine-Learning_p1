import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


titanic=pd.read_csv('titanic.csv')

print(titanic.loc[[2,5,9]])
titanic.loc[[2,5,9]]