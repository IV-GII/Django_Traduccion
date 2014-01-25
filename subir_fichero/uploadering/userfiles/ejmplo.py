from pygooglechart import PieChart3D

# Create a chart object of 250x100 pixels
chart = PieChart3D(250, 100)

# Add some data
chart.add_data([20, 10])

# Assign the labels to the pie data
chart.set_pie_labels(['Hello', 'PEPE'])

# Print the chart URL
print chart.get_url()

# Download the chart
chart.download('pie-hello-world.png')
