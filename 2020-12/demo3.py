import pandas as pd

data = pd.read_csv('test.csv')
# print(data.head())
# print(type(data))

#康康哪些与价格有关
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(5,4))
fig1 = plt.subplot(111)

plt.scatter(list(data.loc[:,'Avg. Area Income']),list(data.loc[:,'Price']))
plt.title('Price VS Area Income')
plt.show()