import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from matplotlib import cm
# from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np

plt.rcParams.update({'font.size': 17})

# my_cmap = cm.get_cmap('tab20', 3)

labels = ['BM', 'CC', 'SSSP']
twitter = [32219, 1910, 61]
twitter_sn = [32219, 2286, 146]
epinion = [10710, 4305, 57]
epinion_sn  = [10710, 4086, 91]
wiki = [169, 77, 1.325222748]
wiki_sn  = [169, 60, 0.82469066301]
sn = [0,0,0]

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars
dist = 0.25  # the spacing of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 0.95*dist, twitter_sn, width, color='#fff2cc', edgecolor='#d6b656', hatch='..') # , color=my_cmap.colors[0])
ax.bar_label(rects1, labels=['t.o.', 't.o.', ""])
rects1 = ax.bar(x - 1.55*dist, twitter, width, label='twitter', color='#fff2cc', edgecolor='#d6b656') # , color=my_cmap.colors[0])
ax.bar_label(rects1, labels=['t.o.', 't.o.', ""])

rects2 = ax.bar(x + 0.3*dist, epinion_sn, width, color='#dae8fc', edgecolor='#6c8ebf', hatch='..') # , color=my_cmap.colors[1],
rects2 = ax.bar(x - 0.3*dist, epinion, width, color='#dae8fc', edgecolor='#6c8ebf',  label='epinion') # , color=my_cmap.colors[1])

rects3 = ax.bar(x + 1.55*dist, wiki_sn, width, color='#f8cecc', edgecolor='#b85450', hatch='..') # , color=my_cmap.colors[2]
rects3 = ax.bar(x + 0.95*dist, wiki, width, color='#f8cecc', edgecolor='#b85450', label='wiki') # , color=my_cmap.colors[2])

ax.bar(x + 1.55*dist, sn, width, color='#f5f5f5', edgecolor='#666666', hatch='..', label='semi-naive')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Speedup')
ax.set_ylim(0.1, 100000)
ax.set_yscale('log')
ax.set_title('X')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.grid(axis='y')
ax.legend()

fig.tight_layout()

# plt.show()
plt.savefig("basic-x.png", dpi=300)
