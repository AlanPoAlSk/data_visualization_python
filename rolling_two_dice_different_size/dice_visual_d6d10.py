import plotly.express as px
from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x' : 'Results', 'y' : 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick = 1)
# If you want to save an html file of the chart
# fig.write_html('dice_visual_d6_d10.html')
fig.show()
    
# print(frequencies)