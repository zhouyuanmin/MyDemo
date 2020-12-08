import pandas as pd
from matplotlib import pyplot as plt

data = {
    'Avg. Area Income': [79545.45857, 5.317138678, 7.009188143, 23086.8005, 188.2142121, 1059033.558],
    'Price': [80175.75416, 6.011592242, 6.104512439, 26748.42842, 156.5346563, 1068138.074]
}
data = pd.DataFrame(data)

fig = plt.figure(figsize=(5, 4))
fig1 = plt.subplot(111)

plt.scatter(data.loc[:, 'Avg. Area Income'], data.loc[:, 'Price'])
plt.title('Price VS Area Income')
plt.show()
