"""
Chart : Thailand C2C E-commerce Visitors (Million) April - November 2017
"""
import pandas as pd
import pygal as pg
from pygal.style import Style

# Get data from xlsx
file = r'เวิร์กบุ๊ก1.xlsx'
xlsx = pd.read_excel(file, sheet_name=1, encoding='UTF-8')

# Data select
axis_x = [str(month) + '/17' for month in range(4, 12)]
show = [i for i in xlsx[xlsx.columns[1]] if type(i) is str]

# Config style
custom_style = Style(
        background='transparent',
        opacity='.6',
        opacity_hover='.9',
        transition='300ms ease-in',
        )

# Create Line Chart
chart = pg.Line(style=custom_style, legend_at_bottom=True, fill=True,
                x_title='Month/Year', y_title='Million Visitors', show_x_guides=True)
chart.title = 'Thailand C2C E-commerce Visitors April - November 2017'

# X-Axis Label
chart.x_labels = axis_x

# Plot Graph
for i in range(len(show)):
    data = []
    for j in xlsx[xlsx.columns[2:]]:
        data.append(xlsx[j][i])
    chart.add(show[i], data)

# Shows the values to 2 decimal places
chart.value_formatter = lambda x: "%.2f" % x

# Export chart
chart.render_to_file('chart_C2C.svg')
