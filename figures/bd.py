import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from matplotlib import cm
# from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np

plt.rcParams.update({'font.size': 17})

# my_cmap = cm.get_cmap('tab20', 3)

labels = ['BM', 'CC', 'SSSP']
twitter = [53, 56, 42]
epinion = [7, 9, 36]
wiki = [1.0147352, 0.9099611343, 16.87975362]

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars
dist = 0.15  # the spacing of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - dist, twitter, width, label='twitter', color='#fff2cc', edgecolor='#d6b656') # , color=my_cmap.colors[0])

rects2 = ax.bar(x, epinion, width, color='#dae8fc', edgecolor='#6c8ebf',  label='epinion') # , color=my_cmap.colors[1])

rects3 = ax.bar(x + dist, wiki, width, color='#f8cecc', edgecolor='#b85450', label='wiki') # , color=my_cmap.colors[2])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Speedup')
ax.set_ylim(0.1, 999)
ax.set_yscale('log')
ax.set_title('BigDatalog')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis='y')

fig.tight_layout()

# plt.show()
plt.savefig("basic-bd.png", dpi=300)
