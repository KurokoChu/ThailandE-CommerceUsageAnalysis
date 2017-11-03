"""
Test : Pulling data by pandas
"""
import pandas as pd
import pygal as pg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

# Import dataset from xls
file = r'(05)00_S-lfs-y_2559_000_000000_00500.xls'
xls = pd.read_excel(file, encoding='UTF-8')

# Data select
axis_x = [year for year in range(2552, 2560)]
axis_x_2 = [year - 543 for year in axis_x]
axis_y = []

# Test1
axis_x_3 = []
for i in xls[xls.columns[0]]:
    if i != 'รวม' and i != 'ภาค' and type(i) is str:
        if i not in axis_x_3 and len(i) < 40:
            axis_x_3.append(i)

# Initialize Bar Chart
chart = pg.Bar(legend_at_bottom=True)

# Chart title
chart.title = 'จำนวนการว่างงาน จำแนกตามภาค พ.ศ. 2552 - 2559'

# X-Axis Label
chart.x_labels = [x for x in axis_x_3]

# Test2
k = 0
for i in xls[xls.columns[1:9]]:
    for j in xls[i]:
        if type(j) is not str:
            if math.isnan(j) is False and j not in axis_x and j not in axis_x_2 \
                    and 20 < j < 200:
                axis_y.append(float('%.04f' % j))

    # Result
    chart.add('พ.ศ.' + str(axis_x[k]), axis_y)
    axis_y = []
    k += 1

# Y-Axis range value
chart.range = [0, 200]
# Render chart
chart.render_to_file('chart.svg')

# Cute Akatsuki
img = mpimg.imread('CzAD3LLUkAAwbsQ.png')

plt.imshow(img)
plt.show()
