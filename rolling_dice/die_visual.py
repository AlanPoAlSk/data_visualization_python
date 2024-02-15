import plotly.express as px
from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results
title = "Results of Rolling One D6 1,000 Times"
labels = {'x' : 'Results', 'y' : 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
# If you want to save an html file of the chart
# fig.write_html('dice_visual_d6.html')
fig.show()
    
# print(frequencies)