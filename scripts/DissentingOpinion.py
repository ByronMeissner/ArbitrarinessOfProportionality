import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Dissenting Decisions', 'Uniform Decisions']
sizes = [4000, 12000]  # Example values, adjust as necessary
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # explode the first slice

# Use a ggplot style for better aesthetics
plt.style.use('ggplot')

plt.figure(figsize=(10, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140, textprops={'fontsize': 14})

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Ratio of Dissenting Decisions to Uniform Decisions', fontsize=18)

# Show the plot
plt.tight_layout()
plt.show()