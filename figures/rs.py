import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from matplotlib import cm
# from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np

plt.rcParams.update({'font.size': 17})

# my_cmap = cm.get_cmap('tab20', 3)

labels = ['BM', 'CC', 'SSSP']
twitter = [3000, 3000, 61]
epinion = [1072, 851, 67]
wiki = [16, 12, 15]

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars
dist = 0.15  # the spacing of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - dist, twitter, width, label='twitter', color='#fff2cc', edgecolor='#d6b656') # , color=my_cmap.colors[0])
ax.bar_label(rects1, labels=['o.o.m.', 'o.o.m.', ""])

rects2 = ax.bar(x, epinion, width, color='#dae8fc', edgecolor='#6c8ebf',  label='epinion') # , color=my_cmap.colors[1])

rects3 = ax.bar(x + dist, wiki, width, color='#f8cecc', edgecolor='#b85450', label='wiki') # , color=my_cmap.colors[2])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Speedup')
ax.set_ylim(0.1, 5000)
ax.set_yscale('log')
ax.set_title('RecStep')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis='y')

fig.tight_layout()

# plt.show()
plt.savefig("basic-rs.png", dpi=300)
